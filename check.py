import pymysql.cursors

table = "dresses"

con = pymysql.connect(host='localhost',
                      user='root',
                      password='Ab123456',
                      db='shein',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
cur = con.cursor()
with cur:
    cur.execute(f"""select * from {table}""")
    con.commit()
for i in cur.fetchall():
    print(i)
