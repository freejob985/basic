# الدرس الرابع: عمليات البت في بايثون
"""
عمليات البت تتعامل مع الأرقام على مستوى البت (الثنائي)
مفيدة في العمليات منخفضة المستوى والتشفير
"""

# 1. تحويل الأرقام إلى النظام الثنائي
a = 60  # بالثنائي: 0011 1100
b = 13  # بالثنائي: 0000 1101

print(f"العدد {a} بالنظام الثنائي: {bin(a)}")
print(f"العدد {b} بالنظام الثنائي: {bin(b)}")

# 2. عملية AND (&)
# تعيد 1 فقط إذا كان كلا البتين 1
result_and = a & b  # 0000 1100 = 12
print(f"نتيجة {a} & {b} = {result_and}")
print(f"بالنظام الثنائي: {bin(result_and)}")

# 3. عملية OR (|)
# تعيد 1 إذا كان أحد البتين 1
result_or = a | b  # 0011 1101 = 61
print(f"نتيجة {a} | {b} = {result_or}")
print(f"بالنظام الثنائي: {bin(result_or)}")

# 4. عملية XOR (^)
# تعيد 1 إذا كان البتان مختلفين
result_xor = a ^ b  # 0011 0001 = 49
print(f"نتيجة {a} ^ {b} = {result_xor}")
print(f"بالنظام الثنائي: {bin(result_xor)}")

# 5. عملية NOT (~)
# تقلب كل البتات
result_not = ~a  # -(0011 1101) = -61
print(f"نتيجة ~{a} = {result_not}")
print(f"بالنظام الثنائي: {bin(result_not)}")

# 6. عمليات الإزاحة
# إزاحة لليسار (<<)
shift_left = a << 2  # 1111 0000 = 240
print(f"نتيجة {a} << 2 = {shift_left}")
print(f"بالنظام الثنائي: {bin(shift_left)}")

# إزاحة لليمين (>>)
shift_right = a >> 2  # 0000 1111 = 15
print(f"نتيجة {a} >> 2 = {shift_right}")
print(f"بالنظام الثنائي: {bin(shift_right)}")

# 7. تطبيقات عملية

# استخدام الأقنعة البتية (Bit Masks)
def has_permission(permissions, permission_mask):
    """التحقق من وجود صلاحية معينة"""
    return permissions & permission_mask != 0

# تعريف الصلاحيات كأقنعة بتية
READ = 4    # 0100
WRITE = 2   # 0010
EXECUTE = 1  # 0001

# إنشاء مجموعة صلاحيات
user_permissions = READ | WRITE  # 0110

# التحقق من الصلاحيات
print(f"هل لديه صلاحية القراءة؟ {has_permission(user_permissions, READ)}")
print(f"هل لديه صلاحية التنفيذ؟ {has_permission(user_permissions, EXECUTE)}")

# 8. تشفير بسيط باستخدام XOR
def simple_encrypt(text, key):
    """تشفير نص باستخدام XOR"""
    return ''.join(chr(ord(c) ^ key) for c in text)

# تشفير وفك تشفير نص
message = "مرحباً"
key = 127

encrypted = simple_encrypt(message, key)
decrypted = simple_encrypt(encrypted, key)

print(f"النص الأصلي: {message}")
print(f"النص المشفر: {encrypted}")
print(f"النص بعد فك التشفير: {decrypted}") 