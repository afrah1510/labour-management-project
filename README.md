# Labour Management System

A web-based application to efficiently manage labour, attendance, tasks, and payments. Ideal for small and medium-sized organizations to simplify workforce management.  

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

---

## Prerequisites

1. **Python** installed (3.8 or higher recommended)  
2. **MySQL** installed and running  

---
## Virtual Environment Setup (Recommended)

It is recommended to use a virtual environment to keep dependencies isolated:

1. **Navigate to your project folder**

```bash
cd path\to\labor-management-project
```

2. **Create a virtual environment**
```bash
python -m venv my_venv
```

3. **Activate the virtual environment**
Windows
```bash
my_venv\Scripts\activate
```

4. **Install required Python packages inside the virtual environment**
```bash
pip install -r requirements.txt
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
cd labour-management-project
```

2. **Open Command Prompt as Administrator (Windows only)**

3. **Activate the virtual environment**
Windows
```bash
my_venv\Scripts\activate
```

4. **Update configuration files**
- Open config.py and replace
  ```bash
  MYSQL_USER = "root"          # replace with your MySQL username
  MYSQL_PASSWORD = "12345"     # replace with your MySQL password
  ```
- Open run_flask_with_mysql.py and replace
  ```bash
  MYSQL_SERVICE_NAME = "MySQL80"                                           # change if your service name is different
  FLASK_APP_PATH = r"D:\CDAC\Python\labour-management-system\app.py"       # replace with path to your Flask app
  ```

5. **Run the project**
```bash
python run_flask_with_mysql.py
```
> This script automatically starts the MySQL server and launches the Flask app.
> Access the app at http://localhost:5000
