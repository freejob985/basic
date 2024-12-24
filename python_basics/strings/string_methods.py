"""
شرح الدوال المتاحة للسلاسل النصية في Python
"""

# سلسلة نصية للتجربة
text = "مرحباً بالعالم العربي"

# دوال تغيير حالة الأحرف
upper_case = text.upper()  # تحويل إلى أحرف كبيرة
lower_case = text.lower()  # تحويل إلى أحرف صغيرة
title_case = text.title()  # تحويل أول حرف من كل كلمة إلى كبير

# دوال البحث والاستبدال
replaced = text.replace("العربي", "الجميل")  # استبدال نص
position = text.find("العالم")  # البحث عن موقع نص
count = text.count("ا")  # عد تكرار حرف أو نص

# دوال التنسيق
stripped = "   نص   ".strip()  # إزالة المسافات
split_text = text.split()  # تقسيم النص إلى قائمة
joined = " ".join(["مرحباً", "بالعالم"])  # دمج قائمة إلى نص

# أمثلة على الاستخدام
if __name__ == "__main__":
    print(f"النص الأصلي: {text}")
    print(f"الأحرف الكبيرة: {upper_case}")
    print(f"ا��أحرف الصغيرة: {lower_case}")
    print(f"حالة العنوان: {title_case}")
    print(f"النص المستبدل: {replaced}")
    print(f"موقع كلمة 'العالم': {position}")
    print(f"عدد تكرار حرف 'ا': {count}")
    print(f"النص بعد إزالة المسافات: {stripped}")
    print(f"النص المقسم: {split_text}")
    print(f"النص المدموج: {joined}") 