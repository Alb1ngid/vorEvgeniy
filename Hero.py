class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_point, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_point
        self.catchphrase = catchphrase

    def super_name(self):
        return self.name

    def double_HP(self):
        self.health_point *= 2
        return self.health_point

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health: {self.health_point}"

    def __len__(self):
        return len(self.catchphrase)

new_hero = SuperHero('Batman', 'Batty', 'Money', 147, 'I`m Batman!')

print(new_hero.super_name())
print(new_hero.double_HP())
print(new_hero)
print(len(new_hero))
