# الدرس الرابع: التغليف (Encapsulation)

"""
التغليف هو إخفاء التفاصيل الداخلية للكائن وحماية البيانات من الوصول المباشر
"""

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.__account_holder = account_holder  # متغير خاص
        self.__balance = initial_balance        # متغير خاص
        self.__account_number = self.__generate_account_number()
    
    def __generate_account_number(self):
        """
        دالة خاصة لتوليد رقم حساب
        المخرجات: str - رقم الحساب
        """
        import random
        return f"ACC-{random.randint(10000, 99999)}"
    
    def get_balance(self):
        """
        دالة للحصول على الرصيد
        المخرجات: float - رصيد الحساب
        """
        return self.__balance
    
    def deposit(self, amount):
        """
        دالة للإيداع في الحساب
        المدخلات: amount (float) - المبلغ المراد إيداعه
        """
        if amount > 0:
            self.__balance += amount
            print(f"تم إيداع {amount} ريال. الرصيد الحالي: {self.__balance}")
        else:
            print("مبلغ الإيداع يجب أن يكون أكبر من صفر")
    
    def withdraw(self, amount):
        """
        دالة للسحب من الحساب
        المدخلات: amount (float) - المبلغ المراد سحبه
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"تم سحب {amount} ريال. الرصيد الحالي: {self.__balance}")
        else:
            print("رصيد غير كافٍ أو مبلغ غير صالح")
    
    def get_account_info(self):
        """
        دالة للحصول على معلومات الحساب
        المخرجات: str - معلومات الحساب
        """
        return f"""
        صاحب الحساب: {self.__account_holder}
        رقم الحساب: {self.__account_number}
        الرصيد الحالي: {self.__balance} ريال
        """

def main():
    # إنشاء حساب بنكي جديد
    account = BankAccount("أحمد محمد", 1000)
    
    # محاولة الوصول للمتغيرات الخاصة مباشرة لن تنجح
    # print(account.__balance)  # سيؤدي إلى خطأ
    
    # استخدام الدوال العامة للتعامل مع الحساب
    print(account.get_account_info())
    account.deposit(500)
    account.withdraw(200)
    print(f"الرصيد الحالي: {account.get_balance()} ريال")

if __name__ == "__main__":
    main() 