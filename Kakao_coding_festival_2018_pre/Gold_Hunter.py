# cf_2017
# cf_2018
def cf_2017(ranking):
    if ranking == 0 or (ranking > 21 and ranking <= 100):
        return 0
    elif ranking == 1:
        return 5000000
    elif ranking >= 2 and ranking <= 3:
        return 3000000
    elif ranking >= 4 and ranking <= 6:
        return 2000000
    elif ranking >= 7 and ranking <= 10:
        return 500000
    elif ranking >= 11 and ranking <= 15:
        return 300000
    elif ranking > 15 and ranking <= 21:
        return 100000
    else:
        return 0
       
def cf_2018(ranking):
    if ranking == 0 or (ranking > 31 and ranking <= 64):
        return 0
    elif ranking == 1:
        return 5120000
    elif ranking >= 2 and ranking <= 3:
        return 2560000
    elif ranking >= 4 and ranking <= 7:
        return 1280000
    elif ranking >= 8 and ranking <= 15:
        return 640000
    elif ranking >= 16 and ranking <= 31:
        return 320000
    else:
        return 0

trial = int(input())
alist = list()
blist = list()

while trial > 0:
    a, b = input().split()
    alist.append(int(a))
    blist.append(int(b))
    trial -= 1

# print("\nResult\n")
for i in range(len(alist)):
    # print(cf_2017(alist[i]), cf_2018(blist[i]))
    print(cf_2017(alist[i])+cf_2018(blist[i]))
