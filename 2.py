# 2)cоздайте класс с именем User. Создайте два атрибута first_name и last_name, а
# затем еще несколь), landко атрибутов, которые обычно хранятся в профиле
# поль), landзователя. Напишите метод describe_user(), который выводит сводку с
# информацией о поль), landзователе. Создайте еще один метод greet_user() для вывода
# персональ), landного приветствия для поль), landзователя.

class User1():
    def __init__(self, first_name,last_name,year_of_birth,fam_status,pol):
        self.first_name=first_name
        self.last_name=last_name
        self.year_of_birth=year_of_birth
        self.fam_status=fam_status
        self.pol=pol
    
    def describe_user (self):

        print('Имя: '+self.first_name)
        print('Фамилия: '+self.last_name)
        print('Год рождения: '+str(self.year_of_birth))
        print('Семейное положение: '+self.fam_status)
        print('Пол: '+self.pol)
    def  greet_user(self):
            print('Здравствуйте, '+self.first_name+' '+self.last_name+' рады вас видеть!')

Mari=User1('Maryam','Muhamedjanova',2000,'not married','girl')
Mari.describe_user()
Mari.greet_user()