print("Мы рады приветствовать всех на проектt «Ваш сад и дача»")

class Tomato:

    # Стадии созревания помидора
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Переход к следующей стадии созревания
    def grow(self):
        self._change_state()

    # Проверка, созрел ли томат
    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    # Защищенные(protected) методы

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Gardener finished')

    # Собираем урожай
    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early! Your plant is green and not ripe.')

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''Наш портал будет полезен садоводам-любителям и всем тем, кто интересуется вопросами в садоводстве и строительстве дачи. Он создан профессионалами в садоводстве и постоянно пополняется новыми статьями и сервисами.

На нашем сайте вы получите информацию о сортах плодовых деревьев и ягодных кустарниках, изучите информацию по посадке и защите сада, научитесь обрезать деревья. Специально в помощь начинающим садоводам на портале создан словарь терминов, библиотека и раздел полезная информация. Большое значение мы придаем развитию каталога товаров и услуг для сада и дачи - Садовники Маркет, где отображены товары и услуги для владельцев загородных домов.

Строительные калькуляторы.

В настоящем проекте обобщены вопросы, с которыми приходится сталкиваться садоводам-любителям, а также будут даны практические рекомендации с учетом достижений науки и практического опыта.

Миссия портала «Ваш сад и дача» – содействие правильному выращиванию и уходу за плодовыми деревьями на приусадебном участке. Предоставление полезной информации для садоводов и дачников, информация о товарах и услугах для сада и строительства дачи.''')


# Тесты
if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()