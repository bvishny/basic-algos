def mult(mat1, mat2):
    result, n = [], len(mat1)
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        for i in xrange(n):
            result.append([])
            
            for j in xrange(n):
                result[i].append(sum([mat1[i][k] * mat2[k][j] for k in xrange(n)]))
    
    return result

print(mult([[1, 2], [3, 4]], [[1, 2], [3, 4]]))