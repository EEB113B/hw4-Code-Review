def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    num = int(size*(1+size)/2) #去掉對角線外的0後的項數
    A = [None]*(num+1) #預設要回傳的list(列)
    B = [None]*(num+1) #預設要回傳的list(行)
    #右上
    for i in range(1,size):
        for j in range(0,i):
            sum1 += Matrix[i][j] #將左上到右下的對角線左側的值相加
    if sum1 == 0: #如果對角線左側的值相加後=0，代表這是一個右上三角矩陣
        index = 0
        for i in range(size):
            for j in range(i,size):
                index = index+1 
                A[index] = Matrix[i][j] #從第0列開始將值取出，加到要回傳的list(列)中
        index = 0
        for i in range(size):
            for j in range(0,i+1):
                index = index+1
                B[index] = Matrix[j][i] #從第0行開始將值取出，加到要回傳的list(列)中
    #左上
    for i in range(1,size):
        for j in range(size-i,size):
            sum2+=Matrix[i][j] #將右上到左下的對角線右側的值相加
    if sum2 == 0: #如果對角線外的值相加後=0，代表這是一個左上三角矩陣
        index = 0
        for i in range(1,size):
            for j in range(size-i,size):
                index = index+1 
                A[index] = Matrix[i][j] #從第0列開始將值取出，加到要回傳的list(列)中
        index = 0
        for i in range(size):
            for j in range(size-i):
                index = index+1
                B[index] = Matrix[j][i] #從第0行開始將值取出，加到要回傳的list(列)中
    #右下
    for i in range(size):
        for j in range(0,size-i-1):
            sum3+=Matrix[i][j] #將右上到左下的對角線左側的值相加
    if sum3 == 0: #如果對角線左側的值相加後=0，代表這是一個右下三角矩陣
        index = 0
        for i in range(size):
            for j in range(size-i-1,size):
                    index = index+1
                    A[index] = Matrix[i][j] #從第0列開始將值取出，加到要回傳的list(列)中          
        index = 0
        for i in range(size):
            for j in range(size-i-1,size):
                    index = index+1
                    B[index] = Matrix[j][i] #從第0行開始將值取出，加到要回傳的list(列)中
    #左下
    for i in range(size):
        for j in range(i+1,size):
            sum4+=Matrix[i][j]#將左上到右下的對角線右側的值相加
    if sum4 == 0:#如果對角線右側的值相加後=0，代表這是一個左下三角矩陣
        index = 0
        for i in range(size):
            for j in range(i+1):
                    index = index+1
                    A[index] = Matrix[i][j] #從第0列開始將值取出，加到要回傳的list(列)中         
        index = 0
        for i in range(size):
            for j in range(i,size):
                    index = index+1
                    B[index] = Matrix[j][i] #從第0行開始將值取出，加到要回傳的list(列)中
                                   
    if Major == "r":
        del(A[0]) #將最前面的None消掉
        return A #回傳list(列)
    elif Major == "c":
        del(B[0]) #將最前面的None消掉
        return B #回傳list(列)
        
     # 回傳值型態:list


if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix =  [[0,5,2,0],
                    [0,0,3,1],
                    [0,0,0,7],
                    [0,0,0,0]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板