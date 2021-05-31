#import a4.utility as utility
#import a4.loader as loader
import copy

import numpy as np
import loader
import utility

# Correction: Best VRP Distance: 787.81
# Nearest Neighbour VRP Heuristic Distance: 1146.40
# Saving VRP Heuristic Distance: 843.69

def main():

    # Paths to the data and solution files.
    vrp_file = "n80-k10.vrp"  # "data/n80-k10.vrp"
    sol_file = "n80-k10.sol"  # "data/n80-k10.sol"

    vrp_file80 = "n80-k10.vrp"
    sol_file80 = "n80-k10.sol"

    # Loading the VRP data file.
    px, py, demand, capacity, depot = loader.load_data(vrp_file)




    # Displaying to console the distance and visualizing the optimal VRP solution.
    vrp_best_sol = loader.load_solution(sol_file)
    best_distance = utility.calculate_total_distance(vrp_best_sol, px, py, depot)
    print("Best VRP Distance:", best_distance)
    utility.visualise_solution(vrp_best_sol, px, py, depot, "Optimal Solution")

    # Executing and visualizing the nearest neighbour VRP heuristic.
    # Uncomment it to do your assignment!

    nnh_solution = nearest_neighbour_heuristic(px, py, demand, capacity, depot)
    nnh_distance = utility.calculate_total_distance(nnh_solution, px, py, depot)
    print("Nearest Neighbour VRP Heuristic Distance:", nnh_distance)
    utility.visualise_solution(nnh_solution, px, py, depot, "Nearest Neighbour Heuristic")

    # Executing and visualizing the saving VRP heuristic.
    # Uncomment it to do your assignment!
    
    sh_solution = savings_heuristic(px, py, demand, capacity, depot)
    sh_distance = utility.calculate_total_distance(sh_solution, px, py, depot)
    print("Saving VRP Heuristic Distance:", sh_distance)
    utility.visualise_solution(sh_solution, px, py, depot, "Savings Heuristic")




def nearest_neighbour_heuristic(px, py, demand, capacity, depot):

    """
    Algorithm for the nearest neighbour heuristic to generate VRP solutions.

    :param px: List of X coordinates for each node.
    :param py: List of Y coordinates for each node.
    :param demand: List of each nodes demand.
    :param capacity: Vehicle carrying capacity.
    :param depot: Depot.
    :return: List of vehicle routes (tours).
    """

    # TODO - Implement the Nearest Neighbour Heuristic to generate VRP solutions.
    Len = len(demand)
    routes = []
    eMat = utility.euclidean_matrix(px,py)
    visitedNodes = [depot]
    demandLeft = copy.deepcopy(demand)
    demandLeft[depot] = float('inf')

    while len(visitedNodes)< Len: # loop runs while nodes left to be visited
        oneRoute = []
        cap = capacity #100
        selNode = depot

        while (cap>0): # while vehicle has capacity
            ascEuc = np.unique(eMat[selNode]) #eucDistanc in ascending order

            for i in ascEuc: # for each h value starting with lowest
                indexList = np.where(i == eMat[selNode])[0]
                indexNo = np.where(i == eMat[selNode])[0][0]
                if len(indexList) > 1:
                    for j in indexList:
                        if (j not in visitedNodes) & (demand[j] <= cap):
                            indexNo = j
                            break
                        else:
                            continue

                if (indexNo not in visitedNodes) & (demand[indexNo] <= cap):
                    visitedNodes.append(indexNo)
                    oneRoute.append(indexNo)
                    cap -= demand[indexNo]
                    demandLeft[indexNo] = float('inf')
                    selNode = indexNo
                    break

            if demandLeft.min() > cap:
                break


        routes.append(oneRoute)



    return np.array(routes,dtype= object)


def savings_heuristic(px, py, demand, capacity, depot):

    """
    Algorithm for Implementing the savings heuristic to generate VRP solutions.

    :param px: List of X coordinates for each node.
    :param py: List of Y coordinates for each node.
    :param demand: List of each nodes demand.
    :param capacity: Vehicle carrying capacity.
    :param depot: Depot.
    :return: List of vehicle routes (tours).
    """
    sMat = utility.savings_matrix(px,py, depot) # 32 x 32, depot not taken out.
    bestSave = np.unique(sMat) # list of best saving

    allroutes = [] #list of lists [[][]] with [depot,index numbers,depot].
    for i in range(len(px)):
        if i == depot:
            continue
        else:
            allroutes.append([depot,i,depot])

    while(True):

        #identify best saving from bestSave
        firstSaving = np.where(sMat == bestSave.max())
        head = firstSaving[0][0]
        tail = firstSaving[1][0]
        headloc = 0
        tailloc = 0
        #something to check whether head and tail in same group already
        #location in allroutes of head and tail
        for i in range(len(allroutes)):
            if head in allroutes[i]:
                headloc = i
            if tail in allroutes[i]:
                tailloc = i

        #check demand of head and tail
        demC = 0

        for i in allroutes[headloc]:
            demC += demand[i]
        for i in allroutes[tailloc]:
            demC += demand[i]

        #if demand does not exceed capacity, proceed with adding
        if demC <= capacity:
            # append two links head to tail
            allroutes[headloc] = allroutes[headloc][:-1] + allroutes[tailloc][1:]
            for i in allroutes[headloc]:
                if i ==0:
                    continue
                else:
                    for j in allroutes[headloc]:
                        if j==0:
                            continue
                        else:
                            sMat[i,j] = 0
            allroutes.remove(allroutes[tailloc])
            #delete head row in sMat
            sMat[head,:] = 0
            sMat[tail,head] = 0
            #delete tail column in sMat
            sMat[:,tail] = 0
            sMat[head,tail] = 0

            bestSave = np.unique(sMat)
        else:
            sMat[head,tail] =0
            sMat[tail,head] =0
            bestSave = np.unique(sMat)

        # for each list in allroutes, check if 2 smallest cumulative demand of lists are over 100. stop loop
        routedem = []
        for i in allroutes:
            dem=0
            for j in i:
                dem += demand[j]
            routedem.append(dem)
        A, B = sorted(routedem)[:2]
        if (A + B) > 100:
            break


    for i in range(len(allroutes)):
        allroutes[i]= allroutes[i][1:-1]

    return np.array(allroutes,dtype=object)


if __name__ == '__main__':
    main()
