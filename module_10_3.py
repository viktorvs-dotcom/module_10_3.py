from threading import Thread, Lock
from random import randint
from time import sleep


class Bank(Thread):
    lock = Lock()

    def __init__(self):
        super().__init__()
        self.balance = 100
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            with self.lock:
                cash = randint(50, 500)
                self.balance += cash
                print(f"Пополнение на: {cash}. Текущий баланс{self.balance}")
            if self.balance <= 500:
                sleep(0.001)

    def take(self):
        for i in range(5):
            with self.lock:
                cash = randint(50, 500)
                print(f"Запрос на снятие {cash}")
                if self.balance >= cash:
                    self.balance -= cash
                    print(f"Снятие: {cash} запрос выполнен. Баланс:{self.balance}")
                else:
                    print(f"Запрос откланён, недостаточно средств")


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
