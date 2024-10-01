class SuperHero:
    people = 'people'

    #Инициализация
    def __init__(self, name, nickname, superpower, health_point, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_point
        self.catchphrase = catchphrase

    #Метод вывода имени супергероя
    def super_name(self):
        return self.name

    #Метод увеличения здоровья героя в два раза
    def double_HP(self):
        self.health_point *= 2
        return self.health_point

    #Магический метод, который выводит прозвище героя, его суперспособность и здоровье
    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health: {self.health_point}"

    #Магический метод расчета длины коронной фразы героя
    def __len__(self):
        return len(self.catchphrase)

#Создание экземпляра
new_hero = SuperHero('Batman', 'Batty', 'Money', 147, 'I`m Batman!')

#Вызов всех методов
print(new_hero.super_name())
print(new_hero.double_HP())
print(new_hero)
print(len(new_hero))
