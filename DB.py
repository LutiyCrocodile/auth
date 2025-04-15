import MySQLdb as mdb
import os
from dotenv import load_dotenv
import hashlib

load_dotenv()


class DataBase:
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASS: str | None = os.environ.get("DB_PASS")
    SCHEMA: str = os.environ.get("SCHEMA")
    SSL: dict | None = os.environ.get("SSL")
    try:

        def auth(self, login_in, passwd, SSL_in: bool | None = None):
            connection = mdb.connect(
                host=self.DB_HOST,
                user=self.DB_USER,
                password=self.DB_PASS,
                database=self.SCHEMA,
                ssl=self.SSL if SSL_in is not None else None,
            )
            log = hashlib.md5(login_in.encode("utf-8")).hexdigest()
            password = hashlib.md5(passwd.encode("utf-8")).hexdigest()
            cur = connection.cursor()
            rows = cur.execute(
                f"SELECT last_name, name, middle_name FROM employees WHERE login = '{log}' and password = '{password}';"
            )
            data = cur.fetchone()
            cur.close()
            if data is not None:
                return data
            else:
                return 0

    except Exception as e:
        print(f"[INFO] {e}")


db = DataBase()
