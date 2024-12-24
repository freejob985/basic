"""
أمثلة عملية على استخدام القوائم في Python
"""

def example_1_todo_list():
    """
    مثال 1: قائمة المهام
    """
    tasks = []
    
    def add_task(task):
        tasks.append(task)
        print(f"تمت إضافة المهمة: {task}")
    
    def remove_task(task):
        if task in tasks:
            tasks.remove(task)
            print(f"تم حذف المهمة: {task}")
        else:
            print(f"المهمة '{task}' غير موجودة")
    
    def show_tasks():
        if tasks:
            print("\nقائمة المهام:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("لا توجد مهام حالياً")
    
    # تجربة القائمة
    add_task("كتابة التقرير")
    add_task("اجتماع الفريق")
    add_task("تحديث الموقع")
    show_tasks()
    remove_task("اجتماع الفريق")
    show_tasks()

def example_2_grade_analysis():
    """
    مثال 2: تحليل الدرجات
    """
    grades = [85, 92, 78, 65, 88, 72, 90, 85]
    
    # حساب المتوسط
    average = sum(grades) / len(grades)
    
    # الدرجة الأعلى والأدنى
    highest = max(grades)
    lowest = min(grades)
    
    # عدد الطلاب الناجحين (درجة >= 70)
    passing = len([g for g in grades if g >= 70])
    
    print("\nتحليل الدرجات:")
    print(f"متوسط الدرجات: {average:.2f}")
    print(f"أعلى درجة: {highest}")
    print(f"أدنى درجة: {lowest}")
    print(f"عدد الطلاب الناجحين: {passing} من {len(grades)}")

def example_3_shopping_cart():
    """
    مثال 3: سلة التسوق
    """
    cart = []
    
    def add_item(item, price):
        cart.append({"item": item, "price": price})
        print(f"تمت إضافة {item} بسعر {price}")
    
    def calculate_total():
        return sum(item["price"] for item in cart)
    
    def show_cart():
        if cart:
            print("\nمحتويات السلة:")
            for i, item in enumerate(cart, 1):
                print(f"{i}. {item['item']} - {item['price']} ريال")
            print(f"المجموع: {calculate_total()} ريال")
        else:
            print("السلة فارغة")
    
    # تجربة سلة التسوق
    add_item("قميص", 100)
    add_item("بنطلون", 150)
    add_item("حذاء", 200)
    show_cart()

if __name__ == "__main__":
    print("=== مثال 1: قائمة المهام ===")
    example_1_todo_list()
    
    print("\n=== مثال 2: تحليل الدرجات ===")
    example_2_grade_analysis()
    
    print("\n=== مثال 3: سلة التسوق ===")
    example_3_shopping_cart() 