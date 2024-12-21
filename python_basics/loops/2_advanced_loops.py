# الدرس الثاني: الحلقات المتقدمة في بايثون
"""
تقنيات متقدمة في استخدام الحلقات وأنماط شائعة في البرمجة
"""

# 1. List Comprehension
print("=== List Comprehension ===")
# إنشاء قائمة بمربعات الأرقام
squares = [x**2 for x in range(1, 6)]
print(f"مربعات الأرقام: {squares}")

# مع شرط
even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
print(f"مربعات الأرقام الزوجية: {even_squares}")

# 2. Dictionary Comprehension
print("\n=== Dictionary Comprehension ===")
names = ["أحمد", "محمد", "علي"]
name_lengths = {name: len(name) for name in names}
print(f"أطوال الأسماء: {name_lengths}")

# 3. Generator Expression
print("\n=== Generator Expression ===")
def sum_of_squares(n):
    """حساب مجموع مربعات الأرقام باستخدام generator"""
    return sum(x**2 for x in range(1, n+1))

print(f"مجموع مربعات الأرقام حتى 5: {sum_of_squares(5)}")

# 4. استخدام zip
print("\n=== استخدام zip ===")
names = ["أحمد", "محمد", "علي"]
ages = [25, 30, 35]
cities = ["الرياض", "جدة", "الدمام"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} عمره {age} ويسكن في {city}")

# 5. التكرار على عدة قوائم في نفس الوقت
print("\n=== التكرار المتزامن ===")
from itertools import chain
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for item in chain(*lists):
    print(item)

# 6. استخدام itertools
print("\n=== استخدام itertools ===")
from itertools import combinations, permutations

# التوافيق
items = ['A', 'B', 'C']
print("التوافيق:")
for combo in combinations(items, 2):
    print(combo)

# التباديل
print("\nالتباديل:")
for perm in permutations(items, 2):
    print(perm)

# 7. حلقات مع معالجة الاستثناءات
print("\n=== حلقات مع معالجة الأخطاء ===")
def safe_divide(numbers, divisors):
    """قسمة آمنة مع معالجة الأخطاء"""
    results = []
    for n, d in zip(numbers, divisors):
        try:
            result = n / d
            results.append(result)
        except ZeroDivisionError:
            results.append("لا يمكن القسمة على صفر")
    return results

numbers = [10, 20, 30]
divisors = [2, 0, 5]
print(safe_divide(numbers, divisors))

# 8. تطبيقات عملية

# مثال 1: تحليل النص
print("\n=== تحليل النص ===")
def analyze_text(text):
    """تحليل النص وإحصاء الكلمات"""
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

text = "مرحبا مرحبا أهلا أهلا وسهلا"
print(analyze_text(text))

# مثال 2: معالجة البيانات المتداخلة
print("\n=== معالجة البيانات المتداخلة ===")
def process_nested_data(data):
    """معالجة البيانات المتداخلة"""
    total = 0
    for row in data:
        for num in row:
            if isinstance(num, (int, float)):
                total += num
    return total

nested_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"مجموع الأرقام: {process_nested_data(nested_data)}") 