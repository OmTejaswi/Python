class main:
     def walk(self):
         print("walking")

class dog(main):
    def bark(self):
        print("barking")
    # if we write nothing under class when it is combined to parent class the we will write "pass" simply
    # pass

class cat(main):
    def meww(self):
        print("meww...")
    # if we write nothing under class when it is combined to parent class the we will write "pass" simply
    # pass

mydog = dog()
mydog.walk()
mydog.bark()

mycat = cat()
mycat.walk()
mycat.meww()