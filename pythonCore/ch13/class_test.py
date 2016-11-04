#!/usr/bin/env python
# -*- coding: utf-8 -*-


class People:
    __name = 'furzoom'
    __age = 22
    gender = 'female'
    __country = 'China'

    def print_name(self):
        print(self.__name)

    def set_name(self, name):
        print(id(self.__name))
        self.__name = name
        print(id(self.__name))

    def set_gender(self, gender):
        self.gender = gender

    @classmethod
    def get_country(cls):
        return cls.__country

    @classmethod
    def set_country(cls, country):
        cls.__country = country

    def __str__(self):
        return self.__name + " " + str(self.__age) + " " + self.gender + " " \
               + self.__country


class UniversityMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Student(UniversityMember):
    def __init__(self, name, age, sno, mark):
        UniversityMember.__init__(self, name, age)
        self.sno = sno
        self.mark = mark

    def get_sno(self):
        return self.sno

    def get_mark(self):
        return self.mark


class Teacher(UniversityMember):
    def __init__(self, name, age, tno, salary):
        UniversityMember.__init__(self, name, age)
        self.tno = tno
        self.salary = salary

    def get_tno(self):
        return self.tno

    def get_salary(self):
        return self.salary


if __name__ == '__main__':
    def test1():
        p = People()
        print(p)
        p.set_name("mn")
        p.set_gender('male')
        p.set_country('USA')
        print(p)
        del p.gender
        print(p)

        q = People()
        print(q)

    def test2():
        st = Student('mn', 18, 110, 95)
        print(st.get_name(), st.get_age(), st.get_sno(), st.get_mark())
        teacher = Teacher('furzoom', 36, "001", 8888)
        print(teacher.get_name(), teacher.get_age(), teacher.get_tno(),
              teacher.get_salary())

    # test1()
    test2()
