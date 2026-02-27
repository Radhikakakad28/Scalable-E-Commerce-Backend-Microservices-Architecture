# 🛒 Scalable E-Commerce Backend (Microservices Architecture)

A scalable microservices-based backend system for an E-Commerce platform built using **FastAPI** and clean architecture principles.

This project demonstrates how modern backend systems are designed using **Microservices Architecture**, **REST APIs**, and **modular services**.

---

## 🚀 Features

- Microservices Architecture
- REST API Design
- Product Service
- Clean Code Structure
- Modular Services
- FastAPI Backend
- Swagger API Documentation
- Scalable Architecture

---

## 🏗 Architecture

This project follows a microservices architecture where each service runs independently.

Microservices provide:

- Scalability
- Fault Isolation
- Independent Deployment

Microservices allow each service to scale independently and improve system reliability. :contentReference[oaicite:0]{index=0}

---

## 📂 Project Structure
ecommerce_microservices/
│
├── product-service/
│ ├── app/
│ │ ├── api/
│ │ │ └── routes.py
│ │ ├── schemas/
│ │ │ └── product.py
│ │ └── main.py
│ │
│ ├── requirements.txt
│ └── venv/

---
## ⚙️ Installation

### 1️⃣ Clone Repository
git clone https://github.com/Radhikakakad28/Scalable-E-Commerce-Backend-Microservices-Architecture.git

cd Scalable-E-Commerce-Backend-Microservices-Architecture/product-service

---
### 2️⃣ Create Virtual Environment
python -m venv venv

Activate:
venv\Scripts\activate

---
### 3️⃣ Install Dependencies
pip install fastapi uvicorn pydantic

---
### 4️⃣ Run Server
python -m uvicorn app.main:app --reload

Server runs at:
http://127.0.0.1:8000

Swagger Docs:
http://127.0.0.1:8000/docs

---
## 📡 API Endpoints
### Home

---
## 🧪 API Documentation
Swagger UI:
http://127.0.0.1:8000/docs


---

## 🛠 Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- REST APIs

---

## 🎯 Use Case

This project demonstrates how scalable backend systems are designed using microservices.

Suitable for:

- Backend Engineering
- Microservices Learning
- REST API Development
- System Design Practice

---

## 👩‍💻 Author

**Radhika Kakad**

AI & Data Science Student

---

## ⭐ Future Improvements

- Cart Service
- Order Service
- Docker Deployment
- Database Integration
- API Gateway

Upload Steps
git add .
git commit -m "Added Scalable E-Commerce Backend Microservices Project"
git push

