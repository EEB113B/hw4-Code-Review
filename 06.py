def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    n = len(Matrix)
    zeros = ((n-1)*n)//2
    #zeros計算n*n三角矩陣所有的0元素
    checkType = ''
    rowArray = []
    collunmArray = []
    # 左下
    for r in range(n):
        for collunm in range(r+1, n):
            checkType+=str(Matrix[r][collunm])#檢查右上方所有元素 並放入checType字串k
        for collunm in range(r+1):
            rowArray.append(Matrix[r][collunm])#將左下矩陣元素以列壓縮
        collunm = r
        #collunm 變為外迴圈變數
        for row in range(collunm, n):# row 為內迴圈變數
            collunmArray.append(Matrix[row][collunm])
            #將左下矩陣元素逐行壓縮
    if checkType == '0'*zeros:#檢查是否為三角矩陣
        #如為4*4矩陣->zeros =6 
            if Major.lower() == 'r':
                return rowArray
            elif Major.lower() == 'c':
                return collunmArray
            else:
                return 'error major'
    
    # 右下
    #做完前者判斷->清空所有壓縮array
    rowArray.clear()
    collunmArray.clear()
    checkType = []

    for r in range(n):#檢查左上方矩陣元素
        checkType = checkType + Matrix[r][:n-r-1]
        rowArray+= Matrix[r][-r-1:]#將右下三角元素丟入row壓縮矩陣
        collunm = r
        for row in range(3-collunm,n):#將右下三角元素丟入collunm壓縮矩陣
            collunmArray.append(Matrix[row][collunm])
    if checkType == [0]*zeros:
            if Major.lower() == 'r':
                return rowArray
            elif Major.lower() == 'c':
                return collunmArray
            else:
                return 'error major'
    
    # 左上
    rowArray.clear()
    collunmArray.clear()
    checkType = []
    for r in range(n):
        checkType = checkType + Matrix[r][n-r:]
        rowArray+= Matrix[r][:n-r]
        collunm = r
        for row in range(n-collunm):
            collunmArray.append(Matrix[row][collunm])
    if checkType == [0]*zeros:
            if Major.lower() == 'r':
                return rowArray
            elif Major.lower() == 'c':
                return collunmArray
            else:
                return 'error major'
    


    # 右上
    rowArray.clear()
    collunmArray.clear()
    checkType = []
    for r in range(n):
        checkType = checkType + Matrix[r][:r]
        rowArray+= Matrix[r][r:]
        collunm = r
        for row in range(collunm+1):
            collunmArray.append(Matrix[row][collunm])
    if checkType == [0]*zeros:
            if Major.lower() == 'r':
                return rowArray
            elif Major.lower() == 'c':
                return collunmArray
            else:
                return 'error major'


    #以上皆非則此引數非三角矩陣            
    return 'it\'s not triangle array'
    
    # 回傳值型態:list



if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[7,0,0,0],
                    [8,3,0,0],
                    [4,6,5,0],
                    [0,5,6,7]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)

    output_array = to_1D_array(input_matrix, "c")
    print(output_array)

    input_matrix = [[0,0,0,1],
                    [0,0,2,3],
                    [0,4,5,5],
                    [0,6,7,7]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)

    output_array = to_1D_array(input_matrix, "c")
    print(output_array)
    input_matrix = [[1,2,3,4],
                    [9,3,2,0],
                    [7,1,0,0],
                    [4,0,0,0]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)

    output_array = to_1D_array(input_matrix, "c")
    print(output_array)
    input_matrix = [[4,1,1,1],
                    [0,2,2,3],
                    [0,0,5,5],
                    [0,0,0,7]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)

    output_array = to_1D_array(input_matrix, "c")
    print(output_array)

    input_matrix = [[0,0,0,0,0,0],
                    [0,0,0,0,7,8],
                    [0,0,0,5,5,9],
                    [0,0,1,6,4,1],
                    [0,0,5,8,4,9],
                    [0,7,2,6,9,0]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)

    output_array = to_1D_array(input_matrix, "c")
    print(output_array)
    input_matrix = [[7,0,0,0,0],
                    [8,3,0,0,0],
                    [4,6,5,0,0],
                    [2,5,6,7,0],
                    [0,4,2,8,9]]


    output_array = to_1D_array(input_matrix, "r")
    print(output_array)

    output_array = to_1D_array(input_matrix, "c")
    print(output_array)


#留言板