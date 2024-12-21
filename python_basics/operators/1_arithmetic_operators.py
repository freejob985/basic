# الدرس الأول: العمليات الحسابية في بايثون
"""
العمليات الحسابية هي العمليات الأساسية التي يمكن إجراؤها على الأرقام
مثل الجمع والطرح والضرب والقسمة
"""

# 1. عمليات الجمع والطرح
num1 = 10
num2 = 5

# عملية الجمع (+)
addition = num1 + num2
print(f"الجمع: {num1} + {num2} = {addition}")  # سيطبع: الجمع: 10 + 5 = 15

# عملية الطرح (-)
subtraction = num1 - num2
print(f"الطرح: {num1} - {num2} = {subtraction}")  # سيطبع: الطرح: 10 - 5 = 5

# 2. عمليات الضرب والقسمة
# عملية الضرب (*)
multiplication = num1 * num2
print(f"الضرب: {num1} × {num2} = {multiplication}")  # سيطبع: الضرب: 10 × 5 = 50

# عملية القسمة (/)
division = num1 / num2
print(f"القسمة: {num1} ÷ {num2} = {division}")  # سيطبع: القسمة: 10 ÷ 5 = 2.0

# القسمة الصحيحة (//)
integer_division = num1 // num2
print(f"القسمة الصحيحة: {num1} // {num2} = {integer_division}")  # سيطب��: 2

# 3. عمليات متقدمة
# باقي القسمة (%)
remainder = num1 % num2
print(f"باقي القسمة: {num1} % {num2} = {remainder}")  # سيطبع: 0

# الأس (**)
power = num1 ** 2  # تربيع العدد
print(f"تربيع {num1} = {power}")  # سيطبع: تربيع 10 = 100

# 4. العمليات المركبة
x = 5
print(f"قيمة x الأولية: {x}")

# الزيادة بمقدار معين
x += 3  # نفس x = x + 3
print(f"بعد x += 3: {x}")  # سيطبع: 8

# النقص بمقدار معين
x -= 2  # نفس x = x - 2
print(f"بعد x -= 2: {x}")  # سيطبع: 6

# الضرب بمقدار معين
x *= 2  # نفس x = x * 2
print(f"بعد x *= 2: {x}")  # سيطبع: 12

# 5. أولويات العمليات الحسابية
result = 10 + 5 * 2
print(f"10 + 5 * 2 = {result}")  # سيطبع: 20 (الضرب قبل الجمع)

result_with_parentheses = (10 + 5) * 2
print(f"(10 + 5) * 2 = {result_with_parentheses}")  # سيطبع: 30

# 6. التعامل مع الأعداد العشرية
decimal1 = 3.14
decimal2 = 2.0

# الجمع
print(f"{decimal1} + {decimal2} = {decimal1 + decimal2}")

# الضرب
print(f"{decimal1} × {decimal2} = {decimal1 * decimal2}")

# تقريب النتائج
result = decimal1 / decimal2
print(f"القسمة بدون تقر��ب: {result}")
print(f"القسمة مع تقريب لرقمين عشريين: {round(result, 2)}") 