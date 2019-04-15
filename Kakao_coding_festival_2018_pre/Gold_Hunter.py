# cf_2017
# cf_2018
def cf_2017(ranking):
    if ranking == 0 or (21 < ranking <= 100):
        return 0
    elif ranking == 1:
        return 5000000
    elif 2 <= ranking <= 3:
        return 3000000
    elif 4 <= ranking <= 6:
        return 2000000
    elif 7 <= ranking <= 10:
        return 500000
    elif 11 <= ranking <= 15:
        return 300000
    elif 15 < ranking <= 21:
        return 100000
    else:
        return 0
       
def cf_2018(ranking):
    if ranking == 0 or (31 < ranking <= 64):
        return 0
    elif ranking == 1:
        return 5120000
    elif 2 <= ranking <= 3:
        return 2560000
    elif 4 <= ranking <= 7:
        return 1280000
    elif 8 <= ranking <= 15:
        return 640000
    elif 16 <= ranking <= 31:
        return 320000
    else:
        return 0

trial = int(input())
alist = list()
blist = list()

# Input data
while trial > 0:
    a, b = input().split()
    alist.append(int(a))
    blist.append(int(b))
    trial -= 1

# Output data
for i in range(len(alist)):
    # print(cf_2017(alist[i]), cf_2018(blist[i]))
    print(cf_2017(alist[i])+cf_2018(blist[i]))
