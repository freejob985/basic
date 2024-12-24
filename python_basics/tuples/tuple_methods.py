"""
شرح الدوال المتاحة للمتتاليات الثابتة (Tuples) في Python
"""

# متتالية للتجربة
numbers = (1, 3, 2, 5, 4, 3, 5)

# دوال العد والبحث
count_of_3 = numbers.count(3)  # عد تكرار قيمة
index_of_5 = numbers.index(5)  # موقع أول ظهور للقيمة

# تحويل المتتالية إلى قائمة
list_from_tuple = list(numbers)  # تحويل إلى قائمة

# تحويل القائمة إلى متتالية
tuple_from_list = tuple([1, 2, 3])  # تحويل قائمة إلى متتالية

# فك عناصر المتتالية (Unpacking)
a, b, *rest = (1, 2, 3, 4, 5)  # فك العناصر إلى متغيرات

# مقارنة المتتاليات
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (3, 2, 1)
are_equal = tuple1 == tuple2  # مقارنة المتتاليات

if __name__ == "__main__":
    print(f"المتتالية الأصلية: {numbers}")
    print(f"عدد تكرار الرقم 3: {count_of_3}")
    print(f"موقع أول ظهور للرقم 5: {index_of_5}")
    print(f"تحويل إلى قائمة: {list_from_tuple}")
    print(f"تحويل من قائمة: {tuple_from_list}")
    print(f"فك العناصر: a={a}, b={b}, rest={rest}")
    print(f"مقارنة المتتاليات:")
    print(f"tuple1 == tuple2: {tuple1 == tuple2}")
    print(f"tuple1 == tuple3: {tuple1 == tuple3}") 