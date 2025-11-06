from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
import mysql.connector
from mysql.connector import Error
import config

app = Flask(__name__)
app.secret_key = "team2_data_dynamics_dbms"  # for session and flash

# ===================== DATABASE CONNECTION =====================
try:
    db = mysql.connector.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        database=config.MYSQL_DB
    )
    cursor = db.cursor(dictionary=True)
except Error as e:
    print("Database connection failed:", e)

# ===================== LOGIN REQUIRED DECORATOR =====================
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin_id" not in session:
            flash("Please log in first.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

# ===================== INDEX =====================
@app.route("/")
def index():
    return render_template("index.html")

# ===================== ADMIN =====================
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            cursor.execute("INSERT INTO admin (username, password) VALUES (%s, %s)", (username, password))
            db.commit()
            flash("Admin registered successfully!", "success")
            return redirect(url_for("login"))
        except Error as e:
            db.rollback()
            return render_template("error.html", message="Database error: " + str(e))
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cursor.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (username, password))
        admin = cursor.fetchone()
        if admin:
            session["admin_id"] = admin["admin_id"]
            session["username"] = admin["username"]
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials", "danger")
    return render_template("login.html")


@app.route("/forgetpassword", methods=["GET", "POST"])
def forgetpassword():
    if request.method == "POST":
        username = request.form["username"]
        new_password = request.form["new_password"]
        try:
            cursor.execute("UPDATE admin SET password=%s WHERE username=%s", (new_password, username))
            db.commit()
            flash("Password updated successfully!", "success")
            return redirect(url_for("login"))
        except Error as e:
            db.rollback()
            return render_template("error.html", message="Database error: " + str(e))
    return render_template("forgetpassword.html")


@app.route("/logout")
@login_required
def logout():
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for("index"))


@app.route("/home")
@login_required
def home():
    return render_template("home.html")


# ===================== LABOUR =====================
@app.route("/register_labour", methods=["GET", "POST"])
@login_required
def register_labour():
    if request.method == "POST":
        try:
            name = request.form["name"]
            gender = request.form["gender"]
            age = request.form["age"]
            contact = request.form["contact"]
            address = request.form["address"]
            skill = request.form["skill"]

            cursor.execute("""
                INSERT INTO labour (name, gender, age, contact, address, skill)
                VALUES (%s,%s,%s,%s,%s,%s)
            """, (name, gender, age, contact, address, skill))
            db.commit()
            flash("Labour registered successfully!", "success")
            return redirect(url_for("home"))
        except Error as e:
            db.rollback()
            return render_template("error.html", message="Error registering labour: " + str(e))
    return render_template("register_labour.html")


@app.route("/view_labour", methods=["GET", "POST"])
@login_required
def view_labour():
    labours = []
    searched = False
    try:
        if request.method == "POST":
            labour_id = request.form.get("labour_id")
            if labour_id:
                cursor.execute("SELECT * FROM labour WHERE labour_id=%s", (labour_id,))
            else:
                cursor.execute("SELECT * FROM labour")
            labours = cursor.fetchall()
            searched = True
        else:
            cursor.execute("SELECT * FROM labour")
            labours = cursor.fetchall()
    except Error as e:
        return render_template("error.html", message="Error loading labour data: " + str(e))
    return render_template("view_labour.html", labours=labours, searched=searched)


# ===================== PROJECT =====================
@app.route("/add_project", methods=["GET", "POST"])
@login_required
def add_project():
    if request.method == "POST":
        try:
            name = request.form.get("name")
            location = request.form.get("location")
            start_date = request.form.get("start_date")
            end_date = request.form.get("end_date") or None
            status = request.form.get("status", "Ongoing")

            cursor.execute(
                "INSERT INTO project (name, location, start_date, end_date, status) VALUES (%s,%s,%s,%s,%s)",
                (name, location, start_date, end_date, status)
            )
            db.commit()
            flash("Project added successfully!", "success")
            return redirect(url_for("view_project"))
        except Error as e:
            db.rollback()
            return render_template("error.html", message="Error adding project: " + str(e))
    return render_template("add_project.html")


@app.route("/view_project", methods=["GET"])
@login_required
def view_project():
    project_id = request.args.get("project_id")  # from search form

    try:
        if project_id:
            sql = "SELECT * FROM project WHERE project_id = %s"
            cursor.execute(sql, (project_id,))
        else:
            sql = "SELECT * FROM project"
            cursor.execute(sql)
        projects = cursor.fetchall()
    except Error as e:
        return render_template("error.html", message="Error loading projects: " + str(e))

    return render_template("view_project.html", projects=projects)


