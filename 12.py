def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)
    B = [None] * ((1 + size) * size // 2)
    ##下面四個判斷為為左上、左下、右上、右下這四種三角形矩陣的其中哪一種
    #左下
    ll = 0
    for i in range(1, size):
        for j in range(0, i):
            ll += Matrix[i][j]
    #右下
    rl = 0
    for i in range(1, size):
        for j in range(size - i, size):
            rl += Matrix[i][j]
    #右上
    rt = 0
    for i in range(size):
        for j in range(i + 1, size):
            rt += Matrix[i][j]
    #左上
    lt = 0
    for i in range(size):
        for j in range(0, size - i -1):
            lt += Matrix[i][j]
    
    ##Major為r時進行一維陣列壓縮處理
    if Major == "r":
        #右上
        if ll == 0:
            index = 0
            for i in range(size):
                for j in range(i, size):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
        #左上
        if rl == 0:
            index = 0
            for i in range(size):
                for j in range(0, size - i):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
        #左下
        if rt == 0:
            index = 0
            for i in range(size):
                for j in range(0, i+1):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
        #右下
        if lt == 0:
            index = 0
            for i in range(size):
                for j in range(size -1 -i, size):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
    
    ##Major為c時進行一維陣列壓縮處理
    if Major == "c":
        #右上
        if ll == 0:
            index = 0
            for i in range(size):
                for j in range(0, i+1):
                    B[index] = Matrix[j][i]
                    index += 1
            return B
        #左上
        if rl == 0:
            index = 0
            for i in range(size):
                for j in range(0, size - i):
                    B[index] = Matrix[j][i]
                    index += 1
            return B
        #左下
        if rt == 0:
            index = 0
            for i in range(size):
                for j in range(i, size):
                    B[index] = Matrix[j][i]
                    index += 1
            return B
        #右下
        if lt == 0:
            index = 0
            for i in range(size):
                for j in range(size -1 -i, size):
                    B[index] = Matrix[j][i]
                    index += 1
            return B

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,5,2,0],
                    [0,0,3,1],
                    [0,0,0,7],
                    [0,0,0,0]]

    output_array = to_1D_array(input_matrix, "r")
    print(output_array)

#留言板