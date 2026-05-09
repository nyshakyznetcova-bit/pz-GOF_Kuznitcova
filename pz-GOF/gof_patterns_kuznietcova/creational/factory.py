class User:
    def role(self):
        pass


class Admin(User):
    def role(self):
        return "Admin (ВІТІ | Кузнєцова Т.Ю. | гр.3201)"


class Guest(User):
    def role(self):
        return "Guest (ВІТІ | гр.3201)"


class UserFactory:
    @staticmethod
    def create(user_type):
        if user_type == "admin":
            return Admin()
        return Guest()


def run():
    user = UserFactory.create("admin")
    print("Factory:", user.role())
class Test:
    pass

def run():
    print("FACTORY WORKS!!!")

if __name__ == "__main__":
    run()