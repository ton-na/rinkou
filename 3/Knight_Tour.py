"""
参考文献　https://daeudaeu.com/knight_tour/
Knight Tour問題をバックトラック法を用いて解き、そして、
制約伝播という手法を用いて高速化する。
"""
import sys
sys.setrecursionlimit(10**8)

# 盤面の大きさ
n = int(input())

# 盤面を初期化
board = [[-1 for i in range(n)] for j in range(n)]

# ナイトが動ける方向
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

# 各マスの次数を記録する配列
degree = [[0 for i in range(n)] for j in range(n)]

# 次数を計算する関数
def calc_degree():
    for i in range(n):
        for j in range(n):
            # 未訪問のマスのみ計算する
            if board[i][j] == -1:
                # 移動できる未訪問のマスの数をカウントする
                count = 0
                for k in range(8):
                    next_i = i + move_x[k]
                    next_j = j + move_y[k]
                    if 0 <= next_i < n and 0 <= next_j < n and board[next_i][next_j] == -1:
                        count += 1
                # 次数にカウントした値を代入する
                degree[i][j] = count

# ナイトの初期位置を盤面の中央付近に設定する. たまに解がでてこなくなるから
start_x = n // 2
start_y = n // 2
board[start_x][start_y] = 0

# 次数を計算する
calc_degree()

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
    min_degree = n # 最小の次数を記録する変数
    min_index = -1 # 最小の次数のマスのインデックスを記録する変数
    for i in range(8):
        # 次のマスの座標
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        
        # 次のマスが盤面内かつ未訪問かどうかチェック
        if 0 <= next_x < n and 0 <= next_y < n and board[next_x][next_y] == -1:
            # 次のマスの次数が最小かどうかチェック
            if degree[next_x][next_y] < min_degree:
                # 最小の次数とインデックスを更新する
                min_degree = degree[next_x][next_y]
                min_index = i
    
    # 最小の次数のマスが見つかった場合
    if min_index != -1:
        # 次のマスの座標
        next_x = x + move_x[min_index]
        next_y = y + move_y[min_index]
        
        # 次のマスにナイトを動かす
        board[next_x][next_y] = pos
        
        # 現在のマスと隣接するマスの次数を-1する
        for i in range(8):
            adj_x = x + move_x[i]
            adj_y = y + move_y[i]
            if 0 <= adj_x < n and 0 <= adj_y < n and board[adj_x][adj_y] == -1:
                degree[adj_x][adj_y] -= 1
        
        # 再帰的に次のマスからバックトラッキングを続ける
        if solveKT(pos+1):
            return True
        
        # 条件に合わない場合はナイトを元に戻す
        board[next_x][next_y] = -1
        
        # 現在のマスと隣接するマスの次数を+1する
        for i in range(8):
            adj_x = x + move_x[i]
            adj_y = y + move_y[i]
            if 0 <= adj_x < n and 0 <= adj_y < n and board[adj_x][adj_y] == -1:
                degree[adj_x][adj_y] += 1
    
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
