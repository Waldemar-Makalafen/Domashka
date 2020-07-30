class People:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
 
    def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname
 
    def get_short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())

class Shkolnik(People):
    def __init__(self, name, patronymic, surname, mom, dad, school_class):
        People.__init__(self, name, patronymic, surname)
        self.mom = mom
        self.dad = dad
        self.school_class = school_class
 
 
class Teacher(People):
    def __init__(self, name, patronymic, surname, subject):
        People.__init__(self, name, patronymic, surname)
        self.subject = subject
 
 
class Class_rooms:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachersdict = {t.subject: t for t in teachers}
 
 
 
if __name__ == '__main__':  # Тестирование.
    teachers = [Teacher('Иван', 'Иванович', 'Иванов', 'Математика'),
                Teacher('Петр', 'Петрович', 'Петров', 'Литература'),
                Teacher('Сидор', 'Сидорович', 'Сидоров', 'Физика'),
                Teacher('Дмитрий', 'Дмитриевич', 'Дмитриев', 'История'),
                Teacher('Никита', 'Никитиевич', 'Никишин', 'Биология')]
    classes = [Class_rooms('11 А', [teachers[0], teachers[1], teachers[2]]),
               Class_rooms('11 Б', [teachers[1], teachers[3], teachers[4]]),
               Class_rooms('10 А', [teachers[3], teachers[1], teachers[0]])]
    parents = [People('Семен', 'Семенович', 'Семенов'),
               People('Светлана', 'Савельевна', 'Семенова'),
               People('Роман', 'Романович', 'Романов'),
               People('Римма', 'Романовна', 'Романова'),
               People('Сергей', 'Сергеевич', 'Сергеев'),
               People('Юлия', 'Викторвна', 'Сергеева')]
    students = [Shkolnik('Игорь', 'Cеменович', 'Семенов', parents[0], parents[1], classes[0]),
                Shkolnik('Ольга', 'Романова', 'Романова', parents[2], parents[3], classes[1]),
                Shkolnik('Александр', 'Сергеевич', 'Сергеев', parents[4], parents[5], classes[2])]
    print('Список классов в школе: ')
    for f in classes:
        print(f.class_room)
 
    for f in classes:
        print('Учителя, преподающие в {} классе:'.format(f.class_room))
        for teacher in classes[0].teachersdict.values():
            print(teacher.get_full_name())
    for f in classes:
        print("Ученики в классе {}:".format(f.class_room))
        for st in students:
            print(st.get_short_name())
 