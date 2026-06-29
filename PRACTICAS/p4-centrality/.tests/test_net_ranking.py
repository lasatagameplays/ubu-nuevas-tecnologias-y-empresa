import os.path
import sys
import networkx as nx
import pandas as pd

# Test 1
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
        from assignment import net_ranking
    except ImportError as e:
        print(f"Error importing function: {e}")
        sys.exit(1)

    # Check the output of the function
    g2=nx.karate_club_graph()
    df=net_ranking(g2,(0.75,0.25))
    assert isinstance(df,pd.DataFrame), "The output of the function should be a pandas DataFrame"
    assert df.iloc[1,0] == 33, "The ranking order is not correct"
    assert round(df.iloc[1,3],10) == 0.9237034175, "The average ranking is not correct"
