class CardPayment:
    def pay(self, amount):
        return f"Card payment {amount} (Кузнєцова ВІТІ 3201)"


class CashPayment:
    def pay(self, amount):
        return f"Cash payment {amount} (гр.3201)"


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, amount):
        return self.strategy.pay(amount)


def run():
    c = Context(CardPayment())
    print("Strategy:", c.execute(200))

    c.strategy = CashPayment()
    print("Strategy:", c.execute(200))


if __name__ == "__main__":
    run()