#Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
#Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
#не изменяя существующий код бойцов или механизм боя.

#- Есть класс `Fighter`, представляющий бойца.
#- Есть класс `Monster`, представляющий монстра.
#- Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
#Шаг 1:Создайте абстрактный класс для оружия
#- Создайте абстрактный класс `Weapon`, который будет содержать абстрактный метод `attack()`.
#Шаг 2: Реализуйте конкретные типы оружия
#- Создайте несколько классов, унаследованных от `Weapon`, например, `Sword` и `Bow`. Каждый из этих классов реализует
#метод `attack()` своим уникальным способом.
#Шаг 3: Модифицируйте класс `Fighter`
#- Добавьте в класс `Fighter` поле, которое будет хранить объект класса `Weapon`.
#- Добавьте метод `changeWeapon()`, который позволяет изменить оружие бойца.
#Шаг 4: Реализация боя
#- Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.

#Требования к заданию:
#- Код должен быть написан на Python.
#- Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять,
#не изменяя существующие классы бойцов и механизм боя.
#- Программа должна выводить результат боя в консоль.

#Пример результата:
#Боец выбирает меч. Боец наносит удар мечом. Монстр побежден! Боец выбирает лук. Боец наносит удар из лука. Монстр побежден!

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом")

class Bow(Weapon):
    def attack(self):
        print("Боец наносит выстрел из лука")

class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        print(self.weapon.attack())

def Monster():
    pass

sword1 = Sword()
bow1 = Bow()

fighter = Fighter(sword1)
fighter.fight()
fighter.changeWeapon(bow1)
fighter.fight()