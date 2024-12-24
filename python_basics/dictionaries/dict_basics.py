"""
شرح أساسيات القواميس (Dictionaries) في Python
"""

# إنشاء القواميس
empty_dict = {}  # قاموس فارغ
person = {
    "name": "أحمد",
    "age": 25,
    "city": "القاهرة"
}  # قاموس بمعلومات شخص

# الوصول إلى العناصر
name = person["name"]  # الوصول المباشر
age = person.get("age")  # الوصول باستخدام get
city = person.get("address", "غير محدد")  # قيمة افتراضية إذا لم يوجد المفتاح

# تعديل وإضافة عناصر
person["email"] = "ahmed@example.com"  # إضافة عنصر جديد
person["age"] = 26  # تعديل قيمة موجودة

# حذف عناصر
removed_email = person.pop("email")  # حذف وإرجاع قيمة
del person["age"]  # حذف مباشر

# العمليات الأساسية
keys = person.keys()  # الحصول على المفاتيح
values = person.values()  # الحصول على القيم
items = person.items()  # الحصول على الأزواج (المفتاح، القيمة)

if __name__ == "__main__":
    print(f"القاموس الفارغ: {empty_dict}")
    print(f"معلومات الشخص: {person}")
    print(f"الاسم: {name}")
    print(f"العمر: {age}")
    print(f"العنوان: {city}")
    print(f"المفاتيح: {list(keys)}")
    print(f"القيم: {list(values)}")
    print(f"العناصر: {list(items)}") 