from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

def test_new_valid_middle_school_student_with_defaults():
    student = MiddleSchoolStudent(
        "Daisy",
        "7th grade",
        ["Math", "English"]
    )

    assert student.name == "Daisy"
    assert student.grade == "7th grade"
    assert student.classes == ["Math", "English"]
    assert student.gets_transportation is False 

def test_middle_school_student_summary_with_transportation():

    student = MiddleSchoolStudent(
            "Daisy",
            "7th grade",
            ["Math", "English"],False
        )

    assert student.name == "Daisy"
    assert student.grade == "7th grade"
    assert student.classes == ["Math", "English"]
    assert student.gets_transportation is False 

def test_middle_school_student_summary_without_transportation():
    
    student = MiddleSchoolStudent(
        "Daisy",
        "7th grade",
        ["Math", "English"],True
    )

    assert student.name == "Daisy"
    assert student.grade == "7th grade"
    assert student.classes == ["Math", "English"]
    assert student.gets_transportation is True 
