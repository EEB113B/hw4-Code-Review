def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)
    N = [None]*((1+size)*size//2)
    index = 0
    A=0
    B=0
    C=0
    D=0
    name=0
    #-------------------------三角形判斷--------------------------  
    #---------------右上判斷:左下角的行列除了端點皆等於0---------------
    for i in range(1,size):
        A = A + Matrix[i][0]
    for j in range(size-1):
        A = A + Matrix[size-1][j]
    if A == 0:
        name = 1  #令右上三角形等於1
    
    #---------------右下判斷:左上角的行列除了端點皆等於0---------------
    for i in range(size-1):
        B = B + Matrix[0][i] + Matrix[i][0]
    if B == 0:
        name = 2  #令右下三角形等於2
        
    #---------------左上判斷:右下角的行列除了端點皆等於0---------------
    for i in range(1,size):
        C = C + Matrix[size-1][i] + Matrix[i][size-1]
    if C == 0:
        name = 3 #令左上三角形等於3
    #---------------左下判斷:右上角的行列除了端點皆等於0---------------
    for i in range(1,size):
        D = D + Matrix[0][i]
    for j in range(size-1):
        D = D + Matrix[j][size-1]
    if D == 0:
        name = 4  #令左下三角形等於4
    #-------------------------壓縮--------------------------
    #---------------右上壓縮---------------'
    if name == 1:          
        if Major == "r":
            for i in range(size):
                for j in range(i,size):
                     N[index] = Matrix[i][j] 
                     index+=1
            return N
        elif  Major == "c":
            for i in range(size):
                for j in range(0,i+1):
                   N[index] = Matrix[j][i] 
                   index+=1
            return N
    #---------------右下壓縮---------------
    if name == 2:          
        if Major == "r":
            for i in range(size):
                for j in range(size-i-1,size):
                     N[index] = Matrix[i][j] 
                     index+=1
            return N
        elif  Major == "c":
            for i in range(size):
                for j in range(size-i-1,size):
                   N[index] = Matrix[j][i] 
                   index+=1
            return N   
   #---------------左上壓縮---------------
    if name == 3:          
        if Major == "r":
            for i in range(size):
                for j in range(0,size-i):
                     N[index] = Matrix[i][j] 
                     index+=1
            return N
        elif  Major == "c":
            for i in range(size):
                for j in range(0,size-i):
                   N[index] = Matrix[j][i] 
                   index+=1
            return N    
    #---------------左下壓縮---------------   
    if name == 4:          
        if Major == "r":
            for i in range(size):
                for j in range(0,i+1):
                     N[index] = Matrix[i][j] 
                     index+=1
            return N
        elif  Major == "c":
            for i in range(size):
                for j in range(i,size):
                   N[index] = Matrix[j][i] 
                   index+=1
            return N
    

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[1,0,0,0],
                    [2,3,0,0],
                    [4,5,6,0],
                    [7,8,9,10]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)



    

#留言板