
class Observer:
    def update(self, subject):
        pass


class SmsNotifier(Observer):
    def update(self, subject):
        print(f"SMS-> к нам присоединился {subject[-1].name}")


class EmailNotifier(Observer):
    def update(self, subject):
        print(f"EMAIL-> к нам присоединился {subject[-1].name}")
