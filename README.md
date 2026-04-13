Below is a **clean, professional, production-grade README** aligned with DevOps, security, and real-world project expectations. It improves structure, adds configuration management, and removes ambiguity.

---

# 📦 Inventory Management System

A lightweight full-stack inventory management application built with **FastAPI, MySQL, and SQLAlchemy**, designed to demonstrate CRUD operations, environment-based configuration, and secure credential handling.

---

## 🚀 Overview

This application enables users to manage product inventory through a simple web interface. It supports adding, viewing, and deleting products while maintaining a clean separation between application logic, database access, and configuration.

---

## ✨ Features

* Create and manage inventory items
* View all products in a structured table
* Delete products by ID
* Track product quantity and pricing
* Highlight low-stock items (UI-level)
* Environment-based configuration (no hardcoded secrets)
* Automatic database and table creation

---

## 🛠️ Technology Stack

| Layer       | Technology                   |
| ----------- | ---------------------------- |
| Backend     | FastAPI                      |
| Database    | MySQL                        |
| ORM         | SQLAlchemy                   |
| Frontend    | HTML, CSS (Jinja2 Templates) |
| Config Mgmt | python-dotenv                |

---

## 📂 Project Structure

```
inventory-management-fastapi/
│
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── database.py      # DB connection & config
│   ├── models.py        # SQLAlchemy models
│   ├── crud.py          # DB operations
│
├── templates/
│   └── index.html       # UI template
│
├── static/
│   └── style.css        # Styling
│
├── .env.example         # Environment template
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuration (IMPORTANT)

This project uses **environment variables** for secure configuration.


### ✅ `.env.example` (for sharing)

```.env.example
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=inventory_db
```

---

## 🧑‍💻 Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/AnbazhaganSekar/inventory-management-fastapi.git
cd inventory-management-fastapi
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

#### Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment

Create `.env.example` file as shown above.

---

### 5. Run Application

```bash
uvicorn app.main:app --reload
```

---

### 6. Access Application

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🗄️ Database Behavior

* Database: `inventory_db`
* Automatically created at startup (if not exists)
* Tables generated via SQLAlchemy ORM

---

## 📡 API Endpoints

| Method | Endpoint       | Description          |
| ------ | -------------- | -------------------- |
| GET    | `/`            | Fetch all products   |
| POST   | `/add`         | Add a new product    |
| GET    | `/delete/{id}` | Delete product by ID |

---

## 📌 Sample Data

| Product | Category    | Quantity | Price |
| ------- | ----------- | -------- | ----- |
| Laptop  | Electronics | 5        | 50000 |
| Mouse   | Accessories | 20       | 500   |

---

## 🔐 Security Considerations

* No hardcoded credentials
* Uses environment variables for secrets
* `.env.example` excluded via `.gitignore`
* Recommended to use:

  * CI/CD secrets (GitHub Actions / Azure DevOps)
  * Cloud secret managers (AWS / Azure / GCP)

---

## 🚧 Future Enhancements

* Authentication & authorization (JWT)
* REST API documentation (Swagger enhancements)
* Docker & Docker Compose setup
* Kubernetes deployment (Secrets + ConfigMaps)
* Role-based access control (RBAC)
* Inventory alerts & notifications

---

## 🧪 Development Notes

* Designed for learning and demonstration purposes
* Suitable for extending into DevOps pipelines
* Can be integrated with CI/CD for automated deployment

---

## 👨‍💻 Author

**Anbazhagan S**

---

## 📄 License

This project is for educational and demonstration purposes.
