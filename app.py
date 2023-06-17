from flask import (
    Flask,  # flask is library name, Flask is class in flask library
    render_template,
    jsonify,  # to return json in endpoints
)
from database import (
    load_jobs_from_db,  # importing engine from database.py file
    load_single_job,
)

app = Flask(__name__)
# print(__name__)

# # dummy data
# dummy_jobs = [
#     {"id": 1, "title": "Data Analyst", "location": "Singapore", "salary": 4000},
#     {"id": 2, "title": "Backend Engineer", "location": "Singapore", "salary": 4000},
#     {"id": 3, "title": "Frontend Engineer", "location": "Singapore", "salary": 4000},
#     {"id": 3, "title": "Full Stack Engineer", "location": "Singapore"},
# ]


# # remember that @ is decorator
# @app.route("/")
# def hello_world():
#     return render_template(
#         "home.html",
#         jobs=dummy_jobs,
#         name="Amir"
#         # dummy_jobs is now accessible in home.html
#     )  # flask looks for html file in specifically a templates folder


# remember that @ is decorator
@app.route("/")
def hello_world():
    db_jobs = load_jobs_from_db()  # storing return result of function into variable
    return render_template(
        "home.html",
        jobs=db_jobs,
        name="Amir"
        # dummy_jobs is now accessible in home.html
    )  # flask looks for html file in specifically a templates folder


# by default, ("/static/xxx.png") route will show you the image


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    print(type(jobs))
    return jsonify(jobs)
    # return render_template("rawdata.html", jobs=jobs)


@app.route("/job/<id>")
def show_job(id):
    job = load_single_job(id)
    return render_template("jobpage.html", job=job)


if __name__ == "__main__":
    app.run(debug=True)
