def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)
    N = [None] * ((size + 1) * size // 2)
    Matrix_type = ""
    count = {"upper_right":0, "upper_left":0, "lower_left":0, "lower_right":0 }
    for i in range(size):
        for j in range(size):

            if i > j and Matrix[i][j] == 0:                        #判斷右上三角形矩陣
                count["upper_right"] += 1 

            elif i+j >= size-1 and Matrix[i][j] == 0:              #判斷左上三角形矩陣
                count["upper_left"] += 1

            elif i < j and Matrix[i][j] == 0:                      #判斷左下三角形矩陣
                count["lower_left"] += 1

            elif i+j <= size-1 and Matrix[i][j] == 0:              #判斷右下三角形矩陣
                count["lower_right"] += 1
  

    s_count = sorted(count.items(), key=lambda d : -d[1])          #利用0出現的次數判斷
    Matrix_type = s_count[0][0]                                    #判斷類別是row或是column

    index = 0

    if Major == "r":                                               #水平壓縮
        for i in range(size):
            for j in range(size):
                                                                   #判別是屬於何種矩陣
                if Matrix_type == "upper_right":
                    if i <= j:
                        N[index] = Matrix[i][j]
                        index += 1

                elif Matrix_type == "lower_left":
                    if i >= j:
                        N[index] = Matrix[i][j]
                        index += 1

                elif Matrix_type == "lower_right":
                    if i + j >= size-1:
                        N[index] == Matrix[i][j]
                        index += 1

                elif Matrix_type == "upper_left":
                    if i + j < size:
                        N[index] == Matrix[i][j]
                        index += 1

    if Major == "c":                                               #垂直壓縮
        for i in range(size):
            for j in range(size):
                                                                   #判別是屬於何種矩陣
                if Matrix_type == "upper_right":
                    if i >= j:
                        N[index] = Matrix[j][i]
                        index += 1

                elif Matrix_type == "lower_left":
                    if i <= j:
                        N[index] = Matrix[j][i]
                        index += 1

                elif Matrix_type == "lower_right":
                    if i + j >= size-1:
                        N[index] = Matrix[j][i]
                        index += 1

                elif Matrix_type == "upper_left":
                    if i + j <= size-1:
                        N[index] = Matrix[j][i]
                        index += 1
    
    return N                                                       #回傳壓縮後的矩陣

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix =  [[1,2,3,4],
                    [5,6,7,0],
                    [8,9,0,0],
                    [0,0,0,0]]



    output_array = to_1D_array(input_matrix, "c")
    print(output_array)

#留言板