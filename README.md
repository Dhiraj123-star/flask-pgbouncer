
# 🚀 Flask + PostgreSQL + PgBouncer (Dockerized)

A minimal production-style setup for running a **Flask application** with a **PostgreSQL database** and **PgBouncer connection pooling**, fully containerized using **Docker** and **Docker Compose**.

---

## 🌐 Core Functionality

* ⚡ **Flask API**
  Lightweight backend application powered by Flask.

* 🗄️ **PostgreSQL Database**
  Reliable relational database to store application data.

* 🔄 **PgBouncer Connection Pooling**
  Efficiently manages database connections, reduces overhead, and improves performance.

* 🛠️ **Database Connection & Models**
  Centralized `db.py` module for database initialization and user model definition.

* 📦 **CRUD API Endpoints**
  RESTful API endpoints in `main.py` for creating, reading, updating, and deleting users.

* 🐳 **Dockerized Setup**
  Each service (Flask, Postgres, PgBouncer) runs in its own container for easy portability and scalability.

* 🔐 **Environment-Based Configuration**
  Credentials and database settings managed via `.env` for security and flexibility.

---

## ✅ Features

* Connection pooling with **PgBouncer**
* Isolated **Flask API backend**
* Persistent **PostgreSQL storage**
* Full **CRUD API support**
* Centralized **database connection handling**
* Simple **Docker Compose orchestration**
* Secure **environment variable management**

---

## 🎯 Use Cases

* Building scalable Flask applications
* Testing Flask + Postgres integrations in a containerized environment
* Learning how to implement database connection pooling with PgBouncer
* Practicing CRUD API development with Flask + SQLAlchemy
* Local development setup mimicking production-style infrastructure

