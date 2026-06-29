import os.path
import sys
import networkx as nx
import numpy as np

# Test 1 Modularity
def test_1_modularity():

    # Check if the file exists
    try:
        exists=os.path.isfile("assignment.py")
        assert exists, "The file 'assignment.py' doesn't exist"
    except AssertionError as e:
        print(e)
        sys.exit(1)
    
    # Check if the function is defined within the script
    sys.path.append("./")
    try:
        from assignment import modularity
    except ImportError as e:
        print(f"Error importing function: {e}")
        sys.exit(1)

    # Check the output of the function
    g2=nx.karate_club_graph()
    part=[{8, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33},{1, 2, 3, 7, 9, 12, 13, 17, 21},{0, 4, 5, 6, 10, 11, 16, 19}]
    assert round(modularity(g2,part),10) == 0.3806706114, "The output of the function is not correct"


# Test 2 Girvan-Newman
def test_2_girvan_newman():

    # Check if the file exists
    try:
        exists=os.path.isfile("assignment.py")
        assert exists, "The file 'assignment.py' doesn't exist"
    except AssertionError as e:
        print(e)
        sys.exit(1)
    
    # Check if the function is defined within the script
    sys.path.append("./")
    try:
        from assignment import girvan_newman_communities
    except ImportError as e:
        print(f"Error importing function: {e}")
        sys.exit(1)
        
    # Check the output of the function
    g2=nx.karate_club_graph()
    part, m, evo = girvan_newman_communities(g2)
    
    assert set([x for i in range(len(part)) for x in part[i]])==set(g2.nodes()), "The partition is not correct"
    assert m > 0.38, "The modularity of the best partition is not correct"
    assert m==np.max(evo), "The highest modularity is not in the elements of the list"

