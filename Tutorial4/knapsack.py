import numpy as np

def knapsack(weights: list,values: list,W: int):
    n = len(weights)
    if len(values) != n:
        print("Values and Weights must have equal size")
        raise Exception

    dp_table = np.zeros((n,W)) #dynamic programming table initialized with 0's
    traceback = np.empty_like(dp_table) #this will keep a record of each choice taken by the algorithm so that the optimal solition can be contructed in the end
    for i in range(n):
        for j in range(W):
            if weights[i] > j:
                dp_table[i,j] = dp_table[i-1,j]
                traceback[i,j] = -1 #indicates that wi must not be taken in opt
            else:
                p0 = dp_table[i-1,j]
                p1 = dp_table[i-1,j-weights[i]] + values[i]
                if p0 > p1:
                    dp_table[i,j] = p0
                    traceback[i,j] = 0 #indicates that choice 0 was made to reach i,j also means that wi is not to be included in opt
                elif p1 > p0:
                    dp_table[i,j] = p1
                    traceback[i,j] = 1 #indicates that choice 1 was made to reach i,j also means wi is to be included in opt
                else: #p0 = p1
                    dp_table[i,j] = p1
                    traceback[i,j] = 2 #indicates that both choices were equal and represents a fork in the possible optimal paths
    max_value = dp_table[n-1,W-1]
    L = tracer((n-1,W-1),weights,traceback)
    return L, max_value

def tracer(coord: tuple,weights: list,traceback: np.ndarray):
    if coord[0] < 0 or coord[1] < 0:
        return []
    p = traceback[coord]
    if p == -1 or p == 0:
        coord_new = (coord[0]-1,coord[1])
        L = tracer(coord_new,weights,traceback)
    else:
        coord_new = (coord[0]-1,coord[1]-weights[coord[0]])
        L = tracer(coord_new,weights,traceback)
        L.append(coord[0])
    
    return L
    # else:
    #     coord_new1 = (coord[0]-1,coord[1])
    #     L1 = tracer(coord_new1,weights,traceback)
    #     for j in range(len(L)):
    #         L1[j].append(coord[0])
    #     coord_new2 = (coord[0]-1,coord[1])
    #     L2 = tracer(coord_new2,L,weights,traceback)
    #     for j in range(len(L)):
    #         L2[j].append(coord[0])
    #     L1.extend(L2)
    #     L
    
print(knapsack([2,2,3],[2,2,10],6))