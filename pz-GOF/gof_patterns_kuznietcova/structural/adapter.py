class OldSystem:
    def request(self):
        return "Old system (ВІТІ 3201)"


class Adapter:
    def __init__(self, old):
        self.old = old

    def request(self):
        return "Adapter → " + self.old.request()


def run():
    old = OldSystem()
    adapted = Adapter(old)
    print("Adapter:", adapted.request())