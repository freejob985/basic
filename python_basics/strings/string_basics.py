"""
شرح أساسيات السلاسل النصية (Strings) في Python
"""

# إنشاء السلاسل النصية
simple_string = "مرحباً بالعالم"
single_quotes = 'مرحباً بالعالم'
multi_line = """هذا نص
متعدد الأسطر
يمكن كتابته بهذه الطريقة"""

# الوصول إلى الأحرف
first_char = simple_string[0]  # يحصل على الحرف الأول
last_char = simple_string[-1]  # يحصل على الحرف الأخير

# تقطيع السلسلة النصية (String Slicing)
part = simple_string[0:5]  # يأخذ الأحرف من 0 إلى 4
reverse = simple_string[::-1]  # يعكس السلسلة النصية

# عمليات أساسية
string_length = len(simple_string)  # طول السلسلة النصية
concatenated = "مرحباً" + " " + "بالعالم"  # دمج السلاسل النصية
repeated = "مرحباً" * 3  # تكرار السلسلة النصية

# أمثلة على الاستخدام
if __name__ == "__main__":
    print(f"السلسلة الأصلية: {simple_string}")
    print(f"الحرف الأول: {first_char}")
    print(f"الحرف الأخير: {last_char}")
    print(f"جزء من السلسلة: {part}")
    print(f"السلسلة معكوسة: {reverse}")
    print(f"طول السلسلة: {string_length}")
    print(f"دمج السلاسل: {concatenated}")
    print(f"تكرار السلسلة: {repeated}") 