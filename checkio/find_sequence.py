from functools import reduce
from operator import eq

def checkio(matrix):
    n = len(matrix)
    r = { 0: range(n), 1: range(n-3), -1: range(n-3, n) }

    def check(dx=0, dy=0):
        for y in r[dy]:
            for x in r[dx]:
                span = [matrix[y+dy*i][x+dx*i] for i in range(4)]
                if span == [span[0]] * 4:
                    return True
        return False
                  
    return check(dx=1) or check(dy=1) or check(dx=1, dy=1) or check(dx=-1, dy=1)
    
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"





# checkio=lambda m: bool(sum([sum([m[j][i]==m[j][i+1]==m[j][i+2]==m[j][i+3] or m[i][j]==m[i+1][j]==m[i+2][j]==m[i+3][j] for j in range(len(m))])+sum([m[i][j]==m[i+1][j+1]==m[i+2][j+2]==m[i+3][j+3] or m[i][j+3]==m[i+1][j+2]==m[i+2][j+1]==m[i+3][j] for j in range(len(m)-3)]) for i in range(len(m)-3)]))



def checkio(matrix):  
    lenth = len(matrix)
    for i in range(lenth-3):
        for j in range(lenth):
            if len(set([matrix[i+k][j] for k in range(4)])) == 1:
                return True
    for i in range(lenth):
        for j in range(lenth-3):
            if len(set([matrix[i][j+k] for k in range(4)])) == 1:
                return True            
    for i in range(lenth-3):
        for j in range(lenth-3):
            if len(set([matrix[i+k][j+k] for k in range(4)])) == 1:
                return True              
    for i in range(3,lenth):
        for j in range(lenth-3):
            if len(set([matrix[i-k][j+k] for k in range(4)])) == 1:
                return True
    return False
