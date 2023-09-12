

def legal_moves(board,turn):
    boards = []
    counter = 0

    if turn == 'black':
        opponents = ['P','R', 'N', 'B','Q', 'K']
        friends = ['p','r','n', 'b','q', 'k']
        for i in board:
            if i == 'p':
                if board[counter-8] == '.':
                    newboard = list.copy(board)
                    if counter - 8 >= 0 and counter - 8 <= 7:
                        newboard[counter - 8] = 'q'
                    else:
                        newboard[counter-8] = 'p'
                    newboard[counter] = '.'
                    boards.append(newboard)
                if counter >= 48 and counter <= 55 and board[counter-16] == '.' and board[counter-8] == '.':
                    newboard = list.copy(board)
                    newboard[counter - 16] = 'p'
                    newboard[counter] = '.'
                    boards.append(newboard)
                if counter%8 == 0 and board[counter-7] in opponents:
                    newboard = list.copy(board)
                    if counter - 7 >= 0 and counter - 7 <= 7:
                        newboard[counter - 7] = 'q'
                    else:
                        newboard[counter-7] = 'p'
                    newboard[counter] = '.'
                    boards.append(newboard)
                if (counter+1)%8 == 0 and board[counter-9] in opponents:
                    newboard = list.copy(board)
                    if counter - 9 >= 0 and counter - 9 <= 7:
                        newboard[counter - 9] = 'q'
                    else:
                        newboard[counter-9] = 'p'
                    newboard[counter] = '.'
                    boards.append(newboard)
                if (counter+1)%8 != 0 and counter%8 != 0  and board[counter-7] in opponents:
                    newboard = list.copy(board)
                    if counter - 9 >= 0 and counter - 9 <= 7:
                        newboard[counter - 7] = 'q'
                    else:
                        newboard[counter - 7] = 'p'
                    newboard[counter] = '.'
                    boards.append(newboard)
                if (counter+1)%8 != 0 and counter%8 != 0  and board[counter-9] in opponents:
                    newboard = list.copy(board)
                    if counter - 9 >= 0 and counter - 9 <= 7:
                        newboard[counter - 9] = 'q'
                    else:
                        newboard[counter - 9] = 'p'
                    newboard[counter] = '.'
                    boards.append(newboard)
            if i == 'n':
                if counter - 15 >= 0 and counter%8 != 7:
                    if board[counter - 15] not in friends:
                        newboard = list.copy(board)
                        newboard[counter - 15] = 'n'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter + 15 <= 63 and counter%8 != 0:
                    if board[counter + 15] not in friends:
                        newboard = list.copy(board)
                        newboard[counter + 15] = 'n'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter - 17 >= 0 and counter%8 != 0:
                    if board[counter - 17] not in friends:
                        newboard = list.copy(board)
                        newboard[counter - 17] = 'n'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter + 17 <= 63 and counter%8 != 7:
                    if board[counter + 17] not in friends:
                        newboard = list.copy(board)
                        newboard[counter + 17] = 'n'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter - 10 >= 0 and counter%8 != 0 and counter%8 != 1:
                    if board[counter - 10] not in friends:
                        newboard = list.copy(board)
                        newboard[counter - 10] = 'n'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter + 10 <= 63 and counter%8 != 6 and counter%8 != 7:
                    if board[counter + 10] not in friends:
                        newboard = list.copy(board)
                        newboard[counter + 10] = 'n'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter - 6 >= 0 and counter%8 != 6 and counter%8 != 7:
                    if board[counter - 6] not in friends:
                        newboard = list.copy(board)
                        newboard[counter - 6] = 'n'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter + 6 <= 63 and counter%8 != 0 and counter%8 != 1:
                    if board[counter + 6] not in friends:
                        newboard = list.copy(board)
                        newboard[counter + 6] = 'n'
                        newboard[counter] = '.'
                        boards.append(newboard)
            if i == 'k':
                if counter - 8 >= 0:
                    if board[counter-8] not in friends:
                        newboard = list.copy(board)
                        newboard[counter - 8] = 'k'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter + 8 <= 63:
                    if board[counter+8] not in friends:
                        newboard = list.copy(board)
                        newboard[counter + 8] = 'k'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter % 8 != 0:
                    if board[counter-1] not in friends:
                        newboard = list.copy(board)
                        newboard[counter -1] = 'k'
                        newboard[counter] = '.'
                        boards.append(newboard)
                    if counter >= 8:
                        if board[counter-7] not in friends:
                            newboard = list.copy(board)
                            newboard[counter - 7] = 'k'
                            newboard[counter] = '.'
                            boards.append(newboard)
                    if counter <= 55:
                        if board[counter+9] not in friends:
                            newboard = list.copy(board)
                            newboard[counter + 9] = 'k'
                            newboard[counter] = '.'
                            boards.append(newboard)
                if counter % 8 != 7:
                    if board[counter+1] not in friends:
                        newboard = list.copy(board)
                        newboard[counter +1] = 'k'
                        newboard[counter] = '.'
                        boards.append(newboard)
                    if counter >= 8:
                        if board[counter-9] not in friends:
                            newboard = list.copy(board)
                            newboard[counter - 9] = 'k'
                            newboard[counter] = '.'
                            boards.append(newboard)
                    if counter <= 55:
                        if board[counter+7] not in friends:
                            newboard = list.copy(board)
                            newboard[counter + 7] = 'k'
                            newboard[counter] = '.'
                            boards.append(newboard)
            if i == 'r':
                if counter % 8 != 0:
                    if board[counter-1] not in friends:
                        if board[counter - 1] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 1] = 'r'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 1] = 'r'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-1) % 8 != 0:
                                if board[counter - 2] not in friends:
                                    if board[counter - 2] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 2] = 'r'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 2] = 'r'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter - 2) % 8 != 0:
                                            if board[counter - 3] not in friends:
                                                if board[counter - 3] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 3] = 'r'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 3] = 'r'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter - 3) % 8 != 0:
                                                        if board[counter - 4] not in friends:
                                                            if board[counter - 4] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 4] = 'r'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 4] = 'r'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter - 4) % 8 != 0:
                                                                    if board[counter - 5] not in friends:
                                                                        if board[counter - 5] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 5] = 'r'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 5] = 'r'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter - 5) % 8 != 0:
                                                                                if board[counter - 6] not in friends:
                                                                                    if board[counter - 6] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 6] = 'r'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 6] = 'r'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 6) % 8 != 0:
                                                                                            if board[counter - 7] not in friends:
                                                                                                if board[counter - 7] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 7] = 'r'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 7] = 'r'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 7:
                    if board[counter + 1] not in friends:
                        if board[counter + 1] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 1] = 'r'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 1] = 'r'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter + 1) % 8 != 7:
                                if board[counter + 2] not in friends:
                                    if board[counter + 2] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 2] = 'r'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 2] = 'r'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter + 2) % 8 != 7:
                                            if board[counter + 3] not in friends:
                                                if board[counter + 3] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 3] = 'r'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 3] = 'r'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter + 3) % 8 != 7:
                                                        if board[counter + 4] not in friends:
                                                            if board[counter + 4] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 4] = 'r'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 4] = 'r'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 4) % 8 != 7:
                                                                    if board[counter + 5] not in friends:
                                                                        if board[counter + 5] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 4] = 'r'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 5] = 'r'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter + 5) % 8 != 7:
                                                                                if board[counter + 6] not in friends:
                                                                                    if board[counter + 6] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 6] = 'r'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 6] = 'r'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 6) % 8 != 7:
                                                                                                if board[counter + 7] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 7] = 'r'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 7] = 'r'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter >= 8:
                    if board[counter-8] not in friends:
                        if board[counter - 8] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 8] = 'r'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 8] = 'r'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-8) >= 8:
                                if board[counter - 16] not in friends:
                                    if board[counter - 16] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 16] = 'r'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 16] = 'r'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter - 16) >= 8:
                                            if board[counter - 24] not in friends:
                                                if board[counter - 24] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 24] = 'r'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 24] = 'r'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter - 24) >= 8:
                                                        if board[counter - 32] not in friends:
                                                            if board[counter - 32] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 32] = 'r'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 32] = 'r'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter - 32) >= 8:
                                                                    if board[counter - 40] not in friends:
                                                                        if board[counter - 40] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 40] = 'r'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 40] = 'r'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter - 40) >= 8:
                                                                                if board[counter - 48] not in friends:
                                                                                    if board[counter - 48] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 48] = 'r'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 48] = 'r'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 48) >= 8:
                                                                                            if board[counter - 56] not in friends:
                                                                                                if board[counter - 56] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 56] = 'r'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 56] = 'r'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter <= 55:
                    if board[counter+8] not in friends:
                        if board[counter + 8] in opponents:
                            newboard = list.copy(board)
                            newboard[counter + 8] = 'r'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 8] = 'r'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter+8) <= 55:
                                if board[counter + 16] not in friends:
                                    if board[counter + 16] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 16] = 'r'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 16] = 'r'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter + 16) <= 55:
                                            if board[counter + 24] not in friends:
                                                if board[counter + 24] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 24] = 'r'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 24] = 'r'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter + 24) <= 55:
                                                        if board[counter + 32] not in friends:
                                                            if board[counter + 32] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 32] = 'r'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 32] = 'r'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 32) <= 55:
                                                                    if board[counter + 40] not in friends:
                                                                        if board[counter + 40] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 40] = 'r'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 40] = 'r'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter + 40) <= 55:
                                                                                if board[counter + 48] not in friends:
                                                                                    if board[counter + 48] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 48] = 'r'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 48] = 'r'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 48) <= 55:
                                                                                            if board[counter + 56] not in friends:
                                                                                                if board[counter + 56] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 56] = 'r'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 56] = 'r'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
            if i == 'b':
                if counter % 8 != 0 and counter >=8:
                    if board[counter-9] not in friends:
                        if board[counter - 9] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 9] = 'b'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 9] = 'b'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-9) % 8 != 0 and (counter-9) >=8:
                                if board[counter - 18] not in friends:
                                    if board[counter - 18] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 18] = 'b'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 18] = 'b'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter - 18) % 8 != 0 and (counter - 18) >=8:
                                            if board[counter - 27] not in friends:
                                                if board[counter - 27] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 27] = 'b'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 27] = 'b'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter - 27) % 8 != 0 and (counter - 27) >=8:
                                                        if board[counter - 36] not in friends:
                                                            if board[counter - 36] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 36] = 'b'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 36] = 'b'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter - 36) % 8 != 0 and (counter - 36) >=8:
                                                                    if board[counter - 45] not in friends:
                                                                        if board[counter - 45] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 45] = 'b'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 45] = 'b'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter - 45) % 8 != 0 and (counter - 45) >=8:
                                                                                if board[counter - 54] not in friends:
                                                                                    if board[counter - 54] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 54] = 'b'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 54] = 'b'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 54) % 8 != 0 and (counter - 54) >=8:
                                                                                            if board[counter - 63] not in friends:
                                                                                                if board[counter - 63] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 63] = 'b'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 63] = 'b'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 7 and counter >=8:
                    if board[counter-7] not in friends:
                        if board[counter - 7] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 7] = 'b'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 7] = 'b'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-7) % 8 != 7 and (counter-7) >=8:
                                if board[counter - 14] not in friends:
                                    if board[counter - 14] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 14] = 'b'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 14] = 'b'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter-14) % 8 != 7 and (counter-14) >=8:
                                            if board[counter - 21] not in friends:
                                                if board[counter - 21] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 21] = 'b'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 21] = 'b'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter-21) % 8 != 7 and (counter-21) >=8:
                                                        if board[counter - 28] not in friends:
                                                            if board[counter - 28] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 28] = 'b'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 28] = 'b'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter- 28) % 8 != 7 and (counter-28) >=8:
                                                                    if board[counter - 35] not in friends:
                                                                        if board[counter - 35] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 35] = 'b'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 35] = 'b'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter-35) % 8 != 7 and (counter-35) >=8:
                                                                                if board[counter - 42] not in friends:
                                                                                    if board[counter - 42] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 42] = 'b'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 42] = 'b'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 42) % 8 != 7 and (counter - 42) >=8:
                                                                                            if board[counter - 49] not in friends:
                                                                                                if board[counter - 49] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 49] = 'b'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 49] = 'b'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 7 and counter <=55:
                    if board[counter+9] not in friends:
                        if board[counter + 9] in opponents:
                            newboard = list.copy(board)
                            newboard[counter + 9] = 'b'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 9] = 'b'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter+9) % 8 != 7 and (counter+9) <=55:
                                if board[counter + 18] not in friends:
                                    if board[counter + 18] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 18] = 'b'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 18] = 'b'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter + 18) % 8 != 7 and (counter + 18) <=55:
                                            if board[counter + 27] not in friends:
                                                if board[counter + 27] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 27] = 'b'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 27] = 'b'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter + 27) % 8 != 7 and (counter + 27) <=55:
                                                        if board[counter + 36] not in friends:
                                                            if board[counter + 36] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 36] = 'b'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 36] = 'b'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 36) % 8 != 7 and (counter + 36) <=55:
                                                                    if board[counter + 45] not in friends:
                                                                        if board[counter + 45] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 45] = 'b'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 45] = 'b'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter + 45) % 8 != 7 and (counter + 45) <=55:
                                                                                if board[counter + 54] not in friends:
                                                                                    if board[counter + 54] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 54] = 'b'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 54] = 'b'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 54) % 8 != 7 and (counter + 54) <=55:
                                                                                            if board[counter + 63] not in friends:
                                                                                                if board[counter + 63] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 63] = 'b'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 63] = 'b'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 0 and counter <=55:
                    if board[counter+7] not in friends:
                        if board[counter + 7] in opponents:
                            newboard = list.copy(board)
                            newboard[counter + 7] = 'b'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 7] = 'b'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter+7) % 8 != 0 and (counter+7) <=55:
                                if board[counter + 14] not in friends:
                                    if board[counter + 14] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 14] = 'b'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 14] = 'b'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter+14) % 8 != 0 and (counter+14) <=55:
                                            if board[counter + 21] not in friends:
                                                if board[counter + 21] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 21] = 'b'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 21] = 'b'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter+21) % 8 != 0 and (counter+21) <=55:
                                                        if board[counter + 28] not in friends:
                                                            if board[counter + 28] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 28] = 'b'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 28] = 'b'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 28) % 8 != 0 and (counter+28) <=55:
                                                                    if board[counter + 35] not in friends:
                                                                        if board[counter + 35] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 35] = 'b'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 35] = 'b'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter+35) % 8 != 0 and (counter+35) <=55:
                                                                                if board[counter + 42] not in friends:
                                                                                    if board[counter + 42] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 42] = 'b'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 42] = 'b'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 42) % 8 != 0 and (counter + 42) <=55:
                                                                                            if board[counter + 49] not in friends:
                                                                                                if board[counter + 49] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 49] = 'b'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 49] = 'b'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
            if i == 'q':
                if counter % 8 != 0 and counter >=8:
                    if board[counter-9] not in friends:
                        if board[counter - 9] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 9] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 9] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-9) % 8 != 0 and (counter-9) >=8:
                                if board[counter - 18] not in friends:
                                    if board[counter - 18] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 18] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 18] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter - 18) % 8 != 0 and (counter - 18) >=8:
                                            if board[counter - 27] not in friends:
                                                if board[counter - 27] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 27] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 27] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter - 27) % 8 != 0 and (counter - 27) >=8:
                                                        if board[counter - 36] not in friends:
                                                            if board[counter - 36] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 36] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 36] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter - 36) % 8 != 0 and (counter - 36) >=8:
                                                                    if board[counter - 45] not in friends:
                                                                        if board[counter - 45] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 45] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 45] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter - 45) % 8 != 0 and (counter - 45) >=8:
                                                                                if board[counter - 54] not in friends:
                                                                                    if board[counter - 54] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 54] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 54] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 54) % 8 != 0 and (counter - 54) >=8:
                                                                                            if board[counter - 63] not in friends:
                                                                                                if board[counter - 63] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 63] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 63] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 7 and counter >=8:
                    if board[counter-7] not in friends:
                        if board[counter - 7] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 7] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 7] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-7) % 8 != 7 and (counter-7) >=8:
                                if board[counter - 14] not in friends:
                                    if board[counter - 14] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 14] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 14] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter-14) % 8 != 7 and (counter-14) >=8:
                                            if board[counter - 21] not in friends:
                                                if board[counter - 21] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 21] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 21] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter-21) % 8 != 7 and (counter-21) >=8:
                                                        if board[counter - 28] not in friends:
                                                            if board[counter - 28] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 28] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 28] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter- 28) % 8 != 7 and (counter-28) >=8:
                                                                    if board[counter - 35] not in friends:
                                                                        if board[counter - 35] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 35] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 35] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter-35) % 8 != 7 and (counter-35) >=8:
                                                                                if board[counter - 42] not in friends:
                                                                                    if board[counter - 42] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 42] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 42] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 42) % 8 != 7 and (counter - 42) >=8:
                                                                                            if board[counter - 49] not in friends:
                                                                                                if board[counter - 49] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 49] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 49] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 7 and counter <=55:
                    if board[counter+9] not in friends:
                        if board[counter + 9] in opponents:
                            newboard = list.copy(board)
                            newboard[counter + 9] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 9] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter+9) % 8 != 7 and (counter+9) <=55:
                                if board[counter + 18] not in friends:
                                    if board[counter + 18] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 18] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 18] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter + 18) % 8 != 7 and (counter + 18) <=55:
                                            if board[counter + 27] not in friends:
                                                if board[counter + 27] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 27] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 27] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter + 27) % 8 != 7 and (counter + 27) <=55:
                                                        if board[counter + 36] not in friends:
                                                            if board[counter + 36] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 36] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 36] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 36) % 8 != 7 and (counter + 36) <=55:
                                                                    if board[counter + 45] not in friends:
                                                                        if board[counter + 45] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 45] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 45] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter + 45) % 8 != 7 and (counter + 45) <=55:
                                                                                if board[counter + 54] not in friends:
                                                                                    if board[counter + 54] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 54] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 54] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 54) % 8 != 7 and (counter + 54) <=55:
                                                                                            if board[counter + 63] not in friends:
                                                                                                if board[counter + 63] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 63] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 63] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 0 and counter <=55:
                    if board[counter+7] not in friends:
                        if board[counter + 7] in opponents:
                            newboard = list.copy(board)
                            newboard[counter + 7] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 7] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter+7) % 8 != 0 and (counter+7) <=55:
                                if board[counter + 14] not in friends:
                                    if board[counter + 14] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 14] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 14] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter+14) % 8 != 0 and (counter+14) <=55:
                                            if board[counter + 21] not in friends:
                                                if board[counter + 21] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 21] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 21] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter+21) % 8 != 0 and (counter+21) <=55:
                                                        if board[counter + 28] not in friends:
                                                            if board[counter + 28] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 28] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 28] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 28) % 8 != 0 and (counter+28) <=55:
                                                                    if board[counter + 35] not in friends:
                                                                        if board[counter + 35] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 35] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 35] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter+35) % 8 != 0 and (counter+35) <=55:
                                                                                if board[counter + 42] not in friends:
                                                                                    if board[counter + 42] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 42] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 42] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 42) % 8 != 0 and (counter + 42) <=55:
                                                                                            if board[counter + 49] not in friends:
                                                                                                if board[counter + 49] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 49] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 49] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)

                if counter % 8 != 0:
                    if board[counter-1] not in friends:
                        if board[counter - 1] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 1] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 1] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-1) % 8 != 0:
                                if board[counter - 2] not in friends:
                                    if board[counter - 2] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 2] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 2] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter - 2) % 8 != 0:
                                            if board[counter - 3] not in friends:
                                                if board[counter - 3] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 3] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 3] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter - 3) % 8 != 0:
                                                        if board[counter - 4] not in friends:
                                                            if board[counter - 4] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 4] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 4] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter - 4) % 8 != 0:
                                                                    if board[counter - 5] not in friends:
                                                                        if board[counter - 5] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 5] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 5] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter - 5) % 8 != 0:
                                                                                if board[counter - 6] not in friends:
                                                                                    if board[counter - 6] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 6] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 6] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 6) % 8 != 0:
                                                                                            if board[counter - 7] not in friends:
                                                                                                if board[counter - 7] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 7] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 7] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 7:
                    if board[counter + 1] not in friends:
                        if board[counter + 1] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 1] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 1] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter + 1) % 8 != 7:
                                if board[counter + 2] not in friends:
                                    if board[counter + 2] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 2] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 2] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter + 2) % 8 != 7:
                                            if board[counter + 3] not in friends:
                                                if board[counter + 3] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 3] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 3] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter + 3) % 8 != 7:
                                                        if board[counter + 4] not in friends:
                                                            if board[counter + 4] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 4] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 4] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 4) % 8 != 7:
                                                                    if board[counter + 5] not in friends:
                                                                        if board[counter + 5] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 4] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 5] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter + 5) % 8 != 7:
                                                                                if board[counter + 6] not in friends:
                                                                                    if board[counter + 6] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 6] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 6] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 6) % 8 != 7:
                                                                                                if board[counter + 7] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 7] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 7] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter >= 8:
                    if board[counter-8] not in friends:
                        if board[counter - 8] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 8] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 8] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-8) >= 8:
                                if board[counter - 16] not in friends:
                                    if board[counter - 16] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 16] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 16] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter - 16) >= 8:
                                            if board[counter - 24] not in friends:
                                                if board[counter - 24] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 24] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 24] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter - 24) >= 8:
                                                        if board[counter - 32] not in friends:
                                                            if board[counter - 32] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 32] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 32] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter - 32) >= 8:
                                                                    if board[counter - 40] not in friends:
                                                                        if board[counter - 40] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 40] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 40] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter - 40) >= 8:
                                                                                if board[counter - 48] not in friends:
                                                                                    if board[counter - 48] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 48] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 48] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 48) >= 8:
                                                                                            if board[counter - 56] not in friends:
                                                                                                if board[counter - 56] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 56] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 56] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter <= 55:
                    if board[counter+8] not in friends:
                        if board[counter + 8] in opponents:
                            newboard = list.copy(board)
                            newboard[counter + 8] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 8] = 'q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter+8) <= 55:
                                if board[counter + 16] not in friends:
                                    if board[counter + 16] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 16] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 16] = 'q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter + 16) <= 55:
                                            if board[counter + 24] not in friends:
                                                if board[counter + 24] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 24] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 24] = 'q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter + 24) <= 55:
                                                        if board[counter + 32] not in friends:
                                                            if board[counter + 32] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 32] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 32] = 'q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 32) <= 55:
                                                                    if board[counter + 40] not in friends:
                                                                        if board[counter + 40] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 40] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 40] = 'q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter + 40) <= 55:
                                                                                if board[counter + 48] not in friends:
                                                                                    if board[counter + 48] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 48] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 48] = 'q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 48) <= 55:
                                                                                            if board[counter + 56] not in friends:
                                                                                                if board[counter + 56] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 56] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 56] = 'q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)



            counter += 1
    if turn == 'white':
        friends = ['P', 'R', 'N', 'B', 'Q', 'K']
        opponents = ['p', 'r', 'n', 'b', 'q', 'k']
        for i in board:
            if i == 'P':
                if board[counter + 8] == '.':
                    newboard = list.copy(board)
                    if counter + 8 >= 56 and counter + 8 <= 63:
                        newboard[counter + 8] = 'Q'
                    else:
                        newboard[counter + 8] = 'P'
                    newboard[counter] = '.'
                    boards.append(newboard)
                if counter >= 8 and counter <= 15 and board[counter + 16] == '.' and board[counter + 8] == '.':
                    newboard = list.copy(board)
                    newboard[counter + 16] = 'P'
                    newboard[counter] = '.'
                    boards.append(newboard)
                if (counter+1) % 8 == 0 and board[counter + 7] in opponents:
                    newboard = list.copy(board)
                    if counter + 9 <=63  and counter + 9 >= 56:
                        newboard[counter + 7] = 'Q'
                    else:
                        newboard[counter + 7] = 'P'
                    newboard[counter] = '.'
                    boards.append(newboard)
                if counter % 8 == 0 and board[counter + 9] in opponents:
                    newboard = list.copy(board)
                    if counter + 9 <=63  and counter + 9 >= 56:
                        newboard[counter + 9] = 'Q'
                    else:
                        newboard[counter + 9] = 'P'
                    newboard[counter] = '.'
                    boards.append(newboard)
                if (counter + 1) % 8 != 0 and counter % 8 != 0 and board[counter + 7] in opponents:
                    newboard = list.copy(board)
                    if counter + 9 <=63  and counter + 9 >= 56:
                        newboard[counter + 7] = 'Q'
                    else:
                        newboard[counter + 7] = 'P'
                    newboard[counter] = '.'
                    boards.append(newboard)
                if (counter + 1) % 8 != 0 and counter % 8 != 0 and board[counter + 9] in opponents:
                    newboard = list.copy(board)
                    if counter + 9 <=63  and counter + 9 >= 56:
                        newboard[counter + 9] = 'Q'
                    else:
                        newboard[counter + 9] = 'P'
                    newboard[counter] = '.'
                    boards.append(newboard)
            if i == 'N':
                if counter - 15 >= 0 and counter%8 != 7:
                    if board[counter - 15] not in friends:
                        newboard = list.copy(board)
                        newboard[counter - 15] = 'N'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter + 15 <= 63 and counter%8 != 0:
                    if board[counter + 15] not in friends:
                        newboard = list.copy(board)
                        newboard[counter + 15] = 'N'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter - 17 >= 0 and counter%8 != 0:
                    if board[counter - 17] not in friends:
                        newboard = list.copy(board)
                        newboard[counter - 17] = 'N'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter + 17 <= 63 and counter%8 != 7:
                    if board[counter + 17] not in friends:
                        newboard = list.copy(board)
                        newboard[counter + 17] = 'N'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter - 10 >= 0 and counter%8 != 0 and counter%8 != 1:
                    if board[counter - 10] not in friends:
                        newboard = list.copy(board)
                        newboard[counter - 10] = 'N'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter + 10 <= 63 and counter%8 != 6 and counter%8 != 7:
                    if board[counter + 10] not in friends:
                        newboard = list.copy(board)
                        newboard[counter + 10] = 'N'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter - 6 >= 0 and counter%8 != 6 and counter%8 != 7:
                    if board[counter - 6] not in friends:
                        newboard = list.copy(board)
                        newboard[counter - 6] = 'N'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter + 6 <= 63 and counter%8 != 0 and counter%8 != 1:
                    if board[counter + 6] not in friends:
                        newboard = list.copy(board)
                        newboard[counter + 6] = 'N'
                        newboard[counter] = '.'
                        boards.append(newboard)
            if i == 'K':
                if counter - 8 >= 0:
                    if board[counter - 8] not in friends:
                        newboard = list.copy(board)
                        newboard[counter - 8] = 'K'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter + 8 <= 63:
                    if board[counter + 8] not in friends:
                        newboard = list.copy(board)
                        newboard[counter + 8] = 'K'
                        newboard[counter] = '.'
                        boards.append(newboard)
                if counter % 8 != 0:
                    if board[counter - 1] not in friends:
                        newboard = list.copy(board)
                        newboard[counter - 1] = 'K'
                        newboard[counter] = '.'
                        boards.append(newboard)
                    if counter >= 8:
                        if board[counter - 7] not in friends:
                            newboard = list.copy(board)
                            newboard[counter - 7] = 'K'
                            newboard[counter] = '.'
                            boards.append(newboard)
                    if counter <= 55:
                        if board[counter + 9] not in friends:
                            newboard = list.copy(board)
                            newboard[counter + 9] = 'K'
                            newboard[counter] = '.'
                            boards.append(newboard)
                if counter % 8 != 7:
                    if board[counter + 1] not in friends:
                        newboard = list.copy(board)
                        newboard[counter + 1] = 'K'
                        newboard[counter] = '.'
                        boards.append(newboard)
                    if counter >= 8:
                        if board[counter - 9] not in friends:
                            newboard = list.copy(board)
                            newboard[counter - 9] = 'K'
                            newboard[counter] = '.'
                            boards.append(newboard)
                    if counter <= 55:
                        if board[counter + 7] not in friends:
                            newboard = list.copy(board)
                            newboard[counter + 7] = 'K'
                            newboard[counter] = '.'
                            boards.append(newboard)
            if i == 'R':
                if counter % 8 != 0:
                    if board[counter - 1] not in friends:
                        if board[counter - 1] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 1] = 'R'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 1] = 'R'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter - 1) % 8 != 0:
                                if board[counter - 2] not in friends:
                                    if board[counter - 2] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 2] = 'R'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 2] = 'R'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter - 2) % 8 != 0:
                                            if board[counter - 3] not in friends:
                                                if board[counter - 3] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 3] = 'R'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 3] = 'R'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter - 3) % 8 != 0:
                                                        if board[counter - 4] not in friends:
                                                            if board[counter - 4] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 4] = 'R'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 4] = 'R'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter - 4) % 8 != 0:
                                                                    if board[counter - 5] not in friends:
                                                                        if board[counter - 5] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 5] = 'R'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 5] = 'R'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter - 5) % 8 != 0:
                                                                                if board[counter - 6] not in friends:
                                                                                    if board[counter - 6] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 6] = 'R'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 6] = 'R'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 6) % 8 != 0:
                                                                                            if board[counter - 7] not in friends:
                                                                                                if board[counter - 7] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 7] = 'R'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 7] = 'R'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 7:
                    if board[counter + 1] not in friends:
                        if board[counter + 1] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 1] = 'R'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 1] = 'R'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter + 1) % 8 != 7:
                                if board[counter + 2] not in friends:
                                    if board[counter + 2] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 2] = 'R'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 2] = 'R'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter + 2) % 8 != 7:
                                            if board[counter + 3] not in friends:
                                                if board[counter + 3] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 3] = 'R'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 3] = 'R'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter + 3) % 8 != 7:
                                                        if board[counter + 4] not in friends:
                                                            if board[counter + 4] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 4] = 'R'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 4] = 'R'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 4) % 8 != 7:
                                                                    if board[counter + 5] not in friends:
                                                                        if board[counter + 5] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 4] = 'R'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 5] = 'R'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter + 5) % 8 != 7:
                                                                                if board[counter + 6] not in friends:
                                                                                    if board[counter + 6] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 6] = 'R'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 6] = 'R'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 6) % 8 != 7:
                                                                                            if board[counter + 7] in opponents:
                                                                                                newboard = list.copy(board)
                                                                                                newboard[counter + 7] = 'R'
                                                                                                newboard[counter] = '.'
                                                                                                boards.append(newboard)
                                                                                            else:
                                                                                                newboard = list.copy(board)
                                                                                                newboard[counter + 7] = 'R'
                                                                                                newboard[counter] = '.'
                                                                                                boards.append(newboard)
                if counter >= 8:
                    if board[counter - 8] not in friends:
                        if board[counter - 8] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 8] = 'R'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 8] = 'R'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter - 8) >= 8:
                                if board[counter - 16] not in friends:
                                    if board[counter - 16] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 16] = 'R'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 16] = 'R'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter - 16) >= 8:
                                            if board[counter - 24] not in friends:
                                                if board[counter - 24] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 24] = 'R'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 24] = 'R'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter - 24) >= 8:
                                                        if board[counter - 32] not in friends:
                                                            if board[counter - 32] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 32] = 'R'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 32] = 'R'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter - 32) >= 8:
                                                                    if board[counter - 40] not in friends:
                                                                        if board[counter - 40] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 40] = 'R'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 40] = 'R'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter - 40) >= 8:
                                                                                if board[counter - 48] not in friends:
                                                                                    if board[counter - 48] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 48] = 'R'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 48] = 'R'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 48) >= 8:
                                                                                            if board[counter - 56] not in friends:
                                                                                                if board[counter - 56] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 56] = 'R'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 56] = 'R'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter <= 55:
                    if board[counter + 8] not in friends:
                        if board[counter + 8] in opponents:
                            newboard = list.copy(board)
                            newboard[counter + 8] = 'R'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 8] = 'R'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter + 8) <= 55:
                                if board[counter + 16] not in friends:
                                    if board[counter + 16] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 16] = 'R'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 16] = 'R'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter + 16) <= 55:
                                            if board[counter + 24] not in friends:
                                                if board[counter + 24] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 24] = 'R'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 24] = 'R'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter + 24) <= 55:
                                                        if board[counter + 32] not in friends:
                                                            if board[counter + 32] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 32] = 'R'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 32] = 'R'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 32) <= 55:
                                                                    if board[counter + 40] not in friends:
                                                                        if board[counter + 40] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 40] = 'R'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 40] = 'R'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter + 40) <= 55:
                                                                                if board[counter + 48] not in friends:
                                                                                    if board[counter + 48] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 48] = 'R'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 48] = 'R'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 48) <= 55:
                                                                                            if board[counter + 56] not in friends:
                                                                                                if board[counter + 56] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 56] = 'R'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(
                                                                                                        newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 56] = 'R'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
            if i == 'B':
                if counter % 8 != 0 and counter >=8:
                    if board[counter-9] not in friends:
                        if board[counter - 9] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 9] = 'B'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 9] = 'B'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-9) % 8 != 0 and (counter-9) >=8:
                                if board[counter - 18] not in friends:
                                    if board[counter - 18] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 18] = 'B'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 18] = 'B'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter - 18) % 8 != 0 and (counter - 18) >=8:
                                            if board[counter - 27] not in friends:
                                                if board[counter - 27] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 27] = 'B'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 27] = 'B'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter - 27) % 8 != 0 and (counter - 27) >=8:
                                                        if board[counter - 36] not in friends:
                                                            if board[counter - 36] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 36] = 'B'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 36] = 'B'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter - 36) % 8 != 0 and (counter - 36) >=8:
                                                                    if board[counter - 45] not in friends:
                                                                        if board[counter - 45] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 45] = 'B'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 45] = 'B'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter - 45) % 8 != 0 and (counter - 45) >=8:
                                                                                if board[counter - 54] not in friends:
                                                                                    if board[counter - 54] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 54] = 'B'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 54] = 'B'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 54) % 8 != 0 and (counter - 54) >=8:
                                                                                            if board[counter - 63] not in friends:
                                                                                                if board[counter - 63] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 63] = 'B'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 63] = 'B'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 7 and counter >=8:
                    if board[counter-7] not in friends:
                        if board[counter - 7] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 7] = 'B'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 7] = 'B'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-7) % 8 != 7 and (counter-7) >=8:
                                if board[counter - 14] not in friends:
                                    if board[counter - 14] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 14] = 'B'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 14] = 'B'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter-14) % 8 != 7 and (counter-14) >=8:
                                            if board[counter - 21] not in friends:
                                                if board[counter - 21] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 21] = 'B'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 21] = 'B'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter-21) % 8 != 7 and (counter-21) >=8:
                                                        if board[counter - 28] not in friends:
                                                            if board[counter - 28] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 28] = 'B'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 28] = 'B'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter- 28) % 8 != 7 and (counter-28) >=8:
                                                                    if board[counter - 35] not in friends:
                                                                        if board[counter - 35] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 35] = 'B'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 35] = 'B'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter-35) % 8 != 7 and (counter-35) >=8:
                                                                                if board[counter - 42] not in friends:
                                                                                    if board[counter - 42] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 42] = 'B'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 42] = 'B'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 42) % 8 != 7 and (counter - 42) >=8:
                                                                                            if board[counter - 49] not in friends:
                                                                                                if board[counter - 49] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 49] = 'B'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 49] = 'B'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 7 and counter <=55:
                    if board[counter+9] not in friends:
                        if board[counter + 9] in opponents:
                            newboard = list.copy(board)
                            newboard[counter + 9] = 'B'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 9] = 'B'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter+9) % 8 != 7 and (counter+9) <=55:
                                if board[counter + 18] not in friends:
                                    if board[counter + 18] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 18] = 'B'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 18] = 'B'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter + 18) % 8 != 7 and (counter + 18) <=55:
                                            if board[counter + 27] not in friends:
                                                if board[counter + 27] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 27] = 'B'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 27] = 'B'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter + 27) % 8 != 7 and (counter + 27) <=55:
                                                        if board[counter + 36] not in friends:
                                                            if board[counter + 36] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 36] = 'B'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 36] = 'B'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 36) % 8 != 7 and (counter + 36) <=55:
                                                                    if board[counter + 45] not in friends:
                                                                        if board[counter + 45] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 45] = 'B'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 45] = 'B'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter + 45) % 8 != 7 and (counter + 45) <=55:
                                                                                if board[counter + 54] not in friends:
                                                                                    if board[counter + 54] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 54] = 'B'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 54] = 'B'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 54) % 8 != 7 and (counter + 54) <=55:
                                                                                            if board[counter + 63] not in friends:
                                                                                                if board[counter + 63] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 63] = 'B'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 63] = 'B'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 0 and counter <=55:
                    if board[counter+7] not in friends:
                        if board[counter + 7] in opponents:
                            newboard = list.copy(board)
                            newboard[counter + 7] = 'B'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 7] = 'B'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter+7) % 8 != 0 and (counter+7) <=55:
                                if board[counter + 14] not in friends:
                                    if board[counter + 14] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 14] = 'B'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 14] = 'B'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter+14) % 8 != 0 and (counter+14) <=55:
                                            if board[counter + 21] not in friends:
                                                if board[counter + 21] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 21] = 'B'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 21] = 'B'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter+21) % 8 != 0 and (counter+21) <=55:
                                                        if board[counter + 28] not in friends:
                                                            if board[counter + 28] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 28] = 'B'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 28] = 'B'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 28) % 8 != 0 and (counter+28) <=55:
                                                                    if board[counter + 35] not in friends:
                                                                        if board[counter + 35] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 35] = 'B'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 35] = 'B'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter+35) % 8 != 0 and (counter+35) <=55:
                                                                                if board[counter + 42] not in friends:
                                                                                    if board[counter + 42] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 42] = 'B'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 42] = 'B'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 42) % 8 != 0 and (counter + 42) <=55:
                                                                                            if board[counter + 49] not in friends:
                                                                                                if board[counter + 49] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 49] = 'B'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 49] = 'B'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
            if i == 'Q':
                if counter % 8 != 0 and counter >=8:
                    if board[counter-9] not in friends:
                        if board[counter - 9] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 9] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 9] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-9) % 8 != 0 and (counter-9) >=8:
                                if board[counter - 18] not in friends:
                                    if board[counter - 18] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 18] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 18] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter - 18) % 8 != 0 and (counter - 18) >=8:
                                            if board[counter - 27] not in friends:
                                                if board[counter - 27] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 27] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 27] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter - 27) % 8 != 0 and (counter - 27) >=8:
                                                        if board[counter - 36] not in friends:
                                                            if board[counter - 36] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 36] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 36] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter - 36) % 8 != 0 and (counter - 36) >=8:
                                                                    if board[counter - 45] not in friends:
                                                                        if board[counter - 45] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 45] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 45] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter - 45) % 8 != 0 and (counter - 45) >=8:
                                                                                if board[counter - 54] not in friends:
                                                                                    if board[counter - 54] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 54] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 54] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 54) % 8 != 0 and (counter - 54) >=8:
                                                                                            if board[counter - 63] not in friends:
                                                                                                if board[counter - 63] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 63] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 63] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 7 and counter >=8:
                    if board[counter-7] not in friends:
                        if board[counter - 7] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 7] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 7] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-7) % 8 != 7 and (counter-7) >=8:
                                if board[counter - 14] not in friends:
                                    if board[counter - 14] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 14] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 14] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter-14) % 8 != 7 and (counter-14) >=8:
                                            if board[counter - 21] not in friends:
                                                if board[counter - 21] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 21] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 21] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter-21) % 8 != 7 and (counter-21) >=8:
                                                        if board[counter - 28] not in friends:
                                                            if board[counter - 28] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 28] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 28] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter- 28) % 8 != 7 and (counter-28) >=8:
                                                                    if board[counter - 35] not in friends:
                                                                        if board[counter - 35] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 35] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 35] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter-35) % 8 != 7 and (counter-35) >=8:
                                                                                if board[counter - 42] not in friends:
                                                                                    if board[counter - 42] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 42] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 42] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 42) % 8 != 7 and (counter - 42) >=8:
                                                                                            if board[counter - 49] not in friends:
                                                                                                if board[counter - 49] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 49] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 49] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 7 and counter <=55:
                    if board[counter+9] not in friends:
                        if board[counter + 9] in opponents:
                            newboard = list.copy(board)
                            newboard[counter + 9] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 9] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter+9) % 8 != 7 and (counter+9) <=55:
                                if board[counter + 18] not in friends:
                                    if board[counter + 18] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 18] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 18] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter + 18) % 8 != 7 and (counter + 18) <=55:
                                            if board[counter + 27] not in friends:
                                                if board[counter + 27] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 27] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 27] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter + 27) % 8 != 7 and (counter + 27) <=55:
                                                        if board[counter + 36] not in friends:
                                                            if board[counter + 36] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 36] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 36] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 36) % 8 != 7 and (counter + 36) <=55:
                                                                    if board[counter + 45] not in friends:
                                                                        if board[counter + 45] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 45] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 45] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter + 45) % 8 != 7 and (counter + 45) <=55:
                                                                                if board[counter + 54] not in friends:
                                                                                    if board[counter + 54] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 54] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 54] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 54) % 8 != 7 and (counter + 54) <=55:
                                                                                            if board[counter + 63] not in friends:
                                                                                                if board[counter + 63] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 63] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 63] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 0 and counter <=55:
                    if board[counter+7] not in friends:
                        if board[counter + 7] in opponents:
                            newboard = list.copy(board)
                            newboard[counter + 7] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 7] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter+7) % 8 != 0 and (counter+7) <=55:
                                if board[counter + 14] not in friends:
                                    if board[counter + 14] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 14] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 14] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter+14) % 8 != 0 and (counter+14) <=55:
                                            if board[counter + 21] not in friends:
                                                if board[counter + 21] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 21] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 21] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter+21) % 8 != 0 and (counter+21) <=55:
                                                        if board[counter + 28] not in friends:
                                                            if board[counter + 28] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 28] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 28] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 28) % 8 != 0 and (counter+28) <=55:
                                                                    if board[counter + 35] not in friends:
                                                                        if board[counter + 35] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 35] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 35] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter+35) % 8 != 0 and (counter+35) <=55:
                                                                                if board[counter + 42] not in friends:
                                                                                    if board[counter + 42] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 42] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 42] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 42) % 8 != 0 and (counter + 42) <=55:
                                                                                            if board[counter + 49] not in friends:
                                                                                                if board[counter + 49] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 49] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 49] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)

                if counter % 8 != 0:
                    if board[counter-1] not in friends:
                        if board[counter - 1] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 1] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 1] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-1) % 8 != 0:
                                if board[counter - 2] not in friends:
                                    if board[counter - 2] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 2] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 2] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter - 2) % 8 != 0:
                                            if board[counter - 3] not in friends:
                                                if board[counter - 3] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 3] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 3] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter - 3) % 8 != 0:
                                                        if board[counter - 4] not in friends:
                                                            if board[counter - 4] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 4] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 4] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter - 4) % 8 != 0:
                                                                    if board[counter - 5] not in friends:
                                                                        if board[counter - 5] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 5] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 5] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter - 5) % 8 != 0:
                                                                                if board[counter - 6] not in friends:
                                                                                    if board[counter - 6] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 6] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 6] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 6) % 8 != 0:
                                                                                            if board[counter - 7] not in friends:
                                                                                                if board[counter - 7] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 7] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 7] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter % 8 != 7:
                    if board[counter + 1] not in friends:
                        if board[counter + 1] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 1] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 1] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter + 1) % 8 != 7:
                                if board[counter + 2] not in friends:
                                    if board[counter + 2] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 2] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 2] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter + 2) % 8 != 7:
                                            if board[counter + 3] not in friends:
                                                if board[counter + 3] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 3] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 3] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter + 3) % 8 != 7:
                                                        if board[counter + 4] not in friends:
                                                            if board[counter + 4] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 4] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 4] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 4) % 8 != 7:
                                                                    if board[counter + 5] not in friends:
                                                                        if board[counter + 5] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 4] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 5] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter + 5) % 8 != 7:
                                                                                if board[counter + 6] not in friends:
                                                                                    if board[counter + 6] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 6] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 6] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 6) % 8 != 7:
                                                                                                if board[counter + 7] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 7] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 7] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter >= 8:
                    if board[counter-8] not in friends:
                        if board[counter - 8] in opponents:
                            newboard = list.copy(board)
                            newboard[counter - 8] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter - 8] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter-8) >= 8:
                                if board[counter - 16] not in friends:
                                    if board[counter - 16] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter - 16] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter - 16] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter - 16) >= 8:
                                            if board[counter - 24] not in friends:
                                                if board[counter - 24] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 24] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter - 24] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter - 24) >= 8:
                                                        if board[counter - 32] not in friends:
                                                            if board[counter - 32] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 32] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter - 32] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter - 32) >= 8:
                                                                    if board[counter - 40] not in friends:
                                                                        if board[counter - 40] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 40] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter - 40] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter - 40) >= 8:
                                                                                if board[counter - 48] not in friends:
                                                                                    if board[counter - 48] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 48] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter - 48] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter - 48) >= 8:
                                                                                            if board[counter - 56] not in friends:
                                                                                                if board[counter - 56] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 56] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter - 56] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                if counter <= 55:
                    if board[counter+8] not in friends:
                        if board[counter + 8] in opponents:
                            newboard = list.copy(board)
                            newboard[counter + 8] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                        else:
                            newboard = list.copy(board)
                            newboard[counter + 8] = 'Q'
                            newboard[counter] = '.'
                            boards.append(newboard)
                            if (counter+8) <= 55:
                                if board[counter + 16] not in friends:
                                    if board[counter + 16] in opponents:
                                        newboard = list.copy(board)
                                        newboard[counter + 16] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                    else:
                                        newboard = list.copy(board)
                                        newboard[counter + 16] = 'Q'
                                        newboard[counter] = '.'
                                        boards.append(newboard)
                                        if (counter + 16) <= 55:
                                            if board[counter + 24] not in friends:
                                                if board[counter + 24] in opponents:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 24] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                else:
                                                    newboard = list.copy(board)
                                                    newboard[counter + 24] = 'Q'
                                                    newboard[counter] = '.'
                                                    boards.append(newboard)
                                                    if (counter + 24) <= 55:
                                                        if board[counter + 32] not in friends:
                                                            if board[counter + 32] in opponents:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 32] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                            else:
                                                                newboard = list.copy(board)
                                                                newboard[counter + 32] = 'Q'
                                                                newboard[counter] = '.'
                                                                boards.append(newboard)
                                                                if (counter + 32) <= 55:
                                                                    if board[counter + 40] not in friends:
                                                                        if board[counter + 40] in opponents:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 40] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                        else:
                                                                            newboard = list.copy(board)
                                                                            newboard[counter + 40] = 'Q'
                                                                            newboard[counter] = '.'
                                                                            boards.append(newboard)
                                                                            if (counter + 40) <= 55:
                                                                                if board[counter + 48] not in friends:
                                                                                    if board[counter + 48] in opponents:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 48] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                    else:
                                                                                        newboard = list.copy(board)
                                                                                        newboard[counter + 48] = 'Q'
                                                                                        newboard[counter] = '.'
                                                                                        boards.append(newboard)
                                                                                        if (counter + 48) <= 55:
                                                                                            if board[counter + 56] not in friends:
                                                                                                if board[counter + 56] in opponents:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 56] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)
                                                                                                else:
                                                                                                    newboard = list.copy(board)
                                                                                                    newboard[counter + 56] = 'Q'
                                                                                                    newboard[counter] = '.'
                                                                                                    boards.append(newboard)

            counter += 1
    return(boards)
def readable(boards):

    for board in boards:
        row1 = []
        row2 = []
        row3 = []
        row4 = []
        row5 = []
        row6 = []
        row7 = []
        row8 = []
        counter = 0
        for item in board:
            if counter <=7:
                row1.append(item)
            elif counter <= 15:
                row2.append(item)
            elif counter <= 23:
                row3.append(item)
            elif counter <= 31:
                row4.append(item)
            elif counter <= 39:
                row5.append(item)
            elif counter <= 47:
                row6.append(item)
            elif counter <= 55:
                row7.append(item)
            else:
                row8.append(item)
            counter += 1
        print(row1)
        print(row2)
        print(row3)
        print(row4)
        print(row5)
        print(row6)
        print(row7)
        print(row8)
        print("Board Done")


startboard = "RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr"
print(len(startboard))
board =[]
for i in startboard:
    board.append(i)
boards = legal_moves(board, 'black')

readable(boards)