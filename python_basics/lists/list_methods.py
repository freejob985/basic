"""
شرح الدوال المتاحة للقوائم في Python
"""

# قائمة للتجربة
numbers = [1, 3, 2, 5, 4, 3]

# دوال الإضافة والحذف
numbers.append(6)  # إضافة عنصر في النهاية
numbers.insert(0, 0)  # إضافة عنصر في موقع محدد
numbers.extend([7, 8])  # إضافة عناصر من قائمة أخرى
popped = numbers.pop()  # حذف وإرجاع آخر عنصر
numbers.remove(3)  # حذف أول ظهور للقيمة
numbers.clear()  # حذف كل العناصر

# دوال الترتيب
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers.sort()  # ترتيب تصاعدي
numbers.sort(reverse=True)  # ترتيب تنازلي
numbers.reverse()  # عكس ترتيب العناصر

# دوال البحث والعد
count_of_5 = numbers.count(5)  # عد تكرار قيمة
index_of_5 = numbers.index(5)  # موقع أول ظهور للقيمة

# نسخ القائمة
shallow_copy = numbers.copy()  # نسخة سطحية

if __name__ == "__main__":
    print(f"القائمة الأصلية: {numbers}")
    print(f"عدد تكرار الرقم 5: {count_of_5}")
    print(f"موقع الرقم 5: {index_of_5}")
    print(f"نسخة من القائمة: {shallow_copy}") 