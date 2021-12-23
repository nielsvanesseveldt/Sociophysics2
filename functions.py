import numpy as np
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

def get_prob(ped_list, ped_ID, field_list):
    # Get the specific distribution map
    mp = field_list[ped_ID]
    # Get current Square:
    x = ped_list[ped_ID][1][0]
    y = ped_list[ped_ID][1][1]
    tot = mp[y+1][x-1] + mp[y+1][x] + mp[y+1][x+1] + mp[y][x-1] + mp[y][x] + mp[y][x+1] + mp[y-1][x-1] + mp[y-1][x] + mp[y-1][x+1]
    squares = []
    for a in range(-1, 2):
        for b in range(-1, 2):
            # Will have to be changed to the exponential method mentioned by Corbetta
            squares.append(mp[y+a][x+b]/tot)
    return squares

def make_decision(normalized_squares):
    sum_prob = 0
    decided_square = -1
    choice = random.randint(0, 100)/100
    for i in range(0 ,9):
        if (choice >= sum_prob) and (choice <= (sum_prob+normalized_squares[i])):
            decided_square = i
        sum_prob += normalized_squares[i]
    return decided_square

def move_ped(ped_list, ped_ID, decided_square):
#move pedestrian sideways
    if ((decided_square == 2) or (decided_square == 5) or (decided_square == 8)):
        ped_list[ped_ID][1][0] += 1
    elif ((decided_square == 0) or (decided_square == 3) or (decided_square == 6)):
        ped_list[ped_ID][1][0] -= 1
    
#move pedestrian up and down
    if ((decided_square == 0) or (decided_square == 1) or (decided_square == 2)):
        ped_list[ped_ID][1][1] -= 1
    elif ((decided_square == 6) or (decided_square == 7) or (decided_square == 8)):
        ped_list[ped_ID][1][1] += 1
        
def generate_ped(ped_list, min_ped, max_ped):
    # Choose random nr pedestrians to be added, depending on given min and max conditions
    nr_ped = random.randint(min_ped, max_ped)
    for p in range(nr_ped):
        start_pos = [random.randint(5, 15), random.randint(0,2)]
        goal = [random.randint(0,20), random.randint(0,150)]
        ped_list.append([goal, start_pos])
    return ped_list

def get_field(ped_list):
    potentials = []
    ped_list_array = np.array(ped_list)
    for ped in range(len(ped_list)):
        M = np.zeros([20,150])
        M[ped_list_array[:,1, 0], ped_list_array[:,1, 1]] = -1
        M[ped_list_array[ped,1, 0], ped_list_array[ped,1, 1]] = 0;
        for n in range(50):
            for j in range(len(M[0,:])-1):
                for i in range(len(M[:,0])-1):
                    if M[i][j] != (1|-1):
                        M[i,j] = 1/4 * (M[i-1][j] + M[i+1][j] + M[i][j-1] + M[i][j+1])
                    else:
                        pass
        potentials.append(M)
    return potentials