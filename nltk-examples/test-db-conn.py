import psycopg2 # type: ignore

# PostgreSQL
# use_storage = False

# if use_storage:
#     # Connect to SQLite database (or create one)
#     conn = psycopg2.connect(database="test_db", user="admin", password="root", host="postgres_db", port=5432)

#     # Create a cursor object to execute SQL commands
#     cursor = conn.cursor()

#     # Create a table for storing scraped data
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS posts (
#         id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
#         url TEXT,
#         content TEXT
#     )
#     ''')

#     # Insert data into the table
#     tuples = []
#     for url, data in parsed_data.items():
#         for item in data:
#             t = (url, item)
#             tuples.append(t)

#     cursor.executemany('INSERT INTO posts (url, content) VALUES (%s, %s)', 
#                     tuples)

#     # Commit the transaction and close the connection
#     conn.commit()
#     conn.close()

conn = psycopg2.connect(database="test_db", user="admin", password="root", host="postgres_db", port=5432)
cursor = conn.cursor()
rows = cursor.execute('SELECT * FROM posts')
# for row in rows:
#     print(f'Id: {row[0]}')
#     print(f'Url: {row[1]}')
#     print(f'Content: {row[2]}')
#     print()
for row in cursor:
    print(row)

conn.close()