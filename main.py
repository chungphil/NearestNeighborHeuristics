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
    vrp_file = "n32-k5.vrp"  # "data/n80-k10.vrp"
    sol_file = "n32-k5.sol"  # "data/n80-k10.sol"

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

    # nnh_solution = nearest_neighbour_heuristic(px, py, demand, capacity, depot)
    # nnh_distance = utility.calculate_total_distance(nnh_solution, px, py, depot)
    # print("Nearest Neighbour VRP Heuristic Distance:", nnh_distance)
    # utility.visualise_solution(nnh_solution, px, py, depot, "Nearest Neighbour Heuristic")

    # Executing and visualizing the saving VRP heuristic.
    # Uncomment it to do your assignment!
    
    # sh_solution = savings_heuristic(px, py, demand, capacity, depot)
    # sh_distance = utility.calculate_total_distance(sh_solution, px, py, depot)
    # print("Saving VRP Heuristic Distance:", sh_distance)
    # utility.visualise_solution(sh_solution, px, py, depot, "Savings Heuristic")


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

    routes = []
    eMat = utility.euclidean_matrix(px,py)

    nodesLeft = len(capacity) - 1 #31

    while (nodesLeft>=0):
        oneRoute = []
        cap = capacity #100
        fInd = np.where(eMat[0] == eMat[0,1:].min())[0][0] #index of min h value
        cap -= demand[fInd] # take demand away from capacity
        while (cap>0):
            oneRoute.append(fInd)



    return None


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

    # TODO - Implement the Saving Heuristic to generate VRP solutions.

    return None


if __name__ == '__main__':
    main()
