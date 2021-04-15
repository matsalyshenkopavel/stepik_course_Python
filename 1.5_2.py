class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.current_seq = []

    def add(self, *a):
        # добавить следующую часть последовательности
        self.current_seq.extend(a)
        while len(self.current_seq) >= 5:
            print(sum(self.current_seq[:5]))
            del self.current_seq[:5]

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.current_seq