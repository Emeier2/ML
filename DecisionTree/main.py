import DecisionTree
import sys
import reader

#read in data
def main():
    buffer = ""
    ## read in data from selected file 
    input = sys.stdin.readline()
    reader(readerOutput)
    DecisionTree(tree, readerOutput.X, readerOutput.feature_names, readerOutput.labels)  
    ##create loop to receive any inputs. on receipt of "quit" program ends
    while(input != "quit"):
        input = sys.stdin.readline()
        