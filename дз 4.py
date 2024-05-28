# class GeeksPeople:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def __str__(self):
#         return f"{self.name}, {self.email}, {self.phone}"
 

# geekspeople = GeeksPeople("Paiper", "promenad@email.com", "35523534")
# print(geekspeople)


# class Student(GeeksPeople):
#     def __init__(self, name, email, phone, group_where_study):
#         GeeksPeople.__init__(self, name, email, phone)
#         self.group_where_study = group_where_study

#     def study(self):
#         print(f"{self.name}- учиться в группе {self.group_where_study}")

# student = Student("Kit", "big@gmail.com","645663674573", "15 1b")
# student.study()
# print(student)

# class Teacher(GeeksPeople):
#     def __init__(self, name, email, phone, group_where_teach):
#         GeeksPeople.__init__(self, name, email, phone)
#         self.group_where_teach = group_where_teach


#     def teach(self):
#         print(f"{self.name}- преподаёт в группе {self.group_where_teach}")

# teacher = Teacher("Наталия Ивановна", "hfgd@gmail.com", "343535455", "15 1b")
# teacher.teach()
# print(teacher)


# class Admin(GeeksPeople):
#     def __init__(self, name, email, phone, admin_ip):
#         GeeksPeople.__init__(self, name, email, phone)
#         self.admin_ip = admin_ip

#     def create(self):
#         print(f"{self.name}- создаёт группу {self.admin_ip}")


# admin = Admin("8-bit", "rfrf@gmail.com", "34542365", "18 2t")
# admin.create()
# print(admin)


# class Mentor(Teacher, Student):
#     def __init__(self, name, email, phone, group_where_teach, group_where_study):
#         Teacher.__init__(self, name, email, phone, group_where_teach)
#         Student.__init__(self, name, email, phone, group_where_study)

    

# mentor = Mentor("mortis", "dggre@gmail", "452346", "12 2t", "15 1b")
# mentor.study()   
# mentor.teach()
# print(mentor)