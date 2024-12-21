# الدرس الأول: مقدمة في البرمجة كائنية التوجه

"""
البرمجة كائنية التوجه هي نموذج برمجي يعتمد على مفهوم "الكائنات"
التي يمكن أن تحتوي على بيانات وشيفرة برمجية
"""

# مثال بسيط لإنشاء فئة (Class)
class Car:
    # المُنشئ (Constructor)
    def __init__(self, brand, model, year):
        self.brand = brand    # ماركة السيارة
        self.model = model    # موديل السيارة
        self.year = year      # سنة الصنع
        self.speed = 0        # السرعة الحالية
    
    # دالة لزيادة السرعة
    def accelerate(self, speed_increase):
        """
        تزيد سرعة السيارة بمقدار معين
        المدخلات: speed_increase (int) - مقدار زيادة السرعة
        المخرجات: None
        """
        self.speed += speed_increase
        print(f"السرعة الحالية: {self.speed} كم/ساعة")
    
    # دالة لتخفيض السرعة
    def brake(self, speed_decrease):
        """
        تخفض سرعة السيارة بمقدار معين
        المدخلات: speed_decrease (int) - مقدار تخفيض السرعة
        المخرجات: None
        """
        self.speed = max(0, self.speed - speed_decrease)
        print(f"السرعة الحالية: {self.speed} كم/ساعة")

# مثال على استخدام الفئة
def main():
    # إنشاء كائن من فئة Car
    my_car = Car("تويوتا", "كامري", 2022)
    
    # استخدام دوال الكائن
    print(f"السيارة: {my_car.brand} {my_car.model} {my_car.year}")
    my_car.accelerate(50)
    my_car.accelerate(30)
    my_car.brake(20)

if __name__ == "__main__":
    main() 