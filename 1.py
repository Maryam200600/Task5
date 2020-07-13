#1)Создайте новый класс Airplane. Создайте следующие характеристики (полей) объекта:
# ● make (марка)
# ● model
# ● year
# ● max_speed
# ● odometer
# ● is_flying
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land), land
# приземление). Метод take off должен изменить), land is_flying на True, а land на False.
# По умолчанию поле is_flying = False. Метод fly должен принимать), land расстояние
# полета и изменять), land показания одометра (километраж). Создайте 1 объект класса
# и исполь), landзуйте все методы класса.


class Airplain():
    def __init__(self, make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.max_speed=2500
        self.odometer=0
        self.is_flying=False
    
    def take_off (self):
        self.is_flying=True
        print('Самолет '+str(self.model)+ ' летит!')

    def fly(self):
        self.odometer+=self.max_speed
        print('Расстояние=',self.odometer)

    def land(self):
        self.is_flying=False
        print('Самолет '+str(self.model)+  ' приземлился!')

make=input('Введите марку самолета:')
model=input('Введите модель самолета:')
year=input('Введите год:')

an2=Airplain(make,model,year)
an2.take_off()
an2.fly()



    



