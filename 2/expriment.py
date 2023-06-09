# 入力
S = "1718110212314413155616720819911"

# 数分解の結果を格納するリスト
ans = []

# メモ化用の辞書
memo = {}

# 深さ優先探索
def dfs(i, s):
    # 全ての文字を使い切ったら結果を出力
    if i == len(S):
        ans.append(tuple(s))
        return
    # メモ化チェック
    if (i, tuple(s)) in memo:
        ans.extend(memo[(i, tuple(s))])
        return
    # 1桁の数を追加（0でなければ）
    if S[i] != "0":
        # 重複チェック
        if int(S[i]) not in s:
            dfs(i + 1, s + [int(S[i])])
    # 2桁の数を追加（可能かつ0で始まらなければ）
    if i < len(S) - 1 and S[i] != "0" and int(S[i:i+2]) <= 20:
        # 重複チェック
        if int(S[i:i+2]) not in s:
            dfs(i + 2, s + [int(S[i:i+2])])
    # メモ化更新
    memo[(i, tuple(s))] = list(ans)

# 最初の呼び出し
dfs(0, [])

# 結果の表示
for a in ans:
    print(" ".join(map(str, a)))

