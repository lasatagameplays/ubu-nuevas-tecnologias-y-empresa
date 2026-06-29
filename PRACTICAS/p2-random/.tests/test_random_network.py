# Test 1 for the random network generator

import os.path
import sys
import networkx as nx
import random

# Test 1 for the random network generator
def test_1():

    # Check if the file exists
    try:
        exists=os.path.isfile("assignment.py")
        assert exists, "The file 'assignment.py' doesn't exist"
    except AssertionError as e:
        print(e)
        sys.exit(1)
    
    # Check if the function is defined withn the script
    sys.path.append("./")
    try:
        from assignment import random_network
    except ImportError as e:
        print(f"Error importing function: {e}")
        sys.exit(1)

    # Check if the function returns a undirected networkx graph
    N=50
    p=0.05
    G = random_network(N, p)
    assert isinstance(G, nx.Graph)
    
    # Check if the number of nodes is correct
    assert G.number_of_nodes() == N

# Test 2 for the random network generator
def test_2():

    # Check if the file exists
    try:
        exists=os.path.isfile("assignment.py")
        assert exists, "The file 'assignment.py' doesn't exist"
    except AssertionError as e:
        print(e)
        sys.exit(1)
    
    # Check if the function is defined withn the script
    sys.path.append("./")
    try:
        from assignment import random_network
    except ImportError as e:
        print(f"Error importing function: {e}")
        sys.exit(1)

    # Check that the number of links is within the confidence interval of the average of a binomial
    random.seed(1234)
    N=1000
    p=0.005
    G = random_network(N, p)   
    avg_links =  p * N * (N - 1) / 2 
    std_dev = (p * (1-p)* N * (N - 1) / 2) ** 0.5
    num_links = G.number_of_edges()
    assert (avg_links - 3 * std_dev) <= num_links <= (avg_links + 3 * std_dev), "The number of links is not within the confidence interval of the average of a binomial"
