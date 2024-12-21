# الدرس الأول: المتغيرات الأساسية في بايثون

"""
المتغيرات هي أماكن لتخزين البيانات في الذاكرة
كل متغير له اسم وقيمة ونوع
"""

# 1. المتغيرات العددية (Numeric Variables)
# تعريف متغير صحيح (integer)
age = 25
print(f"العمر: {age}")  # سيطبع: العمر: 25
print(f"نوع المتغير age: {type(age)}")  # سيطبع: <class 'int'>

# تعريف متغير عشري (float)
height = 175.5
print(f"الطول: {height} سم")  # سيطبع: الطول: 175.5 سم
print(f"نوع المتغير height: {type(height)}")  # سيطبع: <class 'float'>

# 2. المتغيرات النصية (String Variables)
# تعريف متغير نصي
name = "أحمد"
print(f"الاسم: {name}")  # سيطبع: الاسم: أحمد
print(f"نوع المتغير name: {type(name)}")  # سيطبع: <class 'str'>

# يمكن استخدام علامات تنصيص مفردة أو مزدوجة
message = 'مرحباً بك'
print(message)  # سيطبع: مرحباً بك

# 3. المتغيرات المنطقية (Boolean Variables)
# تعريف متغير منطقي
is_student = True
print(f"هل أنت طالب؟ {is_student}")  # سيطبع: هل أنت طالب؟ True
print(f"نوع المتغير is_student: {type(is_student)}")  # سيطبع: <class 'bool'>

# 4. المتغيرات المركبة (Complex Variables)
# تعريف قائمة (List)
fruits = ["تفاح", "موز", "برتقال"]
print(f"الفواكه: {fruits}")  # سيطبع: الفواكه: ['تفاح', 'موز', 'برتقال']
print(f"نوع المتغير fruits: {type(fruits)}")  # سيطبع: <class 'list'>

# تعريف قاموس (Dictionary)
person = {
    "name": "محمد",
    "age": 30,
    "city": "الرياض"
}
print(f"معلومات الشخص: {person}")
print(f"نوع المتغير person: {type(person)}")  # سيطبع: <class 'dict'>

# 5. تغيير قيم المتغيرات
x = 10
print(f"قيمة x الأولية: {x}")
x = 20  # تغيير قيمة المتغير
print(f"قيمة x بعد التغيير: {x}")

# 6. الثوابت (Constants)
# في بايثون، نستخدم الأحرف الكبيرة للدلالة على الثوابت (اصطلاحاً)
PI = 3.14159
MAX_STUDENTS = 30
print(f"قيمة باي: {PI}")
print(f"الحد الأقصى للطلاب: {MAX_STUDENTS}") 