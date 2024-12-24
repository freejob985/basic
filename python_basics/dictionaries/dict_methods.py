"""
شرح الدوال المتاحة للقواميس في Python
"""

# قاموس للتجربة
student = {
    "name": "سارة",
    "age": 20,
    "grades": {"math": 90, "science": 85, "language": 95}
}

# دوال الوصول والتعديل
student.update({"email": "sara@example.com", "phone": "123456"})  # تحديث/إضافة عدة عناصر
default_grade = student.get("history", 0)  # الحصول على قيمة مع قيمة افتراضية
student.setdefault("address", "القاهرة")  # تعيين قيمة افتراضية إذا لم يوجد المفتاح

# دوال الحذف
student.pop("phone")  # حذف عنصر وإرجاع قيمته
student.popitem()  # حذف وإرجاع آخر عنصر تم إضافته
student_copy = student.copy()  # نسخ ضحلة للقاموس
student_deep = __import__('copy').deepcopy(student)  # نسخ عميقة للقاموس
student.clear()  # حذف كل العناصر

# إنشاء قاموس من قوائم
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict_from_lists = dict(zip(keys, values))

# دمج قواميس (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}

if __name__ == "__main__":
    print(f"القاموس الأصلي: {student}")
    print(f"القيمة الافتراضية: {default_grade}")
    print(f"نسخة من القاموس: {student_copy}")
    print(f"قاموس من قوائم: {dict_from_lists}")
    print(f"دمج قواميس: {merged}") 