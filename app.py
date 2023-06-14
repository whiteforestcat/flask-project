from flask import (
    Flask,  # flask is library name, Flask is class in flask library
    render_template,
    jsonify, # to return json in endpoints
)

app = Flask(__name__)
# print(__name__)

# dummy data
dummy_jobs = [
    {"id": 1, "title": "Data Analyst", "location": "Singapore", "salary": 4000},
    {"id": 2, "title": "Backend Engineer", "location": "Singapore", "salary": 4000},
    {"id": 3, "title": "Frontend Engineer", "location": "Singapore", "salary": 4000},
    {"id": 3, "title": "Full Stack Engineer", "location": "Singapore"},
]


# remember that @ is decorator
@app.route("/")
def hello_world():
    return render_template(
        "home.html",
        jobs=dummy_jobs,
        name="Amir"
        # dummy_jobs is now accessible in home.html
    )  # flask looks for html file in specifically a templates folder


# by default, ("/static/xxx.png") route will show you the image

@app.route("/api/jobs")
def list_jobs():
    return jsonify(dummy_jobs)