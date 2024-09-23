class Computer:
    def __init__(self):
        self._maxprice = 900
    def sell(self):
        print("selling Price: {:.2f}".format(self._maxprice))
    def setMaxPrice(self, price):
        self._maxprice = price
c =Computer()
c.sell()
c._maxPrice = 1000
c.sell()