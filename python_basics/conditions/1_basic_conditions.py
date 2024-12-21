# الدرس الأول: الشروط الأساسية في بايثون
"""
الشروط تسمح للبرنامج باتخاذ قرارات مختلفة بناءً على الظروف
نستخدم if, elif, else للتحكم في مسار البرنامج
"""

# 1. الشرط البسيط if
age = 18

# التحقق من شرط واحد
if age >= 18:
    print("أنت بالغ")  # سيتم تنفيذ هذا السطر إذا كان العمر 18 أو أكبر
    print("يمكنك التصويت")

# 2. الشرط if مع else
temperature = 35

if temperature > 30:
    print("الجو حار")
else:
    print("الجو معتدل")  # سيتم تنفيذ هذا السطر إذا كانت درجة الحرارة 30 أو أقل

# 3. الشروط المتعددة باستخدام elif
grade = 85

if grade >= 90:
    print("ممتاز")
elif grade >= 80:
    print("جيد جداً")  # سيتم تنفيذ هذا السطر لأن العلامة 85
elif grade >= 70:
    print("جيد")
else:
    print("تحتاج إلى تحسين")

# 4. الشروط المتداخلة (Nested Conditions)
has_passport = True
has_ticket = True

if has_passport:
    if has_ticket:
        print("يمكنك السفر")
    else:
        print("تحتاج إلى تذكرة")
else:
    print("تحتاج إلى جواز سفر")

# 5. الشروط المركبة باستخدام and و or
username = "ahmed"
password = "123456"

if len(username) >= 3 and len(password) >= 6:
    print("بيانات تسجيل الدخول صحيحة")
else:
    print("يجب أن يكون اسم المستخدم 3 أحرف على الأقل وكلمة المرور 6 أحرف")

# 6. استخدام in للتحقق من العضوية
fruits = ["تفاح", "موز", "برتقال"]
fruit = "موز"

if fruit in fruits:
    print(f"{fruit} موجود في القائمة")

# 7. التحقق من القيم الفارغة
text = ""
number = 0
my_list = []

# التحقق من النص الفارغ
if not text:
    print("النص فارغ")

# التحقق من الرقم الصفري
if number == 0:
    print("الرقم صفر")

# التحقق من القائمة الفارغة
if not my_list:
    print("القائمة فارغة")

# 8. استخدام is للتحقق من الهوية
x = None

if x is None:
    print("المتغير x يساوي None")

# 9. الشرط في سطر واحد (Ternary Operator)
age = 20
status = "بالغ" if age >= 18 else "قاصر"
print(f"الحالة: {status}")

# 10. أمثلة عملية

# مثال 1: التحقق من صحة كلمة المرور
def check_password(password):
    """التحقق من قوة كلمة المرور"""
    if len(password) < 8:
        return "كلمة المرور قصيرة جداً"
    elif password.isalpha():
        return "يجب أن تحتوي كلمة المرور على أرقام"
    elif password.isdigit():
        return "يجب أن تحتوي كلمة المرور على حروف"
    else:
        return "كلمة المرور مقبولة"

# اختبار الدالة
print(check_password("abc123456"))  # كلمة المرور مقبولة
print(check_password("abc"))        # كلمة المرور قصيرة جداً
print(check_password("abcdefgh"))   # يجب أن تحتوي كلمة المرور على أرقام

# مثال 2: تحديد فئة العمر
def get_age_category(age):
    """تحديد فئة العمر"""
    if age < 0:
        return "عمر غير صالح"
    elif age < 13:
        return "طفل"
    elif age < 20:
        return "مراهق"
    elif age < 65:
        return "بالغ"
    else:
        return "متقاعد"

# اختبار الدالة
print(get_age_category(8))   # طفل
print(get_age_category(15))  # مراهق
print(get_age_category(35))  # بالغ
print(get_age_category(70))  # متقاعد 