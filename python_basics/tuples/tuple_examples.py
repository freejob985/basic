"""
أمثلة عملية على استخدام المتتاليات الثابتة في Python
"""

def example_1_coordinates():
    """
    مثال 1: التعامل مع الإحداثيات
    """
    # تمثيل نقاط في المستوى
    points = [
        (0, 0),  # نقطة الأصل
        (1, 2),
        (-1, 3),
        (4, -2)
    ]
    
    def calculate_distance(point):
        x, y = point
        return (x**2 + y**2) ** 0.5
    
    # حساب المسافة لكل نقطة من نقطة الأصل
    for point in points:
        distance = calculate_distance(point)
        print(f"المسافة من نقطة الأصل إلى النقطة {point}: {distance:.2f}")

def example_2_student_records():
    """
    مثال 2: سجلات الطلاب
    """
    # تمثيل سجلات الطلاب (الاسم، العمر، المعدل)
    students = [
        ("أحمد", 20, 3.8),
        ("سارة", 19, 3.9),
        ("محمد", 21, 3.5),
        ("نور", 20, 4.0)
    ]
    
    # طباعة معلومات الطلاب
    print("\nسجلات الطلاب:")
    for name, age, gpa in students:
        print(f"الطالب: {name}, العمر: {age}, المعدل: {gpa}")
    
    # إيجاد الطالب صاحب أعلى معدل
    best_student = max(students, key=lambda x: x[2])
    print(f"\nالطالب صاحب أعلى معدل: {best_student[0]} بمعدل {best_student[2]}")

def example_3_rgb_colors():
    """
    مثال 3: التعامل مع الألوان RGB
    """
    # تعريف بعض الألوان الأساسية
    colors = {
        "أحمر": (255, 0, 0),
        "أخضر": (0, 255, 0),
        "أزرق": (0, 0, 255),
        "أبيض": (255, 255, 255),
        "أسود": (0, 0, 0)
    }
    
    def mix_colors(color1, color2):
        """دمج لونين بأخذ متوسط قيمهم"""
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        return (
            (r1 + r2) // 2,
            (g1 + g2) // 2,
            (b1 + b2) // 2
        )
    
    # تجربة دمج الألوان
    print("\nدمج الألوان:")
    mixed = mix_colors(colors["أحمر"], colors["أزرق"])
    print(f"دمج الأحمر مع الأزرق: {mixed}")

if __name__ == "__main__":
    print("=== مثال 1: التعامل مع الإحداثيات ===")
    example_1_coordinates()
    
    print("\n=== مثال 2: سجلات الطلاب ===")
    example_2_student_records()
    
    print("\n=== مثال 3: التعامل مع الألوان RGB ===")
    example_3_rgb_colors() 