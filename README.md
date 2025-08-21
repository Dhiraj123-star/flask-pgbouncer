
# 🚀 Flask + PostgreSQL + PgBouncer (Dockerized)

A minimal **production-style setup** for running a **Flask application** with a **PostgreSQL database** and **PgBouncer connection pooling**, fully containerized using **Docker** and **Docker Compose**. Includes **CI/CD with GitHub Actions** for automatic Docker image builds and pushes to DockerHub.

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

* ⚙️ **CI/CD with GitHub Actions**
  Automates Docker image builds and pushes to DockerHub (`dhiraj918106/...`) on every push to `main`.

---

## ✅ Features

* Connection pooling with **PgBouncer**
* Isolated **Flask API backend**
* Persistent **PostgreSQL storage**
* Full **CRUD API support**
* Centralized **database connection handling**
* Simple **Docker Compose orchestration**
* Secure **environment variable management**
* Automated **DockerHub builds via CI/CD**

---

## 🎯 Use Cases

* Building scalable Flask applications
* Testing Flask + Postgres integrations in a containerized environment
* Learning how to implement database connection pooling with PgBouncer
* Practicing CRUD API development with Flask + SQLAlchemy
* Local development setup mimicking production-style infrastructure
* Continuous Integration & Deployment with DockerHub publishing

