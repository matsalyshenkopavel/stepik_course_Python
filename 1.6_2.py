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