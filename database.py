from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://r5ijilveql67r8mcxre0:pscale_pw_87qVcs9Ckwn68S4suj64ixEjgHgP9ll3KOBSGgGuxBb@aws.connect.psdb.cloud/flaskp1?charset=utf8mb4",
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    },
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    print(result.all())  # xxx.all() to print all the associated rows
