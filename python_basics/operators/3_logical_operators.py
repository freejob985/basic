# الدرس الثالث: العمليات المنطقية في بايثون
"""
العمليات المنطقية تستخدم للربط بين الشروط المنطقية
وتشمل: and (و), or (أو), not (ليس)
"""

# 1. العملية المنطقية AND (و)
x = 5
y = 10

# يجب تحقق الشرطين معاً للحصول على True
is_between = x > 0 and x < y
print(f"هل {x} بين 0 و {y}؟ {is_between}")  # سيطبع: True

# مثال آخر على AND
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"هل يمكنه القيادة؟ {can_drive}")  # سيطبع: True

# 2. العملية المنطقية OR (أو)
# يكفي تحقق شرط واحد للحصول على True
is_holiday = False
is_weekend = True
can_rest = is_holiday or is_weekend
print(f"هل يمكن الراحة؟ {can_rest}")  # سيطبع: True

# مثال آخر على OR
payment_method = "بطاقة"
can_buy = payment_method == "بطاقة" or payment_method == "نقداً"
print(f"هل يمكن الشراء؟ {can_buy}")  # سيطبع: True

# 3. العملية المنطقية NOT (ليس)
# تعكس القيمة المنطقية
is_busy = True
is_free = not is_busy
print(f"هل هو متفرغ؟ {is_free}")  # سيطبع: False

# مثال آخر على NOT
number = 7
is_not_even = not (number % 2 == 0)
print(f"هل {number} ليس زوجياً؟ {is_not_even}")  # سيطبع: True

# 4. دمج العمليات المنطقية
age = 20
has_degree = True
has_experience = False

# استخدام عدة عمليات منطقية معاً
can_apply = (age >= 18 and has_degree) or has_experience
print(f"هل يمكنه التقدم للوظيفة؟ {can_apply}")  # سيطبع: True

# 5. أولويات العمليات المنطقية
# NOT له الأولوية الأعلى، ثم AND، ثم OR
result = True or True and False  # يساوي: True or (True and False)
print(f"نتيجة True or True and False: {result}")  # سيطبع: True

# استخدام الأقواس لتغيير الأولوية
result_with_parentheses = (True or True) and False
print(f"نتيجة (True or True) and False: {result_with_parentheses}")  # سيطبع: False

# 6. التقييم المختصر (Short-circuit Evaluation)
def expensive_operation():
    """دالة تمثل عملية معقدة"""
    print("تنفيذ عملية معقدة...")
    return True

# في حالة OR، إذا كان الشرط الأول True، لن يتم تنفيذ الشرط الثاني
result = True or expensive_operation()  # لن يتم تنفيذ expensive_operation

# في حالة AND، إذا كان الشرط الأول False، لن يتم تنفيذ الشرط الثاني
result = False and expensive_operation()  # لن يتم تنفيذ expensive_operation

# 7. تطبيقات عملية
# التحقق من صحة المدخلات
username = "ahmed"
password = "123456"

is_valid_username = len(username) >= 3 and username.isalnum()
is_valid_password = len(password) >= 6 and not password.isspace()

can_login = is_valid_username and is_valid_password
print(f"هل يمكن تسجيل الدخول؟ {can_login}") 