# ===================== ASSIGN PROJECT =====================
@app.route("/assign_project", methods=["GET", "POST"])
@login_required
def assign_project():
    try:
        cursor.execute("SELECT labour_id, name FROM labour")
        labours = cursor.fetchall()
        cursor.execute("SELECT project_id, name FROM project")
        projects = cursor.fetchall()

        if request.method == "POST":
            labour_id = request.form["labour_id"]
            project_id = request.form["project_id"]
            assigned_date = request.form.get("assigned_date")
            cursor.execute(
                "INSERT INTO assignment (labour_id, project_id, assigned_date) VALUES (%s,%s,%s)",
                (labour_id, project_id, assigned_date if assigned_date else None)
            )
            db.commit()
            flash("Labour assigned to project!", "success")
            return redirect(url_for("assign_project"))

        cursor.execute("""
            SELECT a.assignment_id, l.name AS labour_name, p.name AS project_name, a.assigned_date
            FROM assignment a
            JOIN labour l ON a.labour_id = l.labour_id
            JOIN project p ON a.project_id = p.project_id
        """)
        assignments = cursor.fetchall()
    except Error as e:
        db.rollback()
        return render_template("error.html", message="Error assigning project: " + str(e))

    return render_template("assign_project.html", labours=labours, projects=projects, assignments=assignments)


# ===================== ATTENDANCE =====================
@app.route("/mark_attendance", methods=["GET", "POST"])
@login_required
def mark_attendance():
    cursor.execute("SELECT labour_id, name FROM labour")
    labours = cursor.fetchall()

    if request.method == "POST":
        try:
            labour_id = request.form["labour_id"]
            date = request.form["date"]
            status = request.form["status"]
            cursor.execute(
                "INSERT INTO attendance (labour_id, date, status) VALUES (%s,%s,%s)",
                (labour_id, date, status)
            )
            db.commit()
            flash("Attendance marked!", "success")
            return redirect(url_for("mark_attendance"))
        except Error as e:
            db.rollback()
            return render_template("error.html", message="Error marking attendance: " + str(e))
    return render_template("mark_attendance.html", labours=labours)


@app.route("/view_attendance", methods=["GET", "POST"])
@login_required
def view_attendance():
    try:
        searched = False
        if request.method == "POST":
            labour_id = request.form.get("labour_id")
            cursor.execute("""
                SELECT a.attendance_id, l.name AS labour_name, a.date, a.status
                FROM attendance a
                JOIN labour l ON a.labour_id = l.labour_id
                WHERE a.labour_id = %s
            """, (labour_id,))
            attendances = cursor.fetchall()
            searched = True
        else:
            cursor.execute("""
                SELECT a.attendance_id, l.name AS labour_name, a.date, a.status
                FROM attendance a
                JOIN labour l ON a.labour_id = l.labour_id
            """)
            attendances = cursor.fetchall()
    except Error as e:
        return render_template("error.html", message="Error loading attendance: " + str(e))

    return render_template("view_attendance.html", attendances=attendances, searched=searched)


# ===================== WAGES =====================
@app.route("/add_wages", methods=["GET", "POST"])
@login_required
def add_wages():
    cursor.execute("SELECT labour_id, name FROM labour")
    labours = cursor.fetchall()

    if request.method == "POST":
        try:
            labour_id = request.form["labour_id"]
            amount = request.form["amount"]
            payment_date = request.form.get("payment_date")
            cursor.execute(
                "INSERT INTO wages (labour_id, amount, payment_date) VALUES (%s,%s,%s)",
                (labour_id, amount, payment_date if payment_date else None)
            )
            db.commit()
            flash("Wages added successfully!", "success")
            return redirect(url_for("add_wages"))
        except Error as e:
            db.rollback()
            return render_template("error.html", message="Error adding wages: " + str(e))

    return render_template("add_wages.html", labours=labours)


@app.route("/view_wages", methods=["GET"])
@login_required
def view_wages():
    labour_id = request.args.get("labour_id")

    try:
        if labour_id:
            cursor.execute("""
                SELECT w.wage_id, l.name AS labour_name, w.amount, w.payment_date
                FROM wages w
                JOIN labour l ON w.labour_id = l.labour_id
                WHERE w.labour_id = %s
            """, (labour_id,))
        else:
            cursor.execute("""
                SELECT w.wage_id, l.name AS labour_name, w.amount, w.payment_date
                FROM wages w
                JOIN labour l ON w.labour_id = l.labour_id
            """)
        wages = cursor.fetchall()
    except Error as e:
        return render_template("error.html", message="Error loading wages: " + str(e))

    return render_template("view_wages.html", wages=wages)


# ===================== GLOBAL ERROR HANDLER =====================
@app.errorhandler(Exception)
def handle_exception(e):
    return render_template("error.html", message="Unexpected error: " + str(e)), 500


# ===================== RUN APP =====================
if __name__ == "__main__":
    app.run(debug=True)
