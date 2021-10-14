import sys
import math

def main():
    firstline = sys.stdin.readline().rstrip('\n')
    inputs = firstline.split(' ')
    print(alg(inputs))
def alg(inputs):
    pos = float(inputs[0])
    neg = float(inputs[1])
    total = pos + neg
    if(pos == 0 or neg == 0):
        return 0
    result = (-(pos/total) * math.log((pos/total),(2))) - ((neg/total) * math.log((neg/total),(2)))
    return result
    
if __name__=="__main__":
    main()
