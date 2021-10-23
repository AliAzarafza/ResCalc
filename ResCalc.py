import ResFunction


resistor = '\033[0;31;40m resistor'

print(f'''
...welcom to{resistor}\033[0;37;40m calculator...
Operation number one parallel resistor *1*
Operation number two Series resistor *2*
''')


opration = input('\033[0;34;40m number of the opration : ')
Res1 = input('\033[0;36;40m The first resistance : ')
Res2 = input('\033[0;36;40m The second resistance : ')


if opration == '1':
    ResFunction.ParallelRes(int(Res1), int(Res2))
elif opration == '2':
    ResFunction.SeriesRes(int(Res1), int(Res2))
else:
    print('\033[0;31;43m Error Please enter a valid opration (1 or 2)')
