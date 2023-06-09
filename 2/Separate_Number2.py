"""
もうめんどくせえから、前から数字を取り出していって、
前回までの数字と照合して一致したらアウトのプログラム作る
深さ優先探索をおこっている
リストの最後の数字が一個の時は二個の参照はできない
リストの外に出る＝エラーのはず
２個の参照はできないようにしよう
次に参照する位置とリストの最後が一致すれば、一文字しか参照できない
もしくはリストの長さが98なら強制的に次の文字をリストに加える
"""
import sys
import resource
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

def separate_list(input,pos,flist):  # inputは入力する数列。posは見る位置。listは答えの候補を格納するもの
    if len(flist) == 99:
        print(flist)
        exit()

    if input[pos+1] != 0:
        N_n1 = input[pos] # next number
        if N_n1 not in flist: # 次に参照する数字が今まで格納した数字に含まれない
            print(N_n1,flist)
            flist.append(N_n1) # リストに数字を格納
            separate_list(input,pos+1,flist) # 次の再帰を実行
 
    if input[pos] == input[-1]:
        separate_list(input,pos+1,flist)

    if input[pos+2] != 0:
        N_n2 = ''.join(input[pos:pos+2])
        if N_n2 not in flist:
            print(N_n2,flist)
            flist.append(N_n2)
            separate_list(input,pos+2,flist)

    # 再帰処理どこにつっこもう？
    # separate_list(input,pos+1,list)
    # separate_list(input,pos+2,list)

ini_pos = 0
ini_list = []
# input.txtの中身を代入
input1 = list('268668743807663281359259975924239968838915518781704591221216502144648297573337534154488714432458672010933572906012936272617155562367959865483138529186273117849466634478519408432309577699417')
input2 = list('588023054721923746425265568413319111288895673218269337846703893426741109162458758615749854723538315243686597944776663689752292218713274605143653928349848950941735964090312799751676207148195')
input3 = list('773181522128748272298129793949024594941105042259227704876614744625899327316561366965719566235587963422604546861151544329262033575401768805730883919989518388467631485645315837491733787983136')

separate_list(input1, ini_pos, ini_list)

ini_pos = 0
ini_list = []

"""
separate_list(input2, ini_pos, ini_list)

ini_pos = 0
ini_list = []

separate_list(input3, ini_pos, ini_list)
"""