# الدرس الأول: الحلقات الأساسية في بايثون
"""
الحلقات تسمح بتكرار تنفيذ مجموعة من الأوامر
نستخدم for و while للتحكم في التكرار
"""

# 1. حلقة for مع القوائم
print("=== التكرار على القوائم ===")
fruits = ["تفاح", "موز", "برتقال"]

for fruit in fruits:
    print(f"الفاكهة: {fruit}")

# 2. حلقة for مع range
print("\n=== التكرار باستخدام range ===")
# طباعة الأرقام من 1 إلى 5
for i in range(1, 6):
    print(f"الرقم: {i}")

# 3. حلقة while البسيطة
print("\n=== حلقة while البسيطة ===")
counter = 0
while counter < 5:
    print(f"العداد: {counter}")
    counter += 1

# 4. حلقة for مع enumerate
print("\n=== استخدام enumerate ===")
colors = ["أحمر", "أخضر", "أزرق"]
for index, color in enumerate(colors):
    print(f"اللون رقم {index + 1}: {color}")

# 5. حلقة for مع القواميس
print("\n=== التكرار على القواميس ===")
person = {
    "name": "أحمد",
    "age": 25,
    "city": "الرياض"
}

# التكرار على المفاتيح والقيم
for key, value in person.items():
    print(f"{key}: {value}")

# 6. استخدام break
print("\n=== استخدام break ===")
for i in range(1, 11):
    if i == 6:
        print("وصلنا إلى 6، سنتوقف هنا")
        break
    print(f"الرقم: {i}")

# 7. استخدام continue
print("\n=== استخدام continue ===")
for i in range(1, 6):
    if i == 3:
        print("سنتخطى الرقم 3")
        continue
    print(f"الرقم: {i}")

# 8. حلقات متداخلة
print("\n=== الحلقات المتداخلة ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# 9. حلقة while مع else
print("\n=== while مع else ===")
count = 0
while count < 3:
    print(f"العداد: {count}")
    count += 1
else:
    print("انتهت الحلقة بنجاح")

# 10. أمثلة عملية

# مثال 1: حساب مجموع الأرقام
print("\n=== حساب مجموع الأرقام ===")
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"مجموع الأرقام: {total}")

# مثال 2: البحث عن عنصر
print("\n=== البحث عن ع��صر ===")
def find_item(items, target):
    """البحث عن عنصر في قائمة"""
    for index, item in enumerate(items):
        if item == target:
            return f"العنصر موجود في الموقع {index}"
    return "العنصر غير موجود"

items = ["قلم", "كتاب", "مسطرة"]
print(find_item(items, "كتاب"))
print(find_item(items, "حاسبة"))

# مثال 3: طباعة جدول الضرب
print("\n=== جدول الضرب ===")
def print_multiplication_table(n):
    """طباعة جدول الضرب حتى الرقم n"""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} × {j} = {i * j}")
        print("-" * 15)

print_multiplication_table(3) 