# 📦 Inventory Management System

A full-stack web application built using **FastAPI, MySQL, HTML, and CSS** to manage product inventory, stock levels, and availability.

---

## 🚀 Features

* Add new products
* View all inventory items
* Delete products
* Track quantity and pricing
* Highlight low stock items
* Clean table-based UI with background theme

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Database:** MySQL
* **Frontend:** HTML, CSS
* **ORM:** SQLAlchemy

---

## 📂 Project Structure

```
inventory_project/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/AnbazhaganSekar/inventory-management-fastapi.git
cd inventory-management-fastapi
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Run Application

```
uvicorn app.main:app --reload
```

---

### 5. Open in Browser

```
http://127.0.0.1:8000
```

---

## 🗄️ Database

* MySQL database: `inventory_db`
* Tables are created automatically using SQLAlchemy

---

## 📬 API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| GET    | `/`            | View all products |
| POST   | `/add`         | Add new product   |
| GET    | `/delete/{id}` | Delete product    |

---

## 📌 Sample Data

Example products:

| Product | Category    | Quantity | Price |
| ------- | ----------- | -------- | ----- |
| Laptop  | Electronics | 5        | 50000 |
| Mouse   | Accessories | 20       | 500   |

---

## 🎯 Key Highlights

* Real-time inventory tracking
* Clean UI with table layout
* Low stock alert (highlighted in red)
* Integrated backend and database

---

## 👨‍💻 Author

Anbazhagan S
