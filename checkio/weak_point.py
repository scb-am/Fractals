def weak_point(matrix):
    rows = [sum(r) for r in matrix]
    columns = [sum(r) for r in zip(*matrix)]
    return rows.index(min(rows)), columns.index(min(columns))

def weak_point(matrix):
    wk = lambda matrix: matrix.index(min(matrix, key=sum))
    tmatrix = list(zip(*matrix)) # transpose
    return [wk(matrix), wk(tmatrix)]

weak_point = lambda matrix: (
    min(enumerate([sum(x) for x in matrix]), key=lambda x: x[1])[0],
    min(enumerate([sum(x) for x in [[y[x] for y in matrix] for x in range(len(matrix[0]))]]), key=lambda x: x[1])[0])