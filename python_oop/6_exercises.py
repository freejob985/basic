# تمارين وتطبيقات عملية

"""
هذا الملف يحتوي على تمارين وتطبيقات عملية للتدرب على المفاهيم السابقة
"""

# التمرين الأول: إنشاء نظام لإدارة المكتبة
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"تمت إضافة الكتاب: {book.title}")
    
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"تم استعارة الكتاب: {book.title}")
                    return
                else:
                    print("الكتاب غير متوفر حالياً")
                    return
        print("الكتاب غير موجود في المكتبة")
    
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"تم إرجاع الكتاب: {book.title}")
                    return
                else:
                    print("هذا الكتاب لم يتم استعارته")
                    return
        print("الكتاب غير موجود في المكتبة")

# التمرين الثاني: نظام لإدارة الموظفين
class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
    
    def get_salary(self):
        return self.salary
    
    def give_raise(self, amount):
        self.salary += amount
        print(f"تم زيادة راتب {self.name} بمقدار {amount}")

class Manager(Employee):
    def __init__(self, name, id, salary, department):
        super().__init__(name, id, salary)
        self.department = department
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"تم إضافة {employee.name} إلى قسم {self.department}")
    
    def list_employees(self):
        print(f"\nموظفو قسم {self.department}:")
        for emp in self.employees:
            print(f"- {emp.name} (الراتب: {emp.salary})")

def main():
    # تجربة نظام المكتبة
    print("=== نظام المكتبة ===")
    library = Library()
    book1 = Book("البرمجة بلغة بايثون", "أحمد محمد", "123456")
    book2 = Book("تعلم الخوارزميات", "سارة أحمد", "789012")
    
    library.add_book(book1)
    library.add_book(book2)
    library.borrow_book("123456")
    library.borrow_book("123456")
    library.return_book("123456")
    
    # تجربة نظام الموظفين
    print("\n=== نظام الموظفين ===")
    manager = Manager("محمد علي", "M001", 10000, "تطوير البرمجيات")
    emp1 = Employee("خالد أحمد", "E001", 5000)
    emp2 = Employee("فاطمة محمد", "E002", 5500)
    
    manager.add_employee(emp1)
    manager.add_employee(emp2)
    manager.list_employees()
    
    emp1.give_raise(500)
    manager.list_employees()

if __name__ == "__main__":
    main() 