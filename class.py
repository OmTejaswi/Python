class pri:
    # Constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y
         
    # class function
    def pmove(self):
        print("move")
    def pdraw(self):
        print("draw")

# prin1 varible
prin1 = pri(20,30)
prin1.pdraw()
prin1.pmove()
prin1.x = 10
prin1.y = 20
print(prin1.x, prin1.y)

# prin2 variable
prin2 = pri(10,20)
print(prin2.x)