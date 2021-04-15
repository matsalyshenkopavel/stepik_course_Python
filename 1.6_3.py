class LoggableList(list, Loggable):
    def append(self, element):
        super(LoggableList, self).append(element)
        self.log(element)