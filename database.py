from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()  # reads .env file and adds values to os.environ
DATABASE_URL = os.getenv("DATABASE_URL")
SSL_CERT_PATH = os.getenv("SSL_CERT_PATH")

engine = create_engine(
    DATABASE_URL,
    connect_args={"ssl": {
        "ssl_ca": SSL_CERT_PATH
        }
    }
)


def load_jobs_from_db():
    # Use text() to wrap raw SQL
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs")) #select from database

        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
        return jobs


