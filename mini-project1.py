

def board_lenght():
    while True:
        try:
            lenght = 1
            
            while lenght < 2 or lenght > 20:
                print('The board game can\'t be smaller than 2 et larger than 20.')
                lenght = int(input('How many cases do you want the board to have? '))

            return lenght
        except ValueError:
            print('Only intergers are accepted!')




def new_board(n):
    board = [0]*n
    return board



def display(board, n):
    for i in range(n):
        if board[i] == 0:
            print('.', end=' ')
        elif board[i] == 1:
            print('x', end=' ')
        elif board[i] == 2:
            print('o', end=' ')
        elif board[i] == 3:
            print('x', end=' ')
        elif board[i] == 4:
            print('o', end=' ')



        if i + 1 >= 9:
            print(' ', end='')

    print('\n', end='')
    for i in range(n):
        print(i+1, end=' ')



def possible(board, n, i):
    if i+1 > 0 and i < n:
        if board[i] == 0:
            return True
        else:
            return False
    else:
        return False


def select(board, n):
    verif = True
    player = 1
    while True:

        try:
            while True:
                print(f'\n\nPlayer : {player}')
                case = int(input('Choose a case to play : '))
                if possible(board, n, case-1):


                    put(board, n, case, player)

                    if verif:
                        verif = False
                        if player == 1:
                            check_board(board, n, 1)
                            player = 2
                        else:
                            check_board(board, n, 2)
                            player = 1
                    else:
                        if player == 1:
                            check_board(board, n, 1)
                            player = 2
                        else:
                            check_board(board, n, 2)
                            player = 1


                    # check_board(board, n, player)
                    display(board, n)
                    # print('\n')
                        

                else:
                    print('You can\'t play that case')

        except ValueError:
            print('Only intergers are accepted!')
            verif = False



def put(board, n, i, player):
    if player == 1:
        board[i-1] = 1
        # display(board, n)
    else:
        board[i-1] = 2
        # display(board, n)

    # print(board)




def check_board(board, n, player):


    if player == 2:
        if board[n-1] == 1:

            p = 1
            while board[n-p] == board[n-1]:
                if board[n-p-1] == 2:
                    for d in range(n-p,n-1+1):
                        board[d] = 0

                p += 1

    else:
        if board[n-1] == 2:

            p = 1
            while board[n-p] == board[n-1]:
                if board[n-p-1] == 1:
                    for d in range(n-p,n-1+1):
                        board[d] = 0

                p += 1
            
    if player == 2:
        if board[n-n] == 1:

            p = 1
            while board[n-n+p] == board[n-n]:
                if board[n-n+p+1] == 2:
                    for d in range(n-n,n-n+p+1):
                        board[d] = 0

                p += 1

    else:
        if board[n-n] == 2:

            p = 1
            while board[n-n+p] == board[n-n]:
                if board[n-n+p+1] == 1:
                    for d in range(n-n,n-n+p+1):
                        board[d] = 0

                p += 1


    total = 0

    for i in range(n):
        if player == 1:
            if board[i] == 1 or board[i] == 3:
                total += 1
        else:
            if board[i] == 2 or board[i] == 4:
                total += 1

    if total > 1:

        for test in range(n):
        
            for i in range(test, n):
                if player == 1:
                    if board[i] == 1 or board[i] == 3:
                        a = i
                        break
                else:
                    if board[i] == 2 or board[i] == 4:
                        a = i
                        break

            for y in range(a+1, n):
                if player == 1:
                    if board[y] == 1 or board[y] == 3:
                        b = y
                        break
                else:
                    if board[y] == 2 or board[y] == 4:
                        b = y
                        break

            if player == 1:
                board[a] = 3
                board[b] = 3
            else:
                board[a] = 4
                board[b] = 4

            lst = board[a+1:b]

            rs = 0
            for each in range(len(lst)):
                if player == 1:
                    if lst[each] == 2:
                        rs += 1
                else:
                    if lst[each] == 1:
                        rs += 1

            if rs == len(lst):
                
                cases = (b-a)-1

                for c in range(a+1, b):
                    board[c] = 0

            if player == 1:
                board[a] = 1
                board[b] = 1
            else:
                board[a] = 2
                board[b] = 2






lenght = board_lenght()
board = new_board(lenght)

display(board, lenght)


select(board, lenght)






# board = new_board()






# print(newBoard(9))