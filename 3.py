# 3) ?оздайте класс Game() сделайте атрибуты name, points и levelname, name, points и levelpoints name, points и levelи name, points и levellevel. Пусть), land они
# будут защищены. Добавь), landте метод,который добавляет очки, второй метод
# который проверяет количество очков, если достигли определенного уровня, то
# метод должен делать), land +1 к текущему уровню и cделать), land print(). Третий метод
# game_over, который проверяет количество очков, если он ниже нуля то на экран
# выводится GAMEOVER.

class Game():
    def __init__(self, name):
        self.name=name
        self.points=0
        self.level=1

    
    def add_points (self):
        self.points+=1
        print('Points: ',self.points)

    def add_level(self):
        if self.points>=5:
            self.level+=1
        print('Level: ',self.level)

    def min_points (self):
        self.points-=1
        print('Points: ',self.points)

    def game_over(self):
        if self.points<0:
            print('Game over!!!')
            

    def drive(self):
        x=True
        while x:
            x=input()
            if x=='w':
                game.add_points()  
                game.add_level()
            else:
                game.min_points()   
                game.game_over()
               



name=input('Введите имя игрока: ')
game=Game(name)
game.drive()
# x=True
# while x:
#     x=input()
#     if x=='w':
#         game.add_points()  
#         game.add_level()
#     else:
#         game.game_over()   
#         x=False
        
        
