import pytest
from main import (
    create_test_data,
    get_students_with_ov_surname,
    get_average_rating,
    get_groups_starting_with_a
)

def test_students_with_ov_surname():
    groups, students, _ = create_test_data()
    result = get_students_with_ov_surname(groups, students)
    
    assert len(result) == 4
    
    assert result == [
        ('Иванов', 'АПервая'),
        ('Петров', 'АПервая'),
        ('Сидоров', 'Вторая'),
        ('Кузнецов', 'АТретья')
    ]

def test_average_rating():
    groups, students, _ = create_test_data()
    result = get_average_rating(groups, students)
    
    assert len(result) == 4
    
    assert result == [
        ('Четвертая', 4.75),
        ('АТретья', 4.7),
        ('АПервая', 4.65),  
        ('Вторая', 4.2)  
    ]

def test_groups_starting_with_a():
    groups, students, student_groups = create_test_data()
    result = get_groups_starting_with_a(groups, student_groups, students)
    
    assert isinstance(result, dict)
    
    assert len(result) == 2
    
    assert result == {
        'АПервая': ['Иванов', 'Петров'],
        'АТретья': ['Кузнецов']
    }
