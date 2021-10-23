
def ParallelRes(res1,res2):
    resv = ((res1 * res2) / (res1 + res2))
    print(f'\033[0;34;47m The resistance value is equal to = {resv} \033[0;34;40m')


def SeriesRes(res1,res2):
    resv = (res1 + res2)
    print(f'\033[0;34;47m The resistance value is equal to = {resv} \033[0;34;40m')

