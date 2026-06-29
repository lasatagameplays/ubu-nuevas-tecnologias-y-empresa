import os.path
import sys
import networkx as nx
import random

# Test 1 for the random vaccine strategy
def test_1():

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
        from assignment import random_vaccine
    except ImportError as e:
        print(f"Error importing function: {e}")
        sys.exit(1)

    # Check the function output
    g2=nx.karate_club_graph()
    assert round(random_vaccine(g2),10) == 4.5882352941, "The random vaccine strategy is not working as expected"
        

# Test 2 for the indirect random vaccine strategy
def test_2():

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
        from assignment import indirect_random_vaccine
    except ImportError as e:
        print(f"Error importing function: {e}")
        sys.exit(1)

    # Check the function output
    g2=nx.karate_club_graph()
    assert round(indirect_random_vaccine(g2),10) == 9.6102100154, "The indirect random vaccine strategy is not working as expected"
