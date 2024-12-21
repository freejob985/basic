# الدرس الثاني: الوراثة في البرمجة كائنية التوجه

"""
الوراثة هي آلية تسمح بإنشاء فئة جديدة باستخدام خصائص ودوال فئة موجودة
"""

# الفئة الأساسية
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start_engine(self):
        """
        تشغيل محرك المركبة
        المخرجات: str - رسالة تأكيد تشغيل المحرك
        """
        return f"تم تشغيل محرك {self.brand} {self.model}"

# فئة فرعية ترث من Vehicle
class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)  # استدعاء مُنشئ الفئة الأساسية
        self.battery_capacity = battery_capacity
    
    def charge(self):
        """
        شحن السيارة الكهربائية
        المخرجات: str - رسالة تأكيد بدء الشحن
        """
        return f"جاري ��حن {self.brand} {self.model}. السعة: {self.battery_capacity} كيلوواط"

def main():
    # إنشاء كائن من السيارة الكهربائية
    tesla = ElectricCar("تسلا", "Model 3", 2023, 75)
    
    # استخدام دوال من الفئة الأساسية والفرعية
    print(tesla.start_engine())
    print(tesla.charge())

if __name__ == "__main__":
    main() 