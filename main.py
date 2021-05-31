#import a4.utility as utility
#import a4.loader as loader
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

    # Loading the VRP data file.
    px, py, demand, capacity, depot = loader.load_data(vrp_file)
    # px , py , demand(sum demand is 410) arrays of values, capacity is 100 for 5 vehicles, depot is at px[0] and py[0]

    # print(px)
    # print(py)
    # print(demand)
    # print(capacity)
    # print(np.sum(demand))
    # print(depot)

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
    demandLeft = demand
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
    bestSave = np.unique(sMat)[::-1]

    allroutes = [] #list of lists [[][]] with index numbers.
    for i in range(len(px)):
        if i == depot:
            continue
        else:
            allroutes.append([i])

    return None


if __name__ == '__main__':
    main()
