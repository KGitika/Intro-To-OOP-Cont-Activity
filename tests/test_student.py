from school_schedule.student import Student

# Write your tests here!
def test_student_class_instantiation():
    #arrange
    name = "Ada"
    grade = "junior"
    classes = ["Math", "Science", "Art"]
    #act

    student = Student(name, grade, classes)

    #assert
    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes

def test_add_class_to_classes():
    #arrange
    name = "Ada"
    grade = "junior"
    classes = ["Math", "Science", "Art"]
    #act

    student = Student(name, grade, classes)
    updated_classes = student.add_class("Economics")

    #assert
    assert updated_classes == classes
    assert updated_classes[-1] == "Economics"
    assert len(classes) == 4

def test_display_classes():
    #arrange
    name = "Ada"
    grade = "junior"
    classes = ["Math", "Science", "Art"]
    expect_result = "Math, Science, Art"
    #act

    student = Student(name, grade, classes)
    actual_result = student.display_classes()
    

    assert actual_result == expect_result

def test_student_summary_return():
    #arrange
    name = "Ada"
    grade = "junior"
    classes = ["Math", "Science", "Art"]
    expect_result = f"{name} is a {grade} " + "enrolled in 3 classes: " + "Math, Science, Art"
    #act

    student = Student(name, grade, classes)
    actual_result = student.summary()

    assert actual_result == expect_result

