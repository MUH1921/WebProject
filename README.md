---
# 🧑‍🎓 Student Registration App (Django + PostgreSQL)
```markdown


This is a basic **Student Registration Web Application** built using the **Django** framework and **PostgreSQL** as the database.  
The app allows users to register students with their **name, age, and class**, and view all registered students in a clean, responsive UI using **Bootstrap**.

---

## 📌 How to Build This

✅ Setup Django project  
✅ Configure PostgreSQL as the database in `student_project/student_project/settings.py` like below:  

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'student_db',         # Your database name
        'USER': 'postgres',           # Your PostgreSQL username
        'PASSWORD': 'yourpassword',   # Your PostgreSQL password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

✅ Create a `Student` model  
✅ Build student registration form (name, age, class)  
✅ Create views and URL routing  
✅ Develop templates using HTML + Bootstrap  
✅ Display list of registered students

---

## 🛠️ Prerequisites

Make sure the following are installed on your system:

- Python
- pip
- PostgreSQL
- Django (`pip install django`)
- psycopg2 (`pip install psycopg2` or `pip install psycopg2-binary`)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/MUH1921/WebProject.git
cd WebProject
```

---

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Your PostgreSQL Database

Open `student_project/student_project/settings.py` and update the `DATABASES` section with your PostgreSQL credentials.

---

### 5. Apply Migrations

```bash
cd student_project
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Run the Development Server

```bash
python manage.py runserver
```

Then visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to use the app.

---

## ✨ Features

- 🔐 Secure student registration form
- 🎨 Clean and modern UI with Bootstrap
- 📋 View a list of all registered students
- 💾 Uses PostgreSQL for persistent storage

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 📬 Contact

For any issues, suggestions, or contributions, feel free to reach out or create a pull request.

GitHub Repo: [MUH1921/WebProject](https://github.com/MUH1921/WebProject)
```

---

Let me know if you want to add screenshots, demo video, deployment guide (e.g., on Heroku), or a `requirements.txt` generator!
