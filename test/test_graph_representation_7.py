import pytest
from collections import defaultdict
from student_code import TSPGraph  
import time
import math

def test_max_flow():
    st=TSPGraph()
    t = time.time()
    nodes=["a","b","c","d","e","f","g","h","i","j","k"]
    loc={}
    loc={'a': (37, 70), 'b': (7, 9), 'c': (48, 83), 'd': (42, 77), 'e': (13, 2), 'f': (50, 80), 'g': (88, 84), 'h': (48, 23), 'i': (11, 76), 'j': (91, 82), 'k': (81, 61)}
    for nd in nodes:
        for nd2 in nodes:
            loc1=loc[nd]
            loc2=loc[nd2]
            st.add_edge(nd,nd2,edge_weight=math.sqrt((loc1[0]-loc2[0])**2+(loc1[1]-loc2[1])**2) )
    CApprox=st.tsp_exact("a")
    CApproxPath=CApprox[0]
    elapsed = time.time() - t
    CApproxPath.append("a")
    assert elapsed >5,"Your code is too fast"
    assert abs(CApprox[1]- 279.9 )<1, "Your code did not produce the correct result"
   