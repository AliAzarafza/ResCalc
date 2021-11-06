
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
    RA = truncate((p1 / R1), 4)
    RB = truncate((p1 / R2), 4)
    RC = truncate((p1 / R3), 4)
    print(f'\033[0;34;47mthe\033[0;31;47m RA \033[0;34;47mvalue is equal to = {RA}\033[0;34;40m\n\033[0;34;47mthe\033[0;31;47m RB \033[0;34;47mvalue is equal to = {RB}\033[0;34;40m\n\033[0;34;47mthe\033[0;31;47m RC \033[0;34;47mvalue is equal to = {RC}\033[0;34;40m')

def Tar2Star(RA,RC,RB):
    R1 = truncate(((RB*RC)/(RA+RB+RC)), 4)
    R2 = truncate(((RA*RC)/(RA+RB+RC)), 4)
    R3 = truncate(((RA*RB)/(RA+RB+RC)), 4)
    print(f'\033[0;34;47mthe\033[0;31;47m R1 \033[0;34;47mvalue is equal to = {R1}\033[0;34;40m\n\033[0;34;47mthe\033[0;31;47m R2 \033[0;34;47mvalue is equal to = {R2}\033[0;34;40m\n\033[0;34;47mthe\033[0;31;47m R3 \033[0;34;47mvalue is equal to = {R3}\033[0;34;40m')
