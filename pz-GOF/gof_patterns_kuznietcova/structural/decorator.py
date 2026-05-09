class Order:
    def cost(self):
        return 100


class VitiDiscount:
    def __init__(self, order):
        self.order = order

    def cost(self):
        return self.order.cost() * 0.85


def run():
    order = Order()
    order = VitiDiscount(order)

    print("Decorator (ВІТІ гр.3201):", order.cost())