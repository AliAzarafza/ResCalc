
from os import truncate

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)


def ParallelRes(res1,res2):
    resv = ((res1 * res2) / (res1 + res2))
    resv = truncate(resv, 4)
    print(f'\033[0;34;47m The \033[0;31;47mresistance\033[0;34;47m value is equal to = {resv} \033[0;34;40m')


def SeriesRes(res1,res2):
    resv = (res1 + res2)
    resv = truncate(resv, 4)
    print(f'\033[0;34;47m The \033[0;31;47mresistance\033[0;34;47m value is equal to = {resv} \033[0;34;40m')

def Star2Tra(R1,R2,R3):
    p1 = (R1*R2+R1*R3+R2*R3)
    RA = p1 / R1
    RA = truncate(RA, 4)
    print(f'\033[0;34;47m The \033[0;31;47mresistance\033[0;34;47m value is equal to = {RA} \033[0;34;40m')