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
        return "True in the True_phrase"

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

# Создание экземпляров героев
fire_hero = Fire('FireMan', 'Blaze', 'Fire Manipulation', 100, 'Burn them all!', 50)
water_hero = Water('WaterMan', 'Splash', 'Water Control', 120, 'Feel the wave!', 40)

# Вызов методов для каждого героя
print(fire_hero.super_name())
print(fire_hero.square_HP())  # Возведение здоровья в квадрат и изменение fly
print(fire_hero)
print(fire_hero.true_phrase())  # Вызов метода с фразой
print(len(fire_hero))

print(water_hero.super_name())
print(water_hero.square_HP())  # Возведение здоровья в квадрат и изменение fly
print(water_hero)
print(water_hero.true_phrase())  # Вызов метода с фразой
print(len(water_hero))
