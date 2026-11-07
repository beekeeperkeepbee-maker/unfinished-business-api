from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Allow the web app (on github.io) to talk to this server

DATA_FILE = "database.json"

# --- Helper functions ---

def load_data():
    """Load the data from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {"unfinished": [], "finished": []}

def save_data(data):
    """Save the data to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# --- Routes ---

@app.route("/", methods=["GET"])
def home():
    """A simple health check. If you see this in the browser, the server works."""
    return jsonify({"status": "Unfinished Business API is running"})

@app.route("/projects", methods=["GET"])
def get_projects():
    """Return all projects (both unfinished and finished)."""
    data = load_data()
    return jsonify(data)

@app.route("/projects", methods=["POST"])
def add_project():
    """Add a new project to the unfinished list."""
    data = load_data()
    new_project = request.json.get("name", "").strip()

    if not new_project:
        return jsonify({"error": "Project name cannot be empty"}), 400

    data["unfinished"].append(new_project)
    save_data(data)
    return jsonify({"message": f"Added '{new_project}'", "data": data})

@app.route("/projects/finish/<int:index>", methods=["POST"])
def finish_project(index):
    """Move a project from unfinished to finished."""
    data = load_data()

    if index < 0 or index >= len(data["unfinished"]):
        return jsonify({"error": "Invalid project index"}), 404

    finished_name = data["unfinished"].pop(index)
    data["finished"].append(finished_name)
    save_data(data)
    return jsonify({"message": f"Finished '{finished_name}'", "data": data})

@app.route("/projects/delete/<int:index>", methods=["POST"])
def delete_project(index):
    """Delete a project (in a real app, we'd also check the shame letter)."""
    data = load_data()

    if index < 0 or index >= len(data["unfinished"]):
        return jsonify({"error": "Invalid project index"}), 404

    removed_name = data["unfinished"].pop(index)
    save_data(data)
    return jsonify({"message": f"Deleted '{removed_name}'", "data": data})

# --- Run the server ---

if __name__ == "__main__":
    # For local development only
    app.run(debug=True, host="0.0.0.0", port=5000)
