import sqlite3
from classes import Task

def query_db(sql_query):
    with sqlite3.connect("todo.db") as conn:
        cur=conn.cursor()
        cur.execute(sql_query)
        return cur.fetchall()

def insert(name, description, date, table="todo"):
    query_db(f"INSERT INTO {table} VALUES (NULL, '{name}', '{description}', '{date}');")

def read(table="todo"):
    return query_db(f"SELECT * FROM {table}")

def read_id(task_id, table="todo"):
    return query_db(f"SELECT * FROM {table} WHERE id={task_id}")

def delete(task_id, table="todo"):
    query_db(f"DELETE FROM {table} WHERE id={task_id}")

def update_description(name, description, date, task_id, table="todo"):
    query_db(f"UPDATE {table} SET name='{name}', description='{description}', date='{date}' WHERE id={task_id};")
