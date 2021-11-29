class operation:
    key = ''
    value = ''
    order = 0
    loop = 1

    def __init__(self):
        pass

    def __init__(self, order):
        self.order = order

    def __init__(self, key, order):
        self.key = key
        self.order = order

    def __init__(self, key, order, loop):
        self.key = key
        self.order = order
        self.loop = loop
