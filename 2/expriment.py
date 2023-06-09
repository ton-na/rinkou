# 深さ優先探索
def dfs(i, s):
    # 全ての文字を使い切ったら結果を出力
    if i == len(S):
        ans.append(tuple(s))
        return ans # ここでansを返す
    # メモ化チェック
    if (i, tuple(s)) in memo:
        ans.extend(memo[(i, tuple(s))])
        return ans # ここでansを返す
    # 1桁の数を追加（0でなければ）
    if S[i] != "0":
        # 重複チェック
        if int(S[i]) not in s:
            dfs(i + 1, s + [int(S[i])])
    # 2桁の数を追加（可能かつ0で始まらなければ）
    if i < len(S) - 1 and S[i] != "0":
        # 重複チェック
        if int(S[i:i+2]) not in s:
            dfs(i + 2, s + [int(S[i:i+2])])
    # メモ化更新
    memo[(i, tuple(s))] = list(ans)

# 入力
S = "773181522128748272298129793949024594941105042259227704876614744625899327316561366965719566235587963422604546861151544329262033575401768805730883919989518388467631485645315837491733787983136"

# 数分解の結果を格納するリスト
ans = []

# メモ化用の辞書
memo = {}

# 最初の呼び出し
result = dfs(0, []) # ここでresultに結果を代入

# 結果の表示ではなく、リストとして扱う
print(result[0]) # 最初の要素を表示
print(result[-1]) # 最後の要素を表示

