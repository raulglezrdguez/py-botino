import sqlite3
import datetime

# create connection
conn = sqlite3.connect('./dbs/logs.db')
# create cursor
c = conn.cursor()

# # **************** First
# # Create table logs
# c.execute('''CREATE TABLE logs
#              (original TEXT, 
#              answer TEXT, 
#              created_at timestamp)''')
# conn.close()

# # **************** Second
# c.execute("INSERT INTO logs VALUES ('probando','respuesta', '{}')".format(datetime.datetime.now()))
# # Save (commit) the changes
# conn.commit()
# conn.close()

# # ****************** testing
# select = "SELECT * FROM logs"
# rows = c.execute(select)
# for row in rows:
#     original = row[0]
#     answer = row[1]
#     dt = row[2]
#     print(original, answer, dt)

# # select = 'SELECT COUNT(*) as cantidad FROM logs'
# # rows = c.execute(select)
# # for row in rows:
# #     print(f'cantidad: {row[0]}')

# # close connection
# conn.close()

f = open("./logs/all-logs.csv", "w", encoding="utf-8")

select = "SELECT * FROM logs order by created_at ASC"
rows = c.execute(select)
for row in rows:
    t = row[0]
    r = row[1]
    d = row[2]
    f.write("{}|{}|{}\n".format(t, r, d))

# close connection
conn.close()

f.close()



















# # **************** Second
# f = open("./martires/all.data", "r", encoding="utf-8")
# for x in f:
#     # print(x)
#     datas = x.split('->')
#     if (len(datas) == 2):
#         # busco que no exista el registro
#         rows = c.execute("SELECT name FROM martires WHERE name = '{}'".format(datas[0]))
#         count = len(rows.fetchall())
#         if count == 0:
#             # Insert a row of data
#             print(datas[0])
#             c.execute("INSERT INTO martires VALUES ('{}','{}')".format(datas[0], datas[1].rstrip()))

# # Save (commit) the changes
# conn.commit()

# # close connection
# conn.close()

# print("done")

# ****************** Testing
# select = "SELECT * FROM martires WHERE number='{}' AND title={}".format(27, 'probando')
# select = "SELECT * FROM martires WHERE number='{}'".format(27)
# select = "SELECT * FROM martires WHERE author like '%{}%' order by number DESC".format('bernard')
# select = "SELECT name FROM martires WHERE name like '%{}%' order by name DESC limit 5".format('raúl')
# select = "SELECT * FROM martires WHERE name like '%{}%' order by name DESC".format('fidel castro')
# rows = c.execute(select)
# for row in rows:
#     name = row[0]
#     # print(name)
#     bio = row[1]
#     print(name,':', bio)

# select = 'SELECT COUNT(*) as cantidad FROM martires'
# rows = c.execute(select)
# for row in rows:
#     print(f'cantidad: {row[0]}')
# # close connection
# conn.close()

# #  create all-good.data

# f = open("./martires/all-good.data", "w", encoding="utf-8")

# select = "SELECT name, biography FROM martires order by name ASC"
# rows = c.execute(select)
# for row in rows:
#     name = row[0]
#     bio = row[1]
#     f.write("{}->{}\n".format(name, bio))

# # close connection
# conn.close()

# f.close()