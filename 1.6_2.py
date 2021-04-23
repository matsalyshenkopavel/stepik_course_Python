"""Реализуйте структуру данных, представляющую собой расширенную структуру стек.
Необходимо поддерживать добавление элемента на вершину стека, удаление с вершины стека,
и необходимо поддерживать операции сложения, вычитания, умножения и целочисленного деления.

Операция сложения на стеке определяется следующим образом. Со стека снимается верхний элемент (top1),
затем снимается следующий верхний элемент (top2),
и затем как результат операции сложения на вершину стека кладется элемент, равный top1 + top2.

Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2) и целочисленного деления (top1 // top2).

Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list."""

class ExtendedStack(list):
    def sum(self):
        # операция сложения
        element1 = super(ExtendedStack, self).pop()
        element2 = super(ExtendedStack, self).pop()
        newTop = element1 + element2
        super(ExtendedStack, self).append(newTop)

    def sub(self):
        # операция вычитания
        element1 = super(ExtendedStack, self).pop()
        element2 = super(ExtendedStack, self).pop()
        newTop = element1 - element2
        super(ExtendedStack, self).append(newTop)

    def mul(self):
        # операция умножения
        element1 = super(ExtendedStack, self).pop()
        element2 = super(ExtendedStack, self).pop()
        newTop = element1 * element2
        super(ExtendedStack, self).append(newTop)

    def div(self):
        # операция целочисленного деления
        element1 = super(ExtendedStack, self).pop()
        element2 = super(ExtendedStack, self).pop()
        newTop = element1 // element2
        super(ExtendedStack, self).append(newTop)