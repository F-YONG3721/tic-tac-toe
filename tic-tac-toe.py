import random as rd
import os

# 棋盤
board = [
    [' ', '01', '02', '03'],       # 0
    ['a', 'None', 'None', 'None'], # 1
    ['b', 'None', 'None', 'None'], # 2
    ['c', 'None', 'None', 'None']  # 3
]  #  0      1       2       3

# 印出棋盤
def printBoard(board):
    print(f"---------------------------\n{"tic-tac-toe":^27s}\n---------------------------")
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(f"{board[i][j]:^4s}", end=' | ')
        print('\n', "---------------------------", sep='')

# 畫ooxx
def draw(symbol = 'X', player = "h", row = None, column = None):
    # column = 0 # --
    # row = 0 # |
    locationTransfer = {
        'a' : 1,
        'b' : 2,
        'c' : 3
        }

    if row.isdigit():
        row = int(row)
    else:
        print("row error")
    
    if column.isalpha():
        column = locationTransfer[column]
    else:
        print("column error")

    global board

    if board[column][row] in 'XO':
        print("input error")
        return "error"

    board[column][row] = symbol

# 檢查是否勝利
def check(board = board, player = 'X'):
    checkList = []
    # 檢查 是否有連線

    # check column
    # print("part 1")
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            # print(f"i: {i}, j: {j}, board[i][j]: {board[i][j]}")
            checkList.append(board[i][j])

        if checkList.count(player) == 3:
            if player == 'X':
                print("game over: human column")
                return "human"
            elif player == 'O':
                print("game over: robot column")
                return "robot"
            else:
                print("player error")

        # print(f"check.checkList: {checkList}")
        # print(f"count(x): {checkList.count("X")}")
        
        
        checkList.clear()

    # check row
    # print("part 2")
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            checkList.append(board[j][i])

        # print(f"checkList: {checkList}\ncount: {checkList.count("X")}")

        if checkList.count(player) == 3:
            if player == 'X':
                print("game over: human row")
                return "human"
            elif player == 'O':
                print("game over: robot row")
                return "robot"
            else:
                print("player error")
        
        # print(f"check.checkList: {checkList}")
        checkList.clear()

    # check slash
    # print("part 3")
    for i in range(1, len(board)):
        checkList.append(board[i][i])
        if checkList.count(player) == 3:
            if player == 'X':
                print("game over: human slash")
                return "human"
            elif player == 'O':
                print("game over: robot slash")
                return "robot"
            else:
                print("player error")
        else:
            pass

    # print(f"check.checkList: {checkList}")
    checkList.clear()

    for i in range(1, len(board)):
        checkList.append(board[i][len(board)-i])
        if checkList.count(player) == 3:
            if player == 'X':
                print("game over: human slash")
                return "human"
            elif player == 'O':
                print("game over: robot slash")
                return "robot"
            else:
                print("player error")
        else:
            pass
    checkList.clear()

    # 檢查是否和局
    # print("check draw")
    countNone = 0
    for i in board:
        countNone += i.count("None")

    # print(f"countNone: {countNone}")
    if countNone == 1:
        return "tie"

# 機器人找要畫的位置
def robotCheck(board = board, player = 'X'):
    checkList = []

    # column
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            checkList.append(board[i][j])

        # print(f"column checkList: {checkList}")
        if checkList.count(player) == 2 and checkList.count("None") != 0:
            c = checkList.index('None') + 1
            return c, i

        checkList.clear()

    # row
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            checkList.append(board[j][i])
        
        # print(f"row checkList: {checkList}")

        if checkList.count(player) == 2 and checkList.count("None") != 0:
            r = checkList.index('None') + 1
            return i, r

        checkList.clear()
    
    # slash
    for i in range(1, len(board)):
        # print(f"slash1: {board[i][i]}")
        checkList.append(board[i][i])

        # print(f"slash checkList: {checkList}")

        if checkList.count(player) == 2 and checkList.count("None") != 0:
            r = checkList.index('None') + 1
            # print(f"slash:r : {r}")
            return r, r
        else:
            pass
    checkList.clear()

    for i in range(1, len(board)):
        # print(f"slash2: {board[i][i]}")
        checkList.append(board[i][len(board)-i])

        # print(f"slash checkList: {checkList}")

        if checkList.count(player) == 2 and checkList.count("None") != 0:
            r = checkList.index('None') + 1
            return len(board) - r, r
        else:
            pass
    checkList.clear()

    return None, None

# 機器人選擇要畫的位置
def robot():
    transfer = {
        1 : 'a',
        2 : 'b',
        3 : 'c'
    }

    r, c = robotCheck(board=board, player= 'O')
    # print(f"1--r: {r}, c: {c}")
    if r == None or c == None:
        r, c = robotCheck(board=board, player= 'X')
        # print(f"11-r: {r}, c: {c}")

        if r == None or c == None:
            r = str(rd.randint(1, 3))
            c = ['a', 'b', 'c'][rd.randint(0, 2)]
        else:
            r = str(r)
            c = transfer[c]            

    else:
        r = str(r)
        c = transfer[c]

    print(f"2--r: {r}, c: {c}")

    
    

    a = draw(row = r, column = c, player='r', symbol='O')
    if a == "error":
        print("robot-請重新輸入: ")
        robot()
    else:
        pass

#人類選擇要畫的位置
def human():
    r, c = input("please input location column, row: ").split()
    a = draw(row = r, column = c)
    if a == "error":
        print("human-請重新輸入: ")
        human()
    else:
        pass

# 遊戲流程控制
def main():
    os.system("clear")
    global board
    printBoard(board)
    while True:
        try:
            human()

            c = check(board=board, player = 'X')
            if c == "human":
                os.system("clear")
                # printBoard(board)
                print("human win")
                break

            elif c == "tie":
                os.system("clear")
                # printBoard(board)
                print("draw")
                break

            else:
                pass

            robot()

            c = check(board=board, player = 'O')
            if c == "robot":
                os.system("clear")
                # printBoard(board)
                print("robot win")
                
                break
            elif c == "tie":
                os.system("clear")
                # printBoard(board)
                print("draw")
                break
            else:
                pass

            os.system("clear")

        except Exception as e:
            print(e)

            a = input("input q exit or [enter] continue: ")
            if a == '':
                pass
            elif a in 'Qq' :
                break
            else:
                pass

        else:
            pass

        finally:
            printBoard(board)

main()