"""
شرح أساسيات القوائم (Lists) في Python
"""

# إنشاء القوائم
empty_list = []  # قائمة فارغة
numbers = [1, 2, 3, 4, 5]  # قائمة أرقام
mixed_list = [1, "نص", 3.14, True]  # قائمة متنوعة
nested_list = [1, [2, 3], [4, 5, 6]]  # قائمة متداخلة

# الوصول إلى العناصر
first_item = numbers[0]  # العنصر الأول
last_item = numbers[-1]  # العنصر الأخير
sub_list = numbers[1:4]  # جزء من القائمة

# تعديل القائمة
numbers[0] = 10  # تغيير قيمة عنصر
numbers.append(6)  # إضافة عنصر في النهاية
numbers.insert(0, 0)  # إضافة عنصر في موقع محدد

# العمليات الأساسية
list_length = len(numbers)  # طول القائمة
combined = numbers + [7, 8, 9]  # دمج قائمتين
repeated = [1, 2] * 3  # تكرار القائمة

# البحث في القائمة
contains_5 = 5 in numbers  # التحقق من وجود عنصر
index_of_5 = numbers.index(5)  # موقع العنصر

if __name__ == "__main__":
    print(f"القائمة الفارغ��: {empty_list}")
    print(f"قائمة الأرقام: {numbers}")
    print(f"القائمة المتنوعة: {mixed_list}")
    print(f"القائمة المتداخلة: {nested_list}")
    print(f"العنصر الأول: {first_item}")
    print(f"العنصر الأخير: {last_item}")
    print(f"جزء من القائمة: {sub_list}")
    print(f"طول القائمة: {list_length}")
    print(f"القائمة المدموجة: {combined}")
    print(f"القائمة المكررة: {repeated}")
    print(f"هل يوجد الرقم 5؟ {contains_5}")
    print(f"موقع الرقم 5: {index_of_5}") 