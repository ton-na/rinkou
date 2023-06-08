"""
もうめんどくせえから、前から数字を取り出していって、
前回までの数字と照合して一致したらアウトのプログラム作る
"""
def separate_list(input,pos,list):  # inputは入力する数列。posは見る位置。listは答えの候補を格納するもの
    if len(list) == 99:
        print(list)
    
    N_n = input[pos] # next number
    if N_n not in list:
        list.append(input[pos])
        separate_list(input,pos+1,list)

    """
    リストの最後の数字が一個の時は二個の参照はできない
    リストの外に出た判定がよくわからんから、listの長さを測って98文字だったら、
    ２個の参照はできないようにしよう
    """
    if len(list) == 98:
        separate_list(input,pos+1,list)
        
    N_n = ''.join(input[pos:pos+2])
    if N_n not in list:
        list.append(''.join(input[pos:pos+2]))
        separate_list(input,pos+2,list)

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