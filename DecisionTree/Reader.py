import sys
def __init__(self):
    #define the following variables and save them in instance      
    self.X = [] # features or predictors
    self.feature_names = [] # name of the features
    self.labels = [] # categories
    file = sys.stdin.readline().split(" ")
    lines = []
    with open(file[0]) as f:
        lines = f.readlines()
    for line in lines:
        #each colum in the 2d array needs to be converted to a row in another
        contents = line.split(",")
        for x in range(len(contents)):
            self.labels[x].append(contents[x])
        
   #define the following variables and save them in instance      
    self.X = lines # features or predictors
    self.feature_names = set(lines) # name of the features
    