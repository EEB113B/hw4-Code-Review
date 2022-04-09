def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)                     #算是幾乘以與幾的矩陣
    new = [None] * ((1+size) * size // 2)  #創立要回傳的空字串

    number = 0
    
    if Major == "c":                            #判斷為行的形式
        if number > 0:                          #判斷為上三角形
            c = 0
            column1 = 0
            for i in range(1,size):                     
                c = int(Matrix[i][0])           #計算最左列的值
                column1 += c

            if column1 > 0:                     #大於0，代表最左列都有數字，所以為左上三角形
                index = 0
                cut = 0
                for j in range(size):                  
                    for i in range(size-cut):
                        new[index] = Matrix[i][j]
                        index += 1
                        cut +=1
                return new

            else:                               #為右上三角形
                index = 0
                for j in range(size):
                    for i in range(0,j+1):
                        new[index] = Matrix[i][j]
                        index += 1
                return new

        else:                                   #判斷為下三角形
            c = 0
            column2 = 0
            for i in range(size):                     
                c = int(Matrix[i][0])
                column2 += c

            if column2 > 0:                     #大於0，代表最左列都有數字，所以為左下三角形
                index = 0
                for j in range(size):
                    for i in range(j,size):
                        new[index] = Matrix[i][j]
                        index += 1
                return new

            else:                               #為右下三角形
                index = 0
                for j in range(size):
                    for i in range(size-j-1,size):
                        new[index] = Matrix[i][j]
                        index += 1
                return new


    if Major == "r":                            #判斷為列的形式
        if number > 0:                          #判斷為上三角形
            r = 0
            row1 = 0

            for i in range(1,size):                    
                r = int(Matrix[i][0])           #計算最左列的值
                row1 += r

            if row1 > 0:                        #大於0，代表最左列都有數字，所以為左上三角形    
                index = 0
                cut = 0

                for i in range(size):                  
                    for j in range(size-cut):
                        new[index] = Matrix[i][j]
                        index += 1
                        cut +=1
                return new

            else:                               #為右上三角形          
                index = 0
                for i in range(size):
                    for j in range(i,size):
                        new[index] = Matrix[i][j]
                        index += 1
                return new

        else:                                   #判斷為下三角形
            r = 0
            row2 = 0
            for i in range(size):                     
                r = int(Matrix[i][0])
                row2 += r

            if row2 > 0:                        #大於0，代表最左列都有數字，所以為左下三角形
                index = 0
                for i in range(size):
                    for j in range(0,i+1):
                        new[index] = Matrix[i][j]
                        index += 1
                return new

            else:                               #為右下三角形
                index = 0
                for i in range(size):
                    for j in range(size-i-1,size):
                        new[index] = Matrix[i][j]
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
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板