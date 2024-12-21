# الدرس الثاني: نطاق المتغيرات (Variable Scope)

"""
نطاق المتغير يحدد أين يمكن استخدام المتغير في البرنامج
هناك نوعان رئيسيان: المتغيرات العامة (Global) والمتغيرات المحلية (Local)
"""

# 1. المتغيرات العامة (Global Variables)
global_var = "أنا متغير عام"  # هذا متغير عام يمكن استخدامه في أي مكان

def print_global():
    """دالة تطبع المتغير العام"""
    print(f"المتغير العام داخل الدالة: {global_var}")

print(f"المتغير العام خارج الدالة: {global_var}")
print_global()

# 2. المتغيرات المحلية (Local Variables)
def local_example():
    """دالة توضح المتغيرات المحلية"""
    local_var = "أنا متغير محلي"  # هذا متغير محلي متاح فقط داخل الدالة
    print(f"المتغير المحلي داخل الدالة: {local_var}")

local_example()
# print(local_var)  # هذا سيسبب خطأ لأن local_var غير متاح خارج الدالة

# 3. استخدام الكلمة المفتاحية global
counter = 0  # متغير عام

def increment_counter():
    """دالة لزيادة العداد العام"""
    global counter  # نعلن أننا نريد استخدام المتغير العام
    counter += 1
    print(f"قيمة العداد: {counter}")

increment_counter()  # سيطبع: قيمة العداد: 1
increment_counter()  # سيطبع: قيمة العداد: 2

# 4. المتغيرات المتداخلة (Nested Variables)
def outer_function():
    """دالة خارجية"""
    outer_var = "أنا في الدالة الخارجية"
    
    def inner_function():
        """دالة داخلية"""
        inner_var = "أنا في الدالة الداخلية"
        print(outer_var)  # يمكن الوصول للمتغير الخارجي
        print(inner_var)
    
    inner_function()
    # print(inner_var)  # هذا سيسبب خطأ

outer_function() 