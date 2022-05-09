import numpy as np

def search_consecutive(m):
    for i in range(5):
        start = 0
        end = 0
        c = m[i,0]
        for j in range(1,5):
            if m[i,j] == c+1:
                end = j
            else:
                start, end = j, j
            c = m[i,j]
            if (end-start) == 3:
                print("m[{},{}] ---> m[{},{}]".format(i,start, i, end))

if __name__ == "__main__":
    matrix = np.random.randint(0,5, size=(5,5))
    print(matrix)

    search_consecutive(matrix)
    search_consecutive(matrix.T)

