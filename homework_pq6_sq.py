import psycopg2

conn = psycopg2.connect(dbname='new_db', user='postgres', password='R29062011Z', host='localhost')
cursor = conn.cursor()
cursor.execute("""
SELECT * FROM public.books
ORDER BY id ASC, title ASC, author ASC, price ASC, "pageCounts" ASC 
""")
records = cursor.fetchall()
print(records)
print(type(records))

...
cursor.close()
conn.close()



