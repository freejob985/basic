# الدرس الخامس: التجريد (Abstraction)

"""
التجريد هو إخفاء التعقيد وإظهار الواجهة البسيطة للمستخدم
نستخدم الفئات المجردة (Abstract Classes) لتحقيق التجريد
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """
        دالة مجردة لحساب المساحة
        """
        pass
    
    @abstractmethod
    def perimeter(self):
        """
        دالة مجردة لحساب المحيط
        """
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """
        حساب مساحة المستطيل
        المخرجات: float - المساحة
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        حساب محيط المستطيل
        المخرجات: float - المحيط
        """
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """
        حساب مساحة الدائرة
        المخرجات: float - المساحة
        """
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """
        حساب محيط الدائرة
        المخرجات: float - المحيط
        """
        import math
        return 2 * math.pi * self.radius

def print_shape_info(shape):
    """
    دالة لطباعة معلومات الشكل
    المدخلات: shape (Shape) - الشكل المراد عرض معلوماته
    """
    print(f"المساحة: {shape.area():.2f}")
    print(f"المحيط: {shape.perimeter():.2f}")

def main():
    # إنشاء أشكال مختلفة
    rectangle = Rectangle(5, 3)
    circle = Circle(4)
    
    print("معلومات المستطيل:")
    print_shape_info(rectangle)
    
    print("\nمعلومات الدائرة:")
    print_shape_info(circle)

if __name__ == "__main__":
    main() 