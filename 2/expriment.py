import sys
import resource
sys.setrecursionlimit(10 ** 9)
print(sys.getrecursionlimit())
# 入力
S = "268668743807663281359259975924239968838915518781704591221216502144648297573337534154488714432458672010933572906012936272617155562367959865483138529186273117849466634478519408432309577699417"

# 数分解の結果を格納するリスト
ans = []

# 深さ優先探索
def dfs(i, s):
    # 全ての文字を使い切ったら結果を出力
    if i == len(S):
        ans.append(s)
        return
    # 1桁の数を追加
    if S[i] not in ans:
        dfs(i + 1, s + " " + S[i])
    # 2桁の数を追加（可能なら）
    if S[i:i+2] not in ans:
        if i < len(S) - 1 and S[i] != "0":
            dfs(i + 2, s + " " + S[i:i+2])

# 最初の呼び出し
dfs(0, "")

# 結果の表示
for a in ans:
    print(a.strip())
