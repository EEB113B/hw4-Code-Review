def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    Matrix = input_matrix
    size = len(Matrix) #判斷矩陣大小
    lst = [None] * ((1 + size) * size // 2) #建造存放一維陣列的空間

    sum = 0 #判斷是否為左下三角矩陣
    for i in range(1,size):
        for j in range(i-1):
            sum += Matrix[j][i]
    if sum ==0:    #如果是執行以下排列

        if Major =='r': #以row排列
            index = 0
            for x in range (size):
                for y in range(0,x+1):
                    lst[index] = Matrix[x][y]
                    index +=1
        if Major =='c': #以column排列
            index = 0
            for x in range (size):
                for y in range(x,size):
                    lst[index] = Matrix[y][x]
                    index +=1
    sum = 0 #判斷是否為右下三角形矩陣
    for i in range(size-1):
        for j in range(size-1-i):
            sum += Matrix[j][i]
    if sum ==0:

        if Major == 'r':
            index = 0
            for x in range (size):
                for y in range(size-1-x,size):
                    lst[index] = Matrix[x][y]
                    index +=1

        elif Major == 'c':
            index = 0
            for x in range (size):
                for y in range(size-1-x,size):
                    lst[index] = Matrix[y][x]
                    index +=1

    sum = 0 #判斷是否為左上三角形矩陣
    for j in range(1,size):
        for i in range(size-j,size):
            sum += Matrix[j][i]
    if sum ==0:
        if Major =='r':
            index = 0
            for x in range (size):
                for y in range(0,size-x):
                    lst[index] = Matrix[x][y]
                    index += 1
        if Major == 'c':
            index = 0
            for x in range(size):
                for y in range(0,size-x):
                    lst[index] = Matrix[y][x]
                    index +=1
    sum = 0 #判斷是否為右上三角形矩陣
    for i in range(1,size):
        for j in range(size):
            sum += Matrix[i][j]
    if sum ==0:
        if Major =='r':
            index = 0
            for x in range (size):
                for y in range(x,size):
                    lst[index] = Matrix[x][y]
                    index +=1
    
        if Major == 'c':
            for y in range(size):
                for x in range(0,y+1):
                    lst[index] = Matrix[x][y]
                    index += 1

        
    return lst# 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,0,0,0,0,0],
                    [0,0,0,0,7,8],
                    [0,0,0,5,5,9],
                    [0,0,1,6,4,1],
                    [0,0,5,8,4,9],
                    [0,7,2,6,9,0]]
    output_array = to_1D_array(input_matrix, 'r')
    print(output_array)


#留言板