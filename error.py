def catch():
    try:
        age = int(input("Age: "))
        print(age)
    except ZeroDivisionError:
        print('Age cannot be 0 (zero)')
        catch()
    except ValueError:
        print("Invalid Value")
        catch()

catch()