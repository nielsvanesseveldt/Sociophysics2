import numpy
import random

def laplace_eq(M):
    for n in range(150):
        for j in range(len(M[0,:])-1):
            for i in range(len(M[:,0])-1):
                if M[i][j] == 1:
                    pass
                elif M[i][j] ==-1:
                    pass
                else:
                    M[i,j] = 1/4 * (M[i-1][j] + M[i+1][j] + M[i][j-1] + M[i][j+1])
    return M

def get_prob(ped_ID):
    # Get the specific distribution map
    # Function: mp = get_prob_map(ped_ID)
    # Get current Square:
    x = ped[ped_ID][1][0]
    y = ped[ped_ID][1][1]
    tot = mp[y+1][x-1] + mp[y+1][x] + mp[y+1][x+1] + mp[y][x-1] + mp[y][x] + mp[y][x+1] + mp[y-1][x-1] + mp[y-1][x] + mp[y-1][x+1]
    squares = []
    for a in range(-1, 2):
        for b in range(-1, 2):
            # Will have to be changed to the exponential method mentioned by Corbetta
            squares.append(mp[y+a][x+b]/tot)
    return squares

def make_decision(normalized_squares):
    sum_prob = 0
    choice = random.randint(0, 100)/100
    for i in range(0 ,9):
        if (choice >= sum_prob) and (choice <= (sum_prob+normalized_squares[i])):

            decided_square = i
        sum_prob += normalized_squares[i]
    return decided_square