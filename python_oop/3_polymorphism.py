# الدرس الثالث: تعدد الأشكال (Polymorphism)

"""
تعدد الأشكال يسمح للكائنات من فئات مختلفة بالاستجابة بشكل مختلف لنفس الدالة
"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        """
        دالة افتراضية لإصدار صوت الحيوان
        """
        pass

class Cat(Animal):
    def make_sound(self):
        """
        المخرجات: str - صوت القط
        """
        return f"{self.name} يقول: مياو!"

class Dog(Animal):
    def make_sound(self):
        """
        المخرجات: str - صوت الكلب
        """
        return f"{self.name} يقول: هاو هاو!"

class Duck(Animal):
    def make_sound(self):
        """
        المخرجات: str - صوت البطة
        """
        return f"{self.name} يقول: كواك كواك!"

def animal_sound(animal):
    """
    دالة تستقبل أي حيوان وتطبع صوته
    المدخلات: animal (Animal) - كائن من ��ئة الحيوان
    """
    print(animal.make_sound())

def main():
    # إنشاء حيوانات مختلفة
    cat = Cat("قطقوط")
    dog = Dog("رعد")
    duck = Duck("بطوط")
    
    # استدعاء نفس الدالة مع كائنات مختلفة
    animal_sound(cat)
    animal_sound(dog)
    animal_sound(duck)

if __name__ == "__main__":
    main() 