@jit()
def get_field(ped_list, ped_coords):
    potentials = []
    for ped in ped_list:
        M = np.zeros([20,150])
        M[ped_coords[:,0], ped_coords[:,1]] = -1
        M[ped_coords[ped,0]][ped_coords[ped,1]] = 0;
        for n in range(50):
            for j in range(len(M[0,:])-1):
                for i in range(len(M[:,0])-1):
                    if M[i][j] != (1|-1):
                        M[i,j] = 1/4 * (M[i-1][j] + M[i+1][j] + M[i][j-1] + M[i][j+1])
                    else:
                        pass
        potentials.append(M)
    return potentials