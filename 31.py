def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)                      #計算矩陣大小
    new_list = [None] * ((1 + size) * size // 2)#創建一個list儲存壓縮矩陣
    bottom_left = True                      #判斷是否為左下三角
    for i in range(size):
        for j in range(i+1,size):
            if Matrix[i][j] != 0:   
                bottom_left *= False
                break
            else:
                bottom_left *= True

    upper_left = True                       #判斷是否為左上三角
    for i in range(1,size):
        for j in range(size-i,size):
            if Matrix[i][j] != 0:   
                upper_left *= False     
                break
            else:
                upper_left *= True

    bottom_right = True                     #判斷是否為右下三角
    for i in range(size):
        for j in range(0,size-1-i):
            if Matrix[i][j] != 0:
                bottom_right *= False
                break
            else:
                bottom_right *= True

    upper_right = True                      #判斷是否為右上三角
    for i in range(1,size):
        for j in range(0,i):
            if Matrix[i][j] != 0:
                upper_right *= False
                break
            else:
                upper_right *= True


    if Major == "r":                        #判斷水平壓縮
        index = 0
        if bottom_left==True:
            for i in range(size):
                for j in range(0, i+1):
                    new_list[index] = Matrix[i][j]
                    index += 1 

        if upper_left==True:
            for i in range(size):
                for j in range(0, size-i):
                    new_list[index] = Matrix[i][j]
                    index += 1

        if bottom_right==True:
            for i in range(size):
                for j in range(size-1-i,size):
                    new_list[index] = Matrix[i][j]
                    index += 1

        if upper_right==True:
            for i in range(size):
                for j in range(i, size):
                    new_list[index] = Matrix[i][j]
                    index += 1






    if Major == "c":                        #判斷垂直壓縮
        index = 0
        if bottom_left==True:
            for j in range(size):
                for i in range(j, size):
                    new_list[index] = Matrix[i][j]
                    index += 1
        if upper_left==True:
            for j in range(size):
                for i in range(0, size-j):
                    new_list[index] = Matrix[i][j]
                    index += 1
        if bottom_right==True:
            for j in range(size):
                for i in range(size-1-j,size):
                    new_list[index] = Matrix[i][j]
                    index += 1

        if upper_right==True:
            for j in range(size):
                for i in range(0, j+1):
                    new_list[index] = Matrix[i][j]
                    index += 1


    return new_list 

        


    # 回傳值型態:list

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