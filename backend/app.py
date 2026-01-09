from flask import Flask, jsonify, request
import psycopg2
import psycopg2.extras
import os

app = Flask(__name__)


DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "dbname": os.getenv("DB_NAME", "employee_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "postgres"),
    "port": os.getenv("DB_PORT", "5432")
}

def get_db():
    try:
        return psycopg2.connect(**DB_CONFIG)
    except Exception as e:
        print(" Database connection failed:", e)
        raise


@app.route("/")
def health():
    return jsonify({"status": "Employee Backend Running"})


@app.route("/debug")
def debug():
    return jsonify({
        "DB_HOST": DB_CONFIG["host"],
        "DB_NAME": DB_CONFIG["dbname"],
        "DB_USER": DB_CONFIG["user"],
        "DB_PORT": DB_CONFIG["port"]
    })


@app.route("/api/employees", methods=["GET"])
def get_employees():
    try:
        conn = get_db()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT id, name, role FROM employees;")
        rows = cur.fetchall()

        employees = [
            {"id": row["id"], "name": row["name"], "role": row["role"]}
            for row in rows
        ]

        cur.close()
        conn.close()
        return jsonify(employees)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/employees", methods=["POST"])
def add_employee():
    try:
        data = request.get_json()

        if not data or "name" not in data or "role" not in data:
            return jsonify({"error": "name and role are required"}), 400

        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO employees (name, role) VALUES (%s, %s);",
            (data["name"], data["role"])
        )
        conn.commit()

        cur.close()
        conn.close()
        return jsonify({"message": "Employee added"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def migrate():
    # create tables here
    db.create_all()

if __name__ == "__main__":
    migrate()
    app.run(host="0.0.0.0", port=5000)
