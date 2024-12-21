# تمارين متقدمة في البرمجة كائنية التوجه

"""
هذا الملف يحتوي على تمارين متقدمة تجمع بين مختلف مفاهيم البرمجة كائنية التوجه
"""

from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime

# التمرين الأول: نظام إدارة المطعم
class MenuItem(ABC):
    """
    فئة مجردة تمثل عنصراً في قائمة الطعام
    مثال على التجريد والتغليف
    """
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def price(self) -> float:
        return self.__price
    
    @abstractmethod
    def get_description(self) -> str:
        """دالة مجردة للحصول على وصف العنصر"""
        pass

class MainDish(MenuItem):
    """فئة الطبق الرئيسي"""
    def __init__(self, name: str, price: float, calories: int):
        super().__init__(name, price)
        self.calories = calories
    
    def get_description(self) -> str:
        return f"{self.name} - {self.calories} سعرة حرارية"

class Drink(MenuItem):
    """فئة المشروبات"""
    def __init__(self, name: str, price: float, size: str):
        super().__init__(name, price)
        self.size = size
    
    def get_description(self) -> str:
        return f"{self.name} - حجم {self.size}"

class Order:
    """
    فئة الطلب: تمثل طلباً في المطعم
    مثال على استخدام القواميس والتغليف
    """
    def __init__(self):
        self.__items: Dict[MenuItem, int] = {}
        self.__order_time = datetime.now()
        self.__status = "جديد"
    
    def add_item(self, item: MenuItem, quantity: int = 1) -> None:
        """إضافة عنصر إلى الطلب"""
        if item in self.__items:
            self.__items[item] += quantity
        else:
            self.__items[item] = quantity
    
    def get_total(self) -> float:
        """حساب إجمالي الطلب"""
        return sum(item.price * quantity 
                  for item, quantity in self.__items.items())
    
    def get_receipt(self) -> str:
        """طباعة فاتورة الطلب"""
        receipt = f"=== ف��تورة الطلب ===\n"
        receipt += f"التاريخ: {self.__order_time}\n"
        receipt += f"الحالة: {self.__status}\n\n"
        
        for item, quantity in self.__items.items():
            receipt += f"{item.get_description()} × {quantity}"
            receipt += f" = {item.price * quantity} ريال\n"
        
        receipt += f"\nالإجمالي: {self.get_total()} ريال"
        return receipt

class Restaurant:
    """
    فئة المطعم: تدير قائمة الطعام والطلبات
    مثال على إدارة العلاقات بين الكائنات
    """
    def __init__(self, name: str):
        self.name = name
        self.menu: List[MenuItem] = []
        self.orders: List[Order] = []
    
    def add_menu_item(self, item: MenuItem) -> None:
        """إضافة عنصر إلى قائمة الطعام"""
        self.menu.append(item)
    
    def place_order(self, order: Order) -> None:
        """تسجيل طلب جديد"""
        self.orders.append(order)
    
    def print_menu(self) -> None:
        """طباعة قائمة الطعام"""
        print(f"\n=== قائمة طعام {self.name} ===")
        for item in self.menu:
            print(f"{item.get_description()} - {item.price} ريال")

def main():
    # إنشاء مطعم وإضافة عناصر للقائمة
    restaurant = Restaurant("مطعم الذواقة")
    
    # إضافة أطباق رئيسية
    restaurant.add_menu_item(MainDish("برجر لحم", 35, 800))
    restaurant.add_menu_item(MainDish("دجاج مشوي", 40, 600))
    
    # إضافة مشروبات
    restaurant.add_menu_item(Drink("عصير برتقال", 10, "كبير"))
    restaurant.add_menu_item(Drink("مشروب غازي", 7, "وسط"))
    
    # عرض القائمة
    restaurant.print_menu()
    
    # إنشاء طلب جديد
    order = Order()
    burger = restaurant.menu[0]  # برجر لحم
    juice = restaurant.menu[2]   # عصير برتقال
    
    order.add_item(burger, 2)
    order.add_item(juice, 2)
    
    # تسجيل الطلب وطباعة الفاتورة
    restaurant.place_order(order)
    print("\n" + order.get_receipt())

if __name__ == "__main__":
    main() 