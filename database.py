from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()   # makes env variables accessible in this file

db_connection_string = os.environ.get("DB_CONNECTION_STR")
# db_connection_string = "mysql+pymysql://tblnsbl73aao5sctbvq3:pscale_pw_pF78NgRaeG3Gjn12yy9BASZkPpymiqv1AU8wcuQRkgQ@aws.connect.psdb.cloud/flaskp1?charset=utf8mb4"


engine = create_engine(
    db_connection_string,
    connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}},
)

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM jobs"))
#     result_all = result.all()
#     # xxx.all() to print all the associated rows
#     # need to store result.all() into a variable cos result.all() can only be called once
#     result_dicts = (
#         []
#     )  # result.all() is an sqlalchemy data structure, need to convert into normal dict
#     for row in result_all:
#         result_dicts.append(row._mapping)
#     print(result_dicts[0])
#     print(result_dicts[1])
#     print(result_dicts)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        result_all = result.all()
        # xxx.all() to print all the associated rows
        # need to store result.all() into a variable cos result.all() can only be called once
        db_jobs = (
            []
        )  # result.all() is an sqlalchemy data structure, need to convert into normal dict
        for row in result_all:
            db_jobs.append(row._mapping)
        # print(jobs[0])
        # print(jobs[1])
        return db_jobs
