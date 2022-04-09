def to_1D_array(Matrix, Major): #Matrix型態:list[list]，Major型態:str
    size = len(Matrix)
    B = [None] * ((1 + size) * size // 2)
    total = 0
    for x in range(1,size): #用兩個for迴圈把右上的數字相加，total為零時代表為左下三角形
        for y in range(x-1):
            total += Matrix[y][x]
    if total == 0:  #為左下三角形
        if Major == 'r':   #判別以列或行的形式印出
            index = 0
            for i in range(size):
                for j in range(0, i+1):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
        if Major == "c":
            index = 0
            for j in range(size):
                for i in range(j,size):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
    total = 0
    for x in range(size-1):  #用兩個for迴圈把左上的數字相加，total為零時代表為右下三角形
        for y in range(size-x-1):
            total += Matrix[y][x]
    if total==0:  #為右下三角形
        if Major == 'r':   #判別以列或行的形式印出
            index = 0
            for i in range(size):
                for j in range(size-1-i, size):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
        if Major == "c":
            index = 0
            for j in range(size):
                for i in range(size-j-1,size):
                    B[index] = Matrix[i][j]
                    index += 1
            return B 
    total = 0
    for y in range(1,size):  #用兩個for迴圈把左下的數字相加，total為零時代表為右上三角形
        for x in range(y):
            total += Matrix[y][x]
    if total==0: #為右上三角形
        if Major == 'r':   #判別以列或行的形式印出
            index = 0
            for i in range(size):
                for j in range(i, size):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
        if Major == "c":
            index = 0
            for j in range(size):
                for i in range(j+1):
                    B[index] = Matrix[i][j]
                    index += 1
            return B 
    total = 0
    for y in range(1,size):   #用兩個for迴圈把右下的數字相加，total為零時代表為左上三角形
        for x in range(size-y,size):
            total += Matrix[y][x]
    if total==0: #為左上三角形
        if Major == 'r':  #判別以列或行的形式印出
            index = 0
            for i in range(size):
                for j in range(size-i):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
        if Major == "c":
            index = 0
            for j in range(size):
                for i in range(size-j):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
# 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,0,0,0,0,0],
                    [0,0,0,0,7,8],
                    [0,0,0,5,5,9],
                    [0,0,1,6,4,1],
                    [0,0,5,8,4,9],
                    [0,7,2,6,9,0]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板