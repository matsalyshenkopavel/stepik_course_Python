class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.current = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if v + self.current <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.current += v