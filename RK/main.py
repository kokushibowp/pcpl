class Student:
    def __init__(self, id, name, group_id, rating):
        self.id = id
        self.name = name
        self.group_id = group_id
        self.rating = rating 

class Group:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class StudentGroup:
    def __init__(self, student_id, group_id):
        self.student_id = student_id
        self.group_id = group_id

def create_test_data():
    groups = [
        Group(1, 'АПервая'),
        Group(2, 'Вторая'),
        Group(3, 'АТретья'),
        Group(4, 'Четвертая')
    ]

    students = [
        Student(1, 'Иванов', 1, 4.5),
        Student(2, 'Петров', 1, 4.8),
        Student(3, 'Сидоров', 2, 4.2),
        Student(4, 'Кузнецов', 3, 4.7),
        Student(5, 'Алексеев', 4, 4.9),
        Student(6, 'Николаев', 4, 4.6)
    ]

    student_groups = [
        StudentGroup(1, 1),
        StudentGroup(2, 1),
        StudentGroup(3, 2),
        StudentGroup(4, 3),
        StudentGroup(5, 4),
        StudentGroup(6, 4)
    ]
    return groups, students, student_groups

def get_students_with_ov_surname(groups, students):
    return [(s.name, g.name) 
            for g in groups 
            for s in students 
            if s.group_id == g.id and s.name.endswith('ов')]

def get_average_rating(groups, students):
    return sorted(
        [(g.name, 
          sum(s.rating for s in students if s.group_id == g.id) / 
          len([s for s in students if s.group_id == g.id])) 
         for g in groups 
         if any(s.group_id == g.id for s in students)],
        key=lambda x: x[1], 
        reverse=True
    )

def get_groups_starting_with_a(groups, student_groups, students):
    return {
        g.name: [s.name for s in students 
                 if s.id in [sg.student_id for sg in student_groups 
                            if sg.group_id == g.id]]
        for g in groups 
        if g.name.startswith('А')
    }

def main():
    groups, students, student_groups = create_test_data()
    
    print("\n--- Задание 1 ---")
    print("Студенты с фамилиями на 'ов':")
    result1 = get_students_with_ov_surname(groups, students)
    print(f"Найдено {len(result1)} записей:")
    for student in result1:
        print(f"  {student[0]} - {student[1]}")
    
    print("\n--- Задание 2 ---")
    print("Средний рейтинг по группам (от высшего к низшему):")
    result2 = get_average_rating(groups, students)
    print(f"Всего групп: {len(result2)}")
    for group in result2:
        print(f"  Группа: {group[0]}, Средний рейтинг: {group[1]:.2f}")
    
    print("\n--- Задание 3 ---")
    print("Группы на букву 'А' и их студенты:")
    result3 = get_groups_starting_with_a(groups, student_groups, students)
    for group_name, students_list in result3.items():
        print(f"  Группа: {group_name}")
        print("  Студенты:")
        for student in students_list:
            print(f"    - {student}")

if __name__ == "__main__":
    main()
