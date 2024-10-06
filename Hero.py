class SuperHero:
    people = 'people'

    # Инициализация
    def __init__(self, name, nickname, superpower, health_point, catchphrase, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_point
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = False  # Добавляем свойство fly по умолчанию

    # Метод вывода имени супергероя
    def super_name(self):
        return self.name

    # Метод возведения здоровья героя в квадрат и изменение fly на True
    def square_HP(self):
        self.health_point **= 2  # Возводим здоровье в квадрат
        self.fly = True  # Меняем значение fly на True
        return self.health_point

    # Новый метод, выводящий фразу
    def true_phrase(self):
        return f"True in the {self.catchphrase}"

    # Магический метод, который выводит прозвище героя, его суперспособность и здоровье
    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health: {self.health_point}, Damage: {self.damage}, Fly: {self.fly}"

    # Магический метод расчета длины коронной фразы героя
    def __len__(self):
        return len(self.catchphrase)


# Класс огненного героя (наследуется от SuperHero)
class Fire(SuperHero):
    def __init__(self, name, nickname, superpower, health_point, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_point, catchphrase, damage)

    # Переопределение магического метода __str__
    def __str__(self):
        return f"Fire Hero - {super().__str__()}"

# Класс водного героя (наследуется от SuperHero)
class Water(SuperHero):
    def __init__(self, name, nickname, superpower, health_point, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_point, catchphrase, damage)

    # Переопределение магического метода __str__
    def __str__(self):
        return f"Water Hero - {super().__str__()}"


# Класс злодея (наследуется от SuperHero)
class Villian(SuperHero):
    people = "monster"  # Меняем значение на monster

    def __init__(self, name, nickname, superpower, health_point, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_point, catchphrase, damage)

    # Переопределение магического метода __str__
    def __str__(self):
        return f"Mega Monster - {super().__str__()}"

    # Метод gen_x пока ничего не делает
    def gen_x(self):
        pass

    # Метод crit, который возводит урон в степень
    def crit(self):
        self.damage **= 2
        return self.damage


# Создание экземпляров героев
fire_hero = Fire('FireMan', 'Blaze', 'Fire Manipulation', 100, 'Burn them all!', 50)
water_hero = Water('WaterMan', 'Splash', 'Water Control', 120, 'Feel the wave!', 40)

# Создание экземпляра злодея
villain = Villian('DoomLord', 'Doom', 'Darkness Control', 200, 'Fear the dark!', 60)

# Вызов методов для злодея
print(villain.super_name())
print(villain.square_HP())  # Возведение здоровья в квадрат и изменение fly
print(villain)
print(villain.true_phrase())  # Вызов метода с фразой
print(len(villain))

# Применение метода crit к злодею и вывод нового значения damage
print(f"Damage before crit: {villain.damage}")
villain.crit()
print(f"Damage after crit: {villain.damage}")

# Применение метода crit для героя с аргументом damage (например, для fire_hero)
print(f"Fire hero damage before crit: {fire_hero.damage}")
fire_hero.damage = villain.crit()  # Применяем метод crit к fire_hero
print(f"Fire hero damage after crit: {fire_hero.damage}")
