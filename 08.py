def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)                     #$算是幾乘以與幾的矩陣
    new = [None] * ((1+size) * size // 2)  #$創立要回傳的空字串
    
    total = 0
        
    for j in range(1,size):                  #$第一列加總
        a = int(Matrix[0][j])
        total += a
    if Major == "r":                         #read row
        if total > 0:                        #$判斷是否為上三角形
            b = 0
            total_1 = 0
            for i in range(1,size):          #矩陣中第一行相加           
                b = int(Matrix[i][0])
                total_1 += b
            if total_1 > 0:                    #如果第一行、第一列有值，就是左上三角
                index = 0
                cut = 0
                for i in range(size):                  #左上
                    for j in range(size-cut):
                        new[index] = Matrix[i][j]       #read row
                        index += 1
                        cut +=1
                return new
            else:                                      #右上
                index = 0
                for i in range(size):
                    for j in range(i,size):
                        new[index] = Matrix[i][j]        #read row
                        index += 1
                return new
        else:                                      #判斷是否為下三角形
            b = 0
            total_2 = 0
            for i in range(size):                     #矩陣中第一行相加
                b = int(Matrix[i][0])
                total_2 += b
            if total_2 > 0:                            #左下
                index = 0
                for i in range(size):
                    for j in range(0,i+1):
                        new[index] = Matrix[i][j]       #read row
                        index += 1
                return new
            else:                                      #右下
                index = 0
                for i in range(size):
                    for j in range(size-i-1,size):
                        new[index] = Matrix[i][j]       #read row
                        index += 1 
                return new
    if Major == "c":                               #read column
        if total > 0:                              #判斷是否為上三角形
            b = 0
            total_1 = 0
            for i in range(1,size):                     
                b = int(Matrix[i][0])
                total_1 += b
            if total_1 > 0:
                index = 0
                cut = 0
                for j in range(size):                  #左上
                    for i in range(size-cut):
                        new[index] = Matrix[i][j]      #read column
                        index += 1
                        cut +=1
                return new
            else:                                      #右上
                index = 0
                for j in range(size):
                    for i in range(0,j+1):
                        new[index] = Matrix[i][j]     #read column
                        index += 1
                return new
        else:                                       #判斷下三角形
            b = 0
            total_2 = 0
            for i in range(size):                     
                b = int(Matrix[i][0])
                total_2 += b
            if total_2 > 0:                            #左下
                index = 0
                for j in range(size):
                    for i in range(j,size):
                        new[index] = Matrix[i][j]      #read column
                        index += 1
                return new
            else:                                      #右下
                index = 0
                for j in range(size):
                    for i in range(size-j-1,size):
                        new[index] = Matrix[i][j]      #read column
                        index += 1
                return new


                
    return # 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[7,0,0,0],
                    [8,3,0,0],
                    [4,6,5,0],
                    [0,5,6,7]]
    output_array = to_1D_array(input_matrix, "c")
    print(output_array)


#留言板