"""
أمثلة عملية على استخدام القواميس في Python
"""

def example_1_word_counter():
    """
    مثال 1: عداد الكلمات في نص
    """
    text = """
    Python لغة برمجة رائعة وسهلة التعلم
    Python تستخدم في مجالات متعددة
    لغة Python من أفضل لغات البرمجة
    """
    
    # تنظيف النص وتقسيمه إلى كلمات
    words = text.lower().replace('\n', ' ').split()
    
    # عد تكرار كل كلمة
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    # عرض النتائج
    print("تكرار الكلمات:")
    for word, count in sorted(word_count.items()):
        print(f"'{word}': {count} مرات")

def example_2_student_database():
    """
    مثال 2: قاعدة بيانات الطلاب
    """
    students = {
        "A101": {
            "name": "أحمد",
            "age": 20,
            "courses": ["رياضيات", "فيزياء", "برمجة"],
            "grades": {"��ياضيات": 90, "فيزياء": 85, "برمجة": 95}
        },
        "A102": {
            "name": "سارة",
            "age": 19,
            "courses": ["كيمياء", "أحياء", "برمجة"],
            "grades": {"كيمياء": 88, "أحياء": 92, "برمجة": 90}
        }
    }
    
    def get_student_average(student_id):
        """حساب متوسط درجات الطالب"""
        grades = students[student_id]["grades"].values()
        return sum(grades) / len(grades)
    
    # عرض معلومات الطلاب
    for student_id, info in students.items():
        print(f"\nمعلومات الطالب {student_id}:")
        print(f"الاسم: {info['name']}")
        print(f"العمر: {info['age']}")
        print(f"المواد: {', '.join(info['courses'])}")
        print(f"المتوسط: {get_student_average(student_id):.2f}")

def example_3_menu_ordering():
    """
    مثال 3: نظام طلب الطعام
    """
    menu = {
        "برجر": 50,
        "بيتزا": 75,
        "سلطة": 25,
        "عصير": 15
    }
    
    def calculate_order(items):
        """حساب تكلفة الطلب"""
        total = sum(menu[item] * quantity for item, quantity in items.items())
        return total
    
    # تجربة نظام الطلب
    order = {
        "برجر": 2,
        "بيتزا": 1,
        "عصير": 3
    }
    
    print("\nتفاصيل الطلب:")
    for item, quantity in order.items():
        price = menu[item] * quantity
        print(f"{item}: {quantity} × {menu[item]} = {price} ريال")
    
    total = calculate_order(order)
    print(f"المجموع الكلي: {total} ريال")

if __name__ == "__main__":
    print("=== مثال 1: عداد الكلمات ===")
    example_1_word_counter()
    
    print("\n=== مثال 2: قاعدة بيانات الطلاب ===")
    example_2_student_database()
    
    print("\n=== مثال 3: نظام طلب الطعام ===")
    example_3_menu_ordering() 