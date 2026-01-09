from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
import time

app = Flask(__name__)

# ------------------------
# Database configuration
# ------------------------
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "employee_db")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgres")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ------------------------
# Database model
# ------------------------
class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)

# ------------------------
# Auto-migration (FIXED)
# ------------------------
def migrate():
    with app.app_context():
        retries = 5
        while retries > 0:
            try:
                db.create_all()
                print("Database migrated successfully")
                return
            except Exception as e:
                print("Waiting for DB...", e)
                retries -= 1
                time.sleep(3)
        raise Exception("Database not ready")

# ------------------------
# Routes
# ------------------------
@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

@app.route("/employees", methods=["GET"])
def get_employees():
    employees = Employee.query.all()
    return jsonify([
        {"id": e.id, "name": e.name, "role": e.role}
        for e in employees
    ])

@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.json
    emp = Employee(name=data["name"], role=data["role"])
    db.session.add(emp)
    db.session.commit()
    return jsonify({"message": "Employee added"}), 201

# ------------------------
# Entrypoint
# ------------------------
if __name__ == "__main__":
    migrate()
    app.run(host="0.0.0.0", port=5000)
