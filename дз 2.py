# class Person:#1
#     def __init__(self, fullname, age, is_married):
#         self.fillname = fullname
#         self.age = age
#         self.is_married = is_married

#     def info(self):
#         print(f" {self.fillname}, {self.age}, {self.is_married}")

# person = Person("Али", "13", " не Женат")
# person.info()

# class Person:#2
#     def __init__(self, fullname, age, is_married, introduce_mayself):
#         self.introduce_mayself = introduce_mayself
#         self.fillname = fullname
#         self.age = age
#         self.is_married = is_married
        

#     def info(self):
#         print(f"{self.fillname}, {self.age}, {self.is_married}, {self.introduce_mayself}")

# person = Person("меня зовут", "Али", "мне 13 лет", "я не Женат")
# person.info()


# class Teacher(Person):#3
#     def __init__(self, fillname, age, is_married, experience):
#         super().__init__(fillname, age, is_married, experience)
#         self.experience = experience

#     def info(self):
#         print(f"имя - {self.fillname}, возраст - {self.age}, не женат - {self.is_married}, опытный - {self.experience}")

# teacher = Teacher("Али", "13", "нет", "Майнкрафтер")
# teacher.info()