import ResFunction
import argparse
import os

# parser = argparse.ArgumentParser()
# parser.add_argument()

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()


resistor = '\033[0;31;40m resistor\033[0;37;40m'

print(f'''
    ...welcom to{resistor} calculator...
    Operation number one parallel resistor [1]
    Operation number two Series resistor [2]
    Operation number tree for Star to triangle [3]
    Operation number four for triangle to star [4]
''')


opration = input('\033[0;34;40m number of the opration : ')


if opration == '1':
    Res1 = input('\033[0;36;40m The first resistance : \033[0;37;40m')
    Res2 = input('\033[0;36;40m The second resistance : \033[0;37;40m')
    ResFunction.ParallelRes(float(Res1), float(Res2))
elif opration == '2':
    Res1 = input('\033[0;36;40m The first resistance : \033[0;37;40m')
    Res2 = input('\033[0;36;40m The second resistance : \033[0;37;40m')
    ResFunction.SeriesRes(float(Res1), float(Res2))
elif opration == '3':
    R1 = input('\033[0;36;40m The R1 value : \033[0;37;40m')
    R2 = input('\033[0;36;40m The R2 value : \033[0;37;40m')
    R3 = input('\033[0;36;40m The R3 value : \033[0;37;40m')
    ResFunction.Star2Tra(float(R1),float(R2),float(R3))
elif opration == '4':
    RA = input('\033[0;36;40m The RA value : \033[0;37;40m')
    RB = input('\033[0;36;40m The RB value : \033[0;37;40m')
    RC = input('\033[0;36;40m The RC value : \033[0;37;40m')
    ResFunction.Tar2Star(float(RA),float(RB),float(RC))
else:
    print('\033[0;31;43m Error Please enter a valid opration (1 or 2) \033[0;37;40m')


print('\033[0;36;40m Credit : Ali Azarafza \033[0;37;40m')
