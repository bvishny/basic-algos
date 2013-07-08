# Matrix Multiplication using Strassen's Algorithm


def strassen(mat1, mat2):
    # Validate non-empty nxn matrices
	result = []
    n = len(mat1)
	if len(mat1) != len(mat2) or len(mat1) == 0 or len(mat2) == 0 or len(mat1[0]) != len(mat2[0]):
	    for i in xrange(n):
			result.append([])
			
			for j in xrange(n):
                print([mat1[j][k] * mat2[k][j] for k in xrange(n)])
			    result[i].append(sum([mat1[j][k] * mat2[k][j] for k in xrange(n)]))
    
        return result
    
print(strassen([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
				