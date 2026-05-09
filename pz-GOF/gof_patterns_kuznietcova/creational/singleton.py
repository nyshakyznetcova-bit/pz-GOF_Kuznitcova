class Logger:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.owner = "Кузнєцова Т.Ю. | ВІТІ | гр.3201"
            cls._instance.logs = []
        return cls._instance

    def log(self, msg):
        self.logs.append(f"[{self.owner}] {msg}")

    def show(self):
        return self.logs


def run():
    l1 = Logger()
    l2 = Logger()

    l1.log("System start")
    l2.log("User login")

    print("Singleton logs:", l1.show())
    print("Same instance:", l1 is l2)