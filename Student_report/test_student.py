# import unittest
# from student_report_card import Student

# class TestStudent(unittest.TestCase):
#     def setUp(self):
#         self.student = Student('Saroja',[57,89,90,78,75,67])
#     def   test_total_marks(self):
#         self.assertEqual(self.student.get_total(), 456)
    
#     def test_average_marks(self):
#         self.assertAlmostEqual(self.student.get_average(), 456 / 6)
        
#     def test_grade(self):
#         self.assertEqual(self.student.get_grade(), "B")

#     def test_low_grade(self):
#         student2 = Student("Arun", [10, 20, 25])
#         self.assertEqual(student2.get_grade(), "E")
        
#     def test_high_grade(self):
#         student3 = Student("Asha", [95, 92, 97])
#         self.assertEqual(student3.get_grade(), "S")

import pytest
from student_report_card import Student

@pytest.fixture
def student():
    return Student('Saroja',[57,89,90,78,75,67])

def test_total_marks(student):
    assert student.get_total() == 456
    
def test_average_mark(student):
    assert student.get_average() == pytest.approx(456 / 6)

def test_grade(student):
    assert student.get_grade() == 'B' 
    
def test_low_grade():
    s = Student("Arun",[23,10,15])
    assert s.get_grade() == 'E'              

def test_hight_grade():
    s = Student('AAsif',[90,95,92])
    assert s.get_grade() == 'S' 
    
    
