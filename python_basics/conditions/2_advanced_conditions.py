# الدرس الثاني: الشروط المتقدمة في بايثون
"""
تقنيات متقدمة في استخدام الشروط وأنماط شائعة في البرمجة
"""

# 1. استخدام match (متوفر في Python 3.10+)
def process_command(command):
    """معالجة الأوامر باستخدام match"""
    match command.lower():
        case "start":
            return "بدء التشغيل"
        case "stop":
            return "إيقاف التشغيل"
        case "restart":
            return "إعادة التشغيل"
        case _:
            return "أمر غير معروف"

# اختبار الدالة
print(process_command("START"))  # بدء التشغيل
print(process_command("stop"))   # إيقاف التشغيل
print(process_command("test"))   # أمر غير معروف

# 2. الشروط كقاموس (Dictionary of conditions)
def get_discount(customer_type):
    """حساب الخصم حسب نوع العميل"""
    discounts = {
        "vip": 0.2,      # خصم 20%
        "regular": 0.1,  # خصم 10%
        "new": 0.05     # خصم 5%
    }
    return discounts.get(customer_type, 0)  # 0 هو القيمة الافتراضية

# اختبار الدالة
print(f"خصم VIP: {get_discount('vip')}")
print(f"خصم عميل عادي: {get_discount('regular')}")
print(f"خصم عميل غير معروف: {get_discount('unknown')}")

# 3. استخدام all() و any()
def validate_user_input(username, password, email):
    """التحقق من صحة بيانات المستخدم"""
    checks = [
        len(username) >= 3,
        len(password) >= 8,
        '@' in email
    ]
    
    return all(checks)  # يجب أن تكون جميع الشروط صحيحة

# اختبار الدالة
print(validate_user_input("ahmed", "12345678", "ahmed@example.com"))  # True
print(validate_user_input("ah", "123", "invalid-email"))              # False

# 4. استخدام التعابير المنطقية المركبة
def check_number(num):
    """التحقق من خصائص الرقم"""
    if isinstance(num, int) and (num % 2 == 0 or num % 3 == 0):
        if num > 0 and num < 100:
            return "رقم صحيح موجب أقل من 100 وقابل للقسمة على 2 أو 3"
    return "لا يحقق الشروط"

# اختبار الدالة
print(check_number(12))  # يحقق الشروط
print(check_number(7))   # لا يحقق الشروط

# 5. استخدام الاستثناءات مع الشروط
def divide_safely(a, b):
    """قسمة آمنة مع التحقق من الأخطاء"""
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("يجب أن تكون الأرقام من نوع int أو float")
        if b == 0:
            raise ZeroDivisionError("لا يمكن القسمة على صفر")
        return a / b
    except (TypeError, ZeroDivisionError) as e:
        return f"خطأ: {str(e)}"

# اختبار الدالة
print(divide_safely(10, 2))    # 5.0
print(divide_safely(10, 0))    # خطأ: لا يمكن القسمة على صفر
print(divide_safely("10", 2))  # خطأ: يجب أن تكون الأرقام من نوع int أو float

# 6. نمط Guard Clause
def process_payment(amount, balance):
    """معالجة الدفع مع التحقق المبكر من الشروط"""
    # التحقق من الشروط أولاً
    if amount <= 0:
        return "مبلغ غير صالح"
    if balance <= 0:
        return "رصيد غير كافٍ"
    if amount > balance:
        return "المبلغ أكبر من الرصيد"
    
    # معالجة الدفع
    return f"تم الدفع بنجاح: {amount}"

# ��ختبار الدالة
print(process_payment(100, 500))  # تم الدفع بنجاح
print(process_payment(-100, 500)) # مبلغ غير صالح
print(process_payment(1000, 500)) # المبلغ أكبر من الرصيد 