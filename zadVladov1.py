from datetime import datetime

class Person:
    def __init__(self, name, egn, birth_date):
        self.name = name
        self.egn = egn
        self.birth_date = birth_date

    def display_info(self):
        print(f"Име: {self.name}, ЕГН: {self.egn}, Дата на раждане: {self.birth_date}")

class Book:
    def __init__(self, title, author, year, genres):
        self.title = title
        self.author = author
        self.year = year
        self.genres = genres

    def display_info(self):
        print(f"Заглавие: {self.title}, Автор: {self.author}, Година: {self.year}, Жанрове: {', '.join(self.genres)}")

class Student:
    def __init__(self, student_id, name, average_grade):
        self.student_id = student_id
        self.name = name
        self.average_grade = average_grade

    def display_info(self):
        print(f"Ученически номер: {self.student_id}, Име: {self.name}, Среден успех: {self.average_grade:.2f}")

people = [
    Person("Иван Желязков", "9001011234", "1990-01-01"),
    Person("Йово Михов", "8503055678", "1985-03-05"),
    Person("Бобо Янев", "9207123456", "1992-07-12"),
    Person("Валери Бозанска", "8809236789", "1988-09-23"),
    Person("Кристян Краджов", "9504159876", "1995-04-15")
]

books = [
    Book("Под игото", "Иван Вазов", 1894, ["Исторически", "Роман", "Скучен"]),
    Book("Гордост и предразсъдъци", "Джейн Остин", 1813, ["Романтика", "Класика"]),
    Book("Пипи Дългото чорапче", "Астрид Линдгрен", 1968, ["Приключения", "Комедия"]),
    Book("Хари Потър и философският камък", "Дж. К. Роулинг", 1997, ["Фентъзи", "Приключения"]),
    Book("Властелинът на пръстените", "Дж. Р. Р. Толкин", 1954, ["Фентъзи", "Приключения"])
]

students = [
    Student(101, "Валери Бозанска", 4.20),
    Student(102, "Йово Михов", 6.00),
    Student(103, "Иван Желязков", 2.86),
    Student(104, "Бобо Янев", 5.74),
    Student(105, "Кристян Краджов", 3.94)
]

print("\n------------- Хора -------------")
for person in people:
    person.display_info()

print("\n------------- Книги -------------")
for book in books:
    book.display_info()

print("\n------------- Ученици -------------")
for student in students:
    student.display_info()
