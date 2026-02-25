import sqlite3
import logging

logging.basicConfig(
    filename= "log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Book:
    def __init__(self,title,author,year):
        if title == "":
            raise ValueError("Назва не може бути порожня")
        if author == "":
            raise ValueError("Автор не може бути порожній")
        if year < 0:
            raise ValueError("Рік введено не правильно ")
        self.title = title
        self.author = author
        self.year = year

def create_base():
    connection = sqlite3.connect("BookMarket.sl3", timeout=15)
    cur = connection.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Books (
    title TEXT,
    author TEXT,
    year INTEGER
    )
    """)
    connection.commit()

def add_book(book):
    connection = sqlite3.connect("BookMarket.sl3", timeout=15)
    cur = connection.cursor()
    cur.execute(" INSERT INTO books(title,author,year)VALUES(?,?,?)",(book.title,book.author,book.year))
    connection.commit()

    connection.close()


try:
    t = input("Введіть назву книги:")
    a = input("Введіть автора книги:")
    y = int(input("Введіть рік видання книги:"))
    b = Book(t,a,y)

    create_base()

    print("Книгу додано")

except ValueError as e:
    print("Помилка:",e)