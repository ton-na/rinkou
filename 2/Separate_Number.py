def separete10x(input): # 10の倍数の位置を探し出す
    list1 = input1
    left10x = [] # inputのうち10の倍数の位置を格納。二桁の数10xの1の位置を格納。
    right10x = [] # inputのうち10の倍数の位置を格納。10xの0の位置を格納
    exf0 = [] # inputのうち10xと10x'の間の数字 except for 0
    right10x = [i for i, x in enumerate(list1) if x == '0']

    # 10xと10xの間の数字を格納
    frag1 = 0 # exf0
    for i in range(9):
        left10x.append(right10x[i]-1) # 10xの左側の数字を格納
        if frag1 == 0:
            exf0.append(list1[0:left10x[i]])
            frag1 = 1
        else:
            exf0.append(list1[right10x[i-1]+1:left10x[i]])
    exf0.append(list1[right10x[8]+1:200])
    return exf0, left10x, right10x

def judge2x(list): # 偶数奇数判定
    result = []
    for i in range(len(list)):
        if not list[i]:
            result.append(-1)
        else:
            if int(list[i]) % 2 == 0:
                result.append(0)
            else:
                result.append(1)
    return result
    

input1 = list('268668743807663281359259975924239968838915518781704591221216502144648297573337534154488714432458672010933572906012936272617155562367959865483138529186273117849466634478519408432309577699417')
input2 = list('588023054721923746425265568413319111288895673218269337846703893426741109162458758615749854723538315243686597944776663689752292218713274605143653928349848950941735964090312799751676207148195')
input3 = list('773181522128748272298129793949024594941105042259227704876614744625899327316561366965719566235587963422604546861151544329262033575401768805730883919989518388467631485645315837491733787983136')

# 10の倍数とそれ以外を分けている
x, y, z = separete10x(input1)
L_s = [ ''.join(x[i]) for i in range(len(x))] # separate list

L_j = judge2x(L_s) # judge list even or odd

print(x,L_s,L_j)