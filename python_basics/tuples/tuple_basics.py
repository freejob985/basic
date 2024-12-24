"""
شرح أساسيات المتتاليات الثابتة (Tuples) في Python
"""

# إنشاء المتتاليات الثابتة
empty_tuple = ()  # متتالية فارغة
numbers = (1, 2, 3, 4, 5)  # متتالية أرقام
mixed_tuple = (1, "نص", 3.14, True)  # متتالية متنوعة
nested_tuple = (1, (2, 3), (4, 5, 6))  # متتالية متداخلة
single_item = (1,)  # متتالية بعنصر واحد (لاحظ الفاصلة)

# الوصول إلى العناصر
first_item = numbers[0]  # العنصر الأول
last_item = numbers[-1]  # العنصر الأخير
sub_tuple = numbers[1:4]  # جزء من المتتالية

# العمليات الأساسية
tuple_length = len(numbers)  # طول المتتالية
combined = numbers + (6, 7, 8)  # دمج متتاليتين
repeated = (1, 2) * 3  # تكرار المتتالية

# البحث في المتتالية
contains_5 = 5 in numbers  # التحقق من وجود عنصر
index_of_5 = numbers.index(5)  # موقع العنصر

if __name__ == "__main__":
    print(f"المتتالية الفارغة: {empty_tuple}")
    print(f"متتالية الأرقام: {numbers}")
    print(f"المتتالية المتنوعة: {mixed_tuple}")
    print(f"المتتالية المتداخلة: {nested_tuple}")
    print(f"متتالية بعنصر واحد: {single_item}")
    print(f"العنصر الأول: {first_item}")
    print(f"العنصر الأخير: {last_item}")
    print(f"جزء من المتتالية: {sub_tuple}")
    print(f"طول المتتالية: {tuple_length}")
    print(f"المتتالية المدموجة: {combined}")
    print(f"المتتالية المكررة: {repeated}")
    print(f"هل يوجد الرقم 5؟ {contains_5}")
    print(f"موقع الرقم 5: {index_of_5}") 