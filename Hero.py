class SuperHero:
    people = 'people'

    #Инициализация
    def __init__(self, name, nickname, superpower, health_point, catchphrase, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_point
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = False

    #Метод вывода имени супергероя
    def super_name(self):
        return self.name

    #Метод увеличения здоровья героя в два раза
    def double_HP(self):
        self.health_point *= 2
        return self.health_point

    #Магический метод, который выводит прозвище героя, его суперспособность и здоровье
    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health: {self.health_point}, Damage: {self.damage}"

    #Магический метод расчета длины коронной фразы героя
    def __len__(self):
        return len(self.catchphrase)

# Класс огненного героя (наследуется от SuperHero)
class Fire(SuperHero):
    def __init__(self, name, nickname, superpower, health_point, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_point, catchphrase, damage)
        self.fly = True  # Огненный герой может летать

    # Переопределение метода увеличения здоровья
    def double_HP(self):
        self.health_point *= 3  # Увеличивает здоровье в 3 раза вместо 2
        return self.health_point

    # Переопределение магического метода
    def __str__(self):
        return f"Fire Hero - {super().__str__()}"

class Water(SuperHero):
    def __init__(self, name, nickname, superpower, health_point, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_point, catchphrase, damage)
        self.fly = False

    def double_HP(self):
        self.health_point += 1.5
        return self.health_point

    def __str__(self):
        return f"Water hero - {super().__str__()}"


#Создание экземпляра
new_hero = SuperHero('Batman', 'Batty', 'Money', 147, 'I`m Batman!')
# Создание экземпляров героев
fire_hero = Fire('FireMan', 'Blaze', 'Fire Manipulation', 100, 'Burn them all!', 50)
water_hero = Water('WaterMan', 'Splash', 'Water Control', 120, 'Feel the wave!', 40)

#Вызов всех методов
print(new_hero.super_name())
print(new_hero.double_HP())
print(new_hero)
print(len(new_hero))

# Вызов всех методов для каждого героя
print(fire_hero.super_name())
print(fire_hero.double_HP())
print(fire_hero)
print(len(fire_hero))

print(water_hero.super_name())
print(water_hero.double_HP())
print(water_hero)
print(len(water_hero))
