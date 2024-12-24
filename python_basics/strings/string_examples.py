"""
أمثلة عملية على استخدام السلاسل النصية في Python
"""

def example_1_password_validation():
    """
    مثال 1: التحقق من صحة كلمة المرور
    """
    password = "Python123!"
    
    # التحقق من طول كلمة المرور
    is_length_valid = len(password) >= 8
    # التحقق من وجود أرقام
    has_number = any(char.isdigit() for char in password)
    # التحقق من وجود أحرف كبيرة
    has_upper = any(char.isupper() for char in password)
    # التحقق من وجود رموز خاصة
    special_chars = "!@#$%^&*"
    has_special = any(char in special_chars for char in password)
    
    print("نتائج فحص كلمة المرور:")
    print(f"الطول كافي: {is_length_valid}")
    print(f"تحتوي على رقم: {has_number}")
    print(f"تحتوي على حرف كبير: {has_upper}")
    print(f"تحتوي على رمز خاص: {has_special}")

def example_2_text_analysis():
    """
    مثال 2: تحليل النص
    """
    text = """
    يعد Python من أفضل لغات البرمجة
    حيث يتميز بسهولة التعلم والاستخدام
    ويستخدم في مجالات متعددة
    """
    
    # عدد الكلمات
    words = text.split()
    word_count = len(words)
    
    # عدد الأسطر
    lines = text.strip().split('\n')
    line_count = len(lines)
    
    # عدد الأحرف (بدون المسافات)
    char_count = len(text.replace(" ", "").replace("\n", ""))
    
    print("تحليل النص:")
    print(f"عدد الكلمات: {word_count}")
    print(f"عدد الأسطر: {line_count}")
    print(f"عدد الأحرف: {char_count}")

def example_3_text_formatting():
    """
    مثال 3: تنسيق النص
    """
    name = "أحمد"
    age = 25
    city = "القاهرة"
    
    # استخدام f-strings
    info_1 = f"اسمي {name}، عمري {age} سنة، وأسكن في {city}"
    
    # استخدام format
    info_2 = "اسمي {0}، عمري {1} سنة، وأسكن في {2}".format(name, age, city)
    
    # استخدام %
    info_3 = "اسمي %s، عمري %d سنة، وأسكن في %s" % (name, age, city)
    
    print("طرق مختلفة لتنسيق النص:")
    print(f"1. باستخدام f-strings:\n   {info_1}")
    print(f"2. باستخدام format:\n   {info_2}")
    print(f"3. باستخدام %:\n   {info_3}")

if __name__ == "__main__":
    print("=== مثال 1: التحقق من كلمة المرور ===")
    example_1_password_validation()
    print("\n=== مثال 2: تحليل النص ===")
    example_2_text_analysis()
    print("\n=== مثال 3: تنسيق النص ===")
    example_3_text_formatting() 