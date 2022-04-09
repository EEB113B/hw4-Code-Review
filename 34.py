def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)
    New_matrix = [None]*((1+size)*size//2)#創建空list
    sum = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(size):#判斷對角線左下各項相加為0 (sum = 0)，則為右上三角矩陣(左下皆為0)
        for j in range (i):
            sum += Matrix[i][j]

    for i in range(size):#判斷對角線右上各項相加為0 (sum1 = 0)，則為左下三角矩陣(右上皆為0)
        for j in range (i+1, size):
            sum1 += Matrix[i][j]
    
    for i in range(size):#判斷對角線右下各項相加為0 (sum2 = 0)，則為左上三角矩陣(右下皆為0)
        for j in range(size-i, size):
            sum2 += Matrix[i][j]
            
    for i in range(size):#判斷對角線左上各項相加為0 (sum3 = 0)，則為右下三角矩陣(左上皆為0)
        for j in range(0, size-1-i):
            sum3 += Matrix[i][j]

    index = 0
    if sum == 0:#如果是右上三角矩陣(左下皆為0)
        if Major == "r":#用一維陣列水平壓縮處理
            for i in range(size):
                for j in range(i, size):
                    New_matrix[index] = Matrix[i][j]
                    index += 1
        if Major == "c":#用一維陣列垂直壓縮處理
            for j in range(size):
                for i in range(0, j+1):
                    New_matrix[index]= Matrix[i][j]
                    index += 1 
    
    if sum1 == 0:#如果是左下三角矩陣(右上皆為0)
        if Major == "r":#用一維陣列水平壓縮處理
            for i in range(size):
                for j in range(0, i+1):
                    New_matrix[index] = Matrix[i][j]
                    index += 1
        if Major == "c":#用一維陣列垂直壓縮處理
            for j in range(size):
                for i in range(j, size):
                    New_matrix[index] = Matrix[i][j]
                    index += 1           
    if sum2 == 0:#如果是左上三角矩陣(右下皆為0)
        if Major == "r":#用一維陣列水平壓縮處理
            for i in range(size):
                for j in range(0, size-i):
                    New_matrix[index] = Matrix[i][j]
                    index += 1  
        if Major == "c":#用一維陣列垂直壓縮處理
            for j in range(size):
                for i in range(0, size-j):
                    New_matrix[index] = Matrix[i][j]
                    index += 1 

    if sum3 == 0:#如果是右下三角矩陣(左上皆為0)
        if Major == "r":#用一維陣列水平壓縮處理
            for i in range(size):
                for j in range(size-1-i, size):
                    New_matrix[index] = Matrix[i][j]
                    index += 1 
        if Major == "c":#用一維陣列垂直壓縮處理
            for j in range(size):
                for i in range(size-1-j, size):
                    New_matrix[index] = Matrix[i][j]
                    index += 1 
    return New_matrix # 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix =     [[0,5,2,0],
                        [0,0,3,1],
                        [0,0,0,7],
                        [0,0,0,0]]

    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板