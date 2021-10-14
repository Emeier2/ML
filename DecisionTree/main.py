from typing import List
import DecisionTree
import Reader
import sys

#read in data
def main():
    buffer = ""
    ## read in data from selected file 
    file = sys.stdin.readline()
    lines = []
    with open(file) as f:
        lines = f.readlines()
    
    ##create loop to receive any inputs. on receipt of "quit" program ends
    #while(sys.stdin.readline() != "quit"):
        ##do something invovling reading in data
            
    
    
