#!/usr/bin/env python
import time
import psycopg2
from django.db import connections
from django.db.utils import OperationalError

def check_db():
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
    except OperationalError:
        return False
    return True

if __name__ == '__main__':
    attempts = 0
    while attempts < 5:
        try:
            if check_db():
                print("Database is ready!")
                break
            else:
                raise Exception("Database not ready")
        except (Exception, psycopg2.OperationalError):
            print("Database unavailable, waiting 1 second...")
            time.sleep(1)
        attempts += 1
