
from os import truncate

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)


def ParallelRes(res1,res2):
    resv = ((res1 * res2) / (res1 + res2))
    resv = truncate(resv, 4)
    print(f'\033[0;34;47m The resistance value is equal to = {resv} \033[0;34;40m')


def SeriesRes(res1,res2):
    resv = (res1 + res2)
    resv = truncate(resv, 4)
    print(f'\033[0;34;47m The resistance value is equal to = {resv} \033[0;34;40m')

