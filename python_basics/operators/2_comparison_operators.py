# الدرس الثاني: عمليات المقارنة في بايثون
"""
عمليات المقارنة تستخدم لمقارنة القيم وتعيد قيمة منطقية (True/False)
هذه العمليات أساسية في كتابة الشروط والحلقات
"""

# 1. عمليات المساواة وعدم المساواة
x = 10
y = 5

# المساواة (==)
is_equal = x == y
print(f"هل {x} يساوي {y}؟ {is_equal}")  # سيطبع: False

# عدم المساواة (!=)
is_not_equal = x != y
print(f"هل {x} لا يساوي {y}؟ {is_not_equal}")  # سيطبع: True

# 2. عمليات المقارنة
# أكبر من (>)
is_greater = x > y
print(f"هل {x} أكبر من {y}؟ {is_greater}")  # سيطبع: True

# أصغر من (<)
is_less = x < y
print(f"هل {x} أصغر من {y}؟ {is_less}")  # سيطبع: False

# أكبر من أو يساوي (>=)
is_greater_or_equal = x >= y
print(f"هل {x} أكبر من أو يساوي {y}؟ {is_greater_or_equal}")  # سيطبع: True

# أصغر من أو يساوي (<=)
is_less_or_equal = x <= y
print(f"هل {x} أصغر من أو يساوي {y}؟ {is_less_or_equal}")  # سيطبع: False

# 3. مقارنة السلاسل النصية
str1 = "أحمد"
str2 = "محمد"

# مقارنة نصية
print(f"هل {str1} يساوي {str2}؟ {str1 == str2}")
print(f"هل {str1} أصغر من {str2}؟ {str1 < str2}")  # يقارن حسب الترتيب الأبجدي

# 4. مقارنة القيم المنطقية
bool1 = True
bool2 = False

print(f"هل {bool1} يساوي {bool2}؟ {bool1 == bool2}")
print(f"هل {bool1} لا يساوي {bool2}؟ {bool1 != bool2}")

# 5. مقارنات متعددة
a = 5
b = 5
c = 10

# يمكن استخدام عمليات المقارنة المتسلسلة
is_between = a <= b <= c
print(f"هل {b} بين {a} و {c}؟ {is_between}")  # سيطبع: True

# 6. مقارنة الهوية (is و is not)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# مقارنة القيم
print(f"هل القيم متساوية؟ {list1 == list2}")  # True

# مقارنة الهوية
print(f"هل هما نفس الكائن؟ {list1 is list2}")  # False
print(f"هل list1 و list3 نفس الكائن؟ {list1 is list3}")  # True

# 7. التحقق من العضوية (in و not in)
numbers = [1, 2, 3, 4, 5]
value = 3

# التحقق من وجود قيمة في قائمة
is_present = value in numbers
print(f"هل {value} موجود في {numbers}؟ {is_present}")  # True

# التحقق من عدم وجود قيمة
is_not_present = 6 not in numbers
print(f"هل 6 غير موجود في {numbers}؟ {is_not_present}")  # True 