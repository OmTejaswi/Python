weight = input('Weight: ')
if weight != '' and type(int(weight)) is int :
    unit = input("Which value you have given? (L)bs or (K)g: ")
    if unit.upper() == 'K':
        newweight = int(weight) * 2.205
        print(str(newweight) + ' pound')
    elif unit.upper() == 'L':
        newweight = int(weight) / 2.205
        print(str(newweight) + 'kg')
elif weight == '' or type(weight) is str == False:
    print('Please Enter A Valid Value')
