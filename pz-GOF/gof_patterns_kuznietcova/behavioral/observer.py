class Subscriber:
    def update(self, msg):
        print(f"[ВІТІ | гр.3201] Notification:", msg)


class News:
    def __init__(self):
        self.subs = []

    def add(self, s):
        self.subs.append(s)

    def notify(self, msg):
        for s in self.subs:
            s.update(msg)


def run():
    news = News()
    news.add(Subscriber())

    news.notify("System update by Kuznietсova T.Y.")


if __name__ == "__main__":
    run()
