
def ParallelRes(res1,res2):
    resv = (res1 * res2) / (res1 + res2)
    print(f'\033[0;36;42m The resistance value is equal to = {resv}')


def SeriesRes(res1,res2):
    resv = res1 + res2
    print(f'\033[0;36;42m The resistance value is equal to = {resv}')

