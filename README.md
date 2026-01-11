Employee Management Web Application

A full-stack Employee Management Web Application built using:
Backend: Flask, SQLAlchemy, PostgreSQL
Frontend: HTML, JavaScript (Node build → Nginx)
Database: PostgreSQL
Containerization: Docker & Docker Compose
Deployment: Shell script (deploy.sh)


Features

Add employee details (name, email, department)
View employee list from database
REST API built with Flask
PostgreSQL database integration
Dockerized backend & frontend
One-command deployment using Docker Compose

| Container | Technology                | Port |
| --------- | ------------------------- | ---- |
| frontend  | Nginx (Node build output) | 3000 |
| backend   | Flask + Gunicorn          | 5000 |
| db        | PostgreSQL 15             | 5432 |
| jenkins   | Jenkins CI/CD             | 8080 |

.
├── backend
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── wait-for-db.sh
│
├── frontend
│   ├── src/
│   ├── package.json
│   ├── Dockerfile
│   └── index.html
│
├── docker-compose.yml
├── deploy.sh
└── README.md

Requirements 
Docker
Docker Compose
Git

| Service        | URL                                                                |
| -------------- | ------------------------------------------------------------------ |
| Frontend       | [http://localhost:3000](http://localhost:3000)                     |
| Backend Health | [http://localhost:5000/health](http://localhost:5000/health)       |
| Employees API  | [http://localhost:5000/employees](http://localhost:5000/employees) |






CI/CD Workflow Overview

GitHub Commit / Push
        |
        ▼
Jenkins Pipeline Triggered
        |
        ▼
Pull Latest Code
        |
        ▼
Build Docker Images
        |
        ▼
Run Containers (docker-compose)
        |
        ▼
Health Check
        |
        ▼
Deployment Complete 






Jenkins Architecture

Jenkins Server: Installed on EC2 / VM


Docker: Installed on Jenkins server


Docker Compose: Used for multi-container deployment


GitHub Repo: Source code repository





Pipeline Stages Explained


Stage	Description


Checkout Code	Pulls latest code from GitHub


Stop Containers	Stops old containers safely


Build Images	Builds backend & frontend images


Start Application	Starts services via Docker Compose


Health Check	Verifies backend availability


| Stage             | Description                          |
| ----------------- | ------------------------------------ |
| Checkout Code     | Pulls latest code from GitHub        |
| Stop Containers   | Stops existing containers safely     |
| Build Images      | Builds backend and frontend images   |
| Start Application | Starts services using Docker Compose |
| Health Check      | Verifies backend availability        |





Docker Compose Used in Pipeline



Jenkins uses your existing:


docker-compose.yml


Services deployed:


PostgreSQL


Flask Backend


Frontend (Nginx)


Verification After Deployment
Backend
curl http://<jenkins-server-ip>:5000/health

Frontend
http://<jenkins-server-ip>:3000






Docker Services

Backend

Python 3.11
Gunicorn server
Flask + SQLAlchemy
Runs on port 5000

Frontend

Node 20 build stage
Served via Nginx
Runs on port 3000
Database
PostgreSQL 15
Persistent volume enabled


Environment Variables
Backend uses the following environment variables (set via Docker Compose):
DATABASE_URL=postgresql://postgres:password@db:5432/postgres


Troubleshooting
Backend not responding?
docker compose logs backend

Database issues?
docker compose logs db



Rebuild everything cleanly
docker compose down -v
docker compose up --build


//Future Improvements\\


 Add frontend form for employee creation

 
 Add authentication

 
 Add pagination & search

 
 Add CI/CD with Jenkins

 
 Add Kubernetes deployment
