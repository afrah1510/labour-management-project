# Labor Management System

A web-based application to efficiently manage labor, attendance, tasks, and payments. Ideal for small and medium-sized organizations to simplify workforce management.  

---

## Features

The **Labor Management System** provides the following functionalities:

- **Register Labour** – Add new laborers to the system.
- **View Labour** – Browse and manage existing labor records.
- **Add Project** – Create new projects for labor assignments.
- **View Project** – See all existing projects and their details.
- **Assign Project** – Allocate laborers to specific projects.
- **Mark Attendance** – Record daily attendance for laborers.
- **View Attendance** – Review attendance records for all laborers.
- **Add Wages** – Input wage details for laborers.
- **View Wages** – View and manage wage records.

> Each feature is accessible from the dashboard with intuitive icons for easy navigation.
 

---

## Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS
- **Database:** MySQL  
- **Python Packages:** `flask`, `mysql-connector-python`  

---

## Prerequisites

1. **Python** installed (3.8 or higher recommended)  
2. **MySQL** installed and running  
3. **Required Python packages**

```bash
pip install flask mysql-connector-python
```

---

## Database setup files

- **schema.sql** – Contains table definitions
- **triggers.sql** – Contains triggers
- **data.sql** – Contains sample data

> Make sure the database is created and ready before running the project.

---

# Installation & Running the Project

1. **Clone the repository**
```bash
git clone https://github.com/afrah1510/labour-management-project.git
cd labor-management-project
```

2. **Open Command Prompt as Administrator (Windows only)**

3. **Run the project**
```bash
python run_flask_with_mysql.py
```
> This script automatically starts the MySQL server and launches the Flask app.
> Access the app at http://localhost:5000
