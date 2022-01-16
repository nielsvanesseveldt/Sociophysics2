import numpy as np
import random
from numba import jit

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
    x = ped_list[ped_ID][1][0]
    y = ped_list[ped_ID][1][1]
    
#move pedestrian sideways    
    if (((decided_square == 2) or (decided_square == 5) or (decided_square == 8)) and (x < 120)):
        ped_list[ped_ID][1][0] += 1
    elif (((decided_square == 0) or (decided_square == 3) or (decided_square == 6)) and (x > 0)):
        ped_list[ped_ID][1][0] -= 1
        
#move pedestrian up and down
    if (((decided_square == 0) or (decided_square == 1) or (decided_square == 2)) and (y > 0 )):
        ped_list[ped_ID][1][1] -= 1
    elif (((decided_square == 6) or (decided_square == 7) or (decided_square == 8)) and (y < 21)):
        ped_list[ped_ID][1][1] += 1
    return ped_list
        
def generate_ped(ped_list, min_ped, max_ped):
    # Choose random nr pedestrians to be added, depending on given min and max conditions
    nr_ped = random.randint(min_ped, max_ped)
    for p in range(nr_ped):
        start_pos = [random.randint(5, 15), random.randint(1,3)]
        while True:
            goal_coord = np.random.exponential(scale = 1)
            if goal_coord <= 1:
                goal_coord = int(np.rint(119*goal_coord))
                break
            else:
                pass
        goal = [random.randint(0,20), goal_coord]
        ped_list.append([goal, start_pos])
    return ped_list

@jit(nopython = True)
def laplace_solve(M):
    for n in range(50):
        for j in range(len(M[0,:])-1):
            for i in range(len(M[:,0])-1):
                if M[i][j] != 1:
                    if M[i][j] != -1:
                        if M[i][j] != 5:
                            M[i,j] = 1/4 * (M[i-1][j] + M[i+1][j] + M[i][j-1] + M[i][j+1])
                else:
                    pass
    return M
    

def get_field(ped_list):
    potentials = []
    ped_list_array = np.array(ped_list)
    for pedest in range(len(ped_list)):
        try:
            M = np.zeros([21,120]) #new grid size
            M[0,:] = -1 #boundaries
            M[-1,:] = -1
            M[:,0] = -1
            M[:,-1] = -1
            M[7,51:82] = 1 #bench coords
            M[10,98:105] = 1
            M[15,51:82] = 1
            M[12,98:105] = 1
            M[ped_list_array[:,1, 0], ped_list_array[:,1, 1]] = -1
            M[ped_list_array[pedest,1, 0], ped_list_array[pedest,1, 1]] = 0
            M[ped_list_array[pedest,0, 0], ped_list_array[pedest,0, 1]] = 5 #goals, the value 5 is arbitrary
            potentials.append(laplace_solve(M))
        except:
            pass
    return potentials