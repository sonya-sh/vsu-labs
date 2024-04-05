import psycopg2

conn = psycopg2.connect(
    database="lab_injections",
    user="postgres",
    password="11513",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

username = "alice"
password = "new_pass_alice"

#username = "alice' OR ''='"
#password = ""

cur.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';")

#cur.execute("SELECT * FROM users WHERE username = %s AND password = %s;", (username, password))

result = cur.fetchall()
print(result)

cur.close()
conn.close()

