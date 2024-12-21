# أمثلة إضافية للبرمجة كائنية التوجه
"""
هذا الملف يحتوي على أمثلة إضافية متنوعة لتوضيح مفاهيم البرمجة كائنية التوجه
كل مثال يوضح مفاهيم مختلفة مع شرح تفصيلي
"""

# المثال الأول: نظام التجارة الإلكترونية
class Product:
    """
    فئة المنتج: تمثل منتجاً في متجر إلكتروني
    الخصائص:
        - name: اسم المنتج
        - price: السعر
        - stock: الكمية المتوفرة
    """
    def __init__(self, name: str, price: float, stock: int):
        self.__name = name          # اسم المنتج (خاص)
        self.__price = price        # سعر المنتج (خاص)
        self.__stock = stock        # الكمية المتوفرة (خاص)
    
    @property
    def name(self) -> str:
        """الحصول على اسم المنتج"""
        return self.__name
    
    @property
    def price(self) -> float:
        """الحصول على سعر المنتج"""
        return self.__price
    
    def check_availability(self, quantity: int) -> bool:
        """
        التحقق من توفر الكمية المطلوبة
        المدخلات: quantity - الكمية المطلوبة
        المخرجات: True إذا كانت الكمية متوفرة، False إذا لم تكن متوفرة
        """
        return self.__stock >= quantity
    
    def reduce_stock(self, quantity: int) -> None:
        """تخفيض المخزون بعد الشراء"""
        if self.check_availability(quantity):
            self.__stock -= quantity

class ShoppingCart:
    """
    فئة عربة التسوق: تحتوي على المنتجات المراد شراؤها
    تستخدم القاموس (dict) لتخزين المنتجات وكمياتها
    """
    def __init__(self):
        self.__items = {}  # قاموس يخزن المنتجات وكمياتها
        
    def add_item(self, product: Product, quantity: int = 1) -> bool:
        """
        إضافة منتج إلى عربة التسوق
        المدخلات:
            - product: المنتج المراد إضافته
            - quantity: الكمية المطلوبة (افتراضياً 1)
        المخرجات: True إذا تمت الإضافة بنجاح، False إذا فشلت
        """
        if product.check_availability(quantity):
            if product in self.__items:
                self.__items[product] += quantity
            else:
                self.__items[product] = quantity
            return True
        return False
    
    def get_total(self) -> float:
        """
        حساب المجموع الكلي للمشتريات
        المخرجات: القيمة الإجمالية للمنتجات في العربة
        """
        return sum(product.price * quantity 
                  for product, quantity in self.__items.items())
    
    def checkout(self) -> None:
        """
        إتمام عملية الشراء
        تخفيض المخزون وتفريغ العربة
        """
        for product, quantity in self.__items.items():
            product.reduce_stock(quantity)
        self.__items.clear()

# المثال الثاني: نظام المدرسة
class Person:
    """
    فئة أساسية تمثل شخصاً في النظام المدرسي
    مثال على الوراثة المتعددة والتجريد
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def get_info(self) -> str:
        """
        دالة مجردة للحصول على معلومات الشخص
        سيتم تنفيذها بشكل مختلف في الفئات الفرعية
        """
        return f"الاسم: {self.name}, العمر: {self.age}"

class Student(Person):
    """فئة الطالب - ترث من فئة Person"""
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []
    
    def get_info(self) -> str:
        """تنفيذ مختلف لدالة get_info - مثال على تعدد الأشكال"""
        base_info = super().get_info()
        return f"{base_info}\nرقم الطالب: {self.student_id}"
    
    def enroll(self, course: 'Course') -> None:
        """تسجيل الطالب في مادة دراسية"""
        self.courses.append(course)
        course.add_student(self)

class Teacher(Person):
    """فئة المعلم - ترث من فئة Person"""
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.subject = subject
        self.courses = []
    
    def get_info(self) -> str:
        """تنفيذ مختلف لدالة get_info - مثال على تعدد الأشكال"""
        base_info = super().get_info()
        return f"{base_info}\nالمادة: {self.subject}"

class Course:
    """فئة المادة الدراسية"""
    def __init__(self, name: str, teacher: Teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        teacher.courses.append(self)
    
    def add_student(self, student: Student) -> None:
        """إضافة طالب إلى المادة"""
        if student not in self.students:
            self.students.append(student)

def main():
    # تجربة نظام التجارة الإلكترونية
    print("=== نظام التجارة الإلكترونية ===")
    # إنشاء منتجات
    laptop = Product("لابتوب", 5000, 10)
    phone = Product("هاتف ذكي", 2000, 20)
    
    # إنشاء عربة تسوق وإضافة منتجات
    cart = ShoppingCart()
    cart.add_item(laptop, 2)
    cart.add_item(phone, 1)
    
    print(f"المجموع الكلي: {cart.get_total()} ريال")
    cart.checkout()
    
    # تجربة نظام المدرسة
    print("\n=== نظام المدرسة ===")
    # إنشاء معلم ومادة
    math_teacher = Teacher("أحمد", 35, "رياضيات")
    math_course = Course("رياضيات متقدمة", math_teacher)
    
    # إنشاء طلاب وتسجيلهم في المادة
    student1 = Student("محمد", 18, "ST001")
    student2 = Student("سارة", 17, "ST002")
    
    student1.enroll(math_course)
    student2.enroll(math_course)
    
    # عرض معلومات المشاركين
    print(math_teacher.get_info())
    print("\nالطلاب المسجلون:")
    for student in math_course.students:
        print(student.get_info())

if __name__ == "__main__":
    main() 