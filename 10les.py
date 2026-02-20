import sqlite3

connection = sqlite3.connect("AnimalKingdom.sl3", timeout=15)
cur = connection.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Animals (
    ID INTEGER,
    name TEXT,
    type TEXT
)
""")
connection.commit()

cur.execute("""
INSERT INTO Animals (ID, name, type) VALUES
(1, 'Лев', 'Ссавець'),
(2, 'Крокодил', 'Плазун'),
(3, 'Орел', 'Птах'),
(4, 'Морська черепаха', 'Плазун'),
(5, 'Мавпа', 'Ссавець')
""")
connection.commit()

cur.execute("""
UPDATE Animals
SET name = 'Сокіл'
WHERE name = 'Орел'
""")
connection.commit()

cur.execute("SELECT * FROM Animals WHERE type = 'Ссавець'")
result = cur.fetchall()
print("Ссавці:", result)

cur.execute("SELECT * FROM Animals")
result = cur.fetchall()
print("Всі звірі:", result)

connection.close()