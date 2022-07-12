import psycopg2

# CRUD

# Read - чтение(сортировка и фильтрация) из базы и запись в эксель файл
# Create - вставка новых данных (из эксель файл)
# Delete - удаление строк по условиям
# Update - обновление из базы и запись в эксель файл

# READ (SELECT)
############################################################################

# Connect to your postgres DB
conn = psycopg2.connect("dbname=postgres user=public.example password=R29062011Z")

# Open a cursor to perform database operations
cur = conn.cursor()


