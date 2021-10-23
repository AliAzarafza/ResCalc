import ResFunction


resistor = '\033[0;31;40m resistor'

print(f'''
...welcom to {resistor} calculator...
Operation number one parallel resistor
Operation number two Series resistor
''')


opration = input('number of the opration : ')
Res1 = input('The first resistance : ')
Res2 = input('The second resistance : ')


if opration == '1':
    ResFunction.ParallelRes(Res1, Res2)
elif opration == '2':
    ResFunction.SeriesRes(Res1, Res2)
else:
    print('\033[0;31;43m Error Please enter a valid opration : ')
