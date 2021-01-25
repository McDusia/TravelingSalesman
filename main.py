import copy

from mpi4py import MPI

n = 4
matrix = [[0 for _ in range(n)] for _ in range(n)]
a_min = 1000
best_visited_nodes_order = [0 for _ in range(n)]


def create_graph_matrix():
    matrix[0][1] = 2
    matrix[1][0] = 2
    matrix[0][2] = 1
    matrix[2][0] = 1
    matrix[0][3] = 3
    matrix[3][0] = 3
    matrix[3][1] = 1
    matrix[1][3] = 1
    matrix[3][2] = 1
    matrix[2][3] = 1
    print(matrix)


# Proc to evaluate path from prev_node to node_nr using current_solution
def evaluate(prev_node, node_nr, current_solution):
    print("Evaluate ", prev_node, node_nr, "Current Solution ", current_solution)
    print(matrix[prev_node][node_nr])
    result = current_solution + matrix[prev_node][node_nr]
    return result


def bbsearch():
    visited_nodes_order = [-1 for _ in range(n)]

    print("VisitedNodesOrder, lets start...")
    print(visited_nodes_order)

    bbsearch_1(0, 0, visited_nodes_order, 0, 0)


def bbsearch_1(prev_node, current_node_nr, visited_nodes_order, current_solution, visited_nodes_quantity):
    score = evaluate(prev_node, current_node_nr, current_solution)
    current_solution = score
    print("Score ", score)
    global a_min
    global n
    if score <= a_min:
        visited_nodes_order[visited_nodes_quantity] = current_node_nr

        print("VisitedNodesOrder ", visited_nodes_order)
        visited_nodes_quantity += 1
        print("VisitedNodesQuantity ", visited_nodes_quantity)

        if visited_nodes_quantity == n:
            print("Hey, VisitedNodesQuantity == n")
            if matrix[0][current_node_nr] != 0:
                a_min = score
                global best_visited_nodes_order
                best_visited_nodes_order = visited_nodes_order
                print("Now, VisitedNodesOrder ", visited_nodes_order)
                return visited_nodes_order
            else:
                print("Unfortunately, such order has not cycle")
                tab = [-1 for _ in range(n)]
                for i in range(n):
                    tab[i] = -1
                return tab
        else:
            for i in range(n):
                print(" Zobaczmy ", current_node_nr, i)
                print("Aktualne visited_nodes_order: ", visited_nodes_order)
                if matrix[current_node_nr][i] != 0 and i not in visited_nodes_order:
                    print("Call b&bsearch_1 for ", current_node_nr, ",", i)
                    bbsearch_1(current_node_nr, i, copy.deepcopy(visited_nodes_order), current_solution, visited_nodes_quantity)
            print("OK, I (", current_node_nr, ") want to finish, I called for children.")
    print("OK, I (", current_node_nr, ") want to finish. My solution is worse than CurrentSolution")
    tab = [-1 for _ in range(n)]
    for i in range(n):
        tab[i] = -1
    return tab


def traveling_salesman_problem_solver():
    print("Problem Komiwojaźera")
    create_graph_matrix()
    bbsearch()
    print(a_min)
    print(best_visited_nodes_order)


if __name__ == '__main__':
    traveling_salesman_problem_solver()
