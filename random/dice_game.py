from hashlib import new
import random
class Dice:
    def roll(self):
        fn = random.randint(1,6)
        sn = random.randint(1,6)
        return fn,sn

mydice = Dice()
print(mydice.roll())