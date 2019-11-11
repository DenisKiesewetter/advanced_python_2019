
import pytest
import sys, os
# This block is not neccessary if you instaled your package
# using e.g. pip install -e
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), # location of this file
            os.pardir, # and one level up, in linux ../
        )
    )
)
# EOBlock
import playground


def test_find_black_peaks():
    peaks = playground.color.find_black_peaks([(1,1,1),(1,0,1),(1,1,1)])
    assert peaks == [2]  
    
def test_find_black_two_peaks():
    peaks = playground.color.find_black_peaks([(1,1,1),(1,0,1),(1,1,1),(0,1,1),(1,1,1)])
    assert peaks == [2, 2] 

def test_find_black_peaks_max_edge():
    peaks = playground.color.find_black_peaks([(1,0,0),(1,0,1),(1,1,0)])
    assert peaks == [] 
    
def test_find_black_peaks_empty_list():
    peaks = playground.color.find_black_peaks([])
    assert peaks == [] 
