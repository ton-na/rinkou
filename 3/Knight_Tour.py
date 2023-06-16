# 盤面の大きさ
n = int(input())

# 盤面を初期化
board = [[-1 for i in range(n)] for j in range(n)]

# ナイトが動ける方向
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

# ナイトの初期位置
board[n-1][0] = 0

# バックトラッキング関数 深さ優先探索の一種
def solveKT(pos):
    # ナイトの現在位置を取得
    x = -1
    y = -1
    for i in range(n):
        for j in range(n):
            if board[i][j] == pos-1:
                x = i
                y = j
                break

    # 全てのマスを訪れたらTrueを返す
    if pos == n**2:
        return True
    
    # 現在の位置から次に動けるマスを探す
    for i in range(8):
        # 次のマスの座標
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        
        # 次のマスが盤面内かつ未訪問かどうかチェック
        if 0 <= next_x < n and 0 <= next_y < n and board[next_x][next_y] == -1:
            # 次のマスにナイトを動かす
            board[next_x][next_y] = pos
            # 再帰的に次のマスからバックトラッキングを続ける
            if solveKT(pos+1):
                return True
            # 条件に合わない場合はナイトを元に戻す
            board[next_x][next_y] = -1
    
    # 解が見つからない場合はFalseを返す
    return False

# バックトラッキング関数を呼び出す
if solveKT(1):
    # 解が見つかった場合は盤面を出力する
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
else:
    # 解が見つからなかった場合はメッセージを出力する
    print("解がありません")
