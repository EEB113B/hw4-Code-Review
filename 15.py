def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str

    size = len(Matrix) #抓出矩陣共有多少行列

    #將四方向的三角形列出list
    upper_right_list = []
    upper_left_list = []
    lower_right_list = []
    lower_left_list = []

    #設一參數
    index = 0

    #以column-major進行壓縮
    if Major == "c":
        for i in range(size):
            for j in range(0,i+1):
                upper_right_list.append(Matrix[j][i])  # 右上三角形矩陣
        
        for i in range(0,size):
            for j in range(0, size-index):
                upper_left_list.append(Matrix[j][i])
            index += 1
        index = 0                                      # 左上三角形矩陣
        
        for k in range(size):
            for l in range(k, size):
                lower_left_list.append(Matrix[l][k])   # 左下三角形矩陣
        
        for k in range(0,size):
            for l in range(size-index-1, size):
                lower_right_list.append(Matrix[l][k])
            index += 1
        index = 0                                       # 右下三角形矩陣

    #以row-major進行壓縮
    if Major == "r":
        for i in range(size):
            for j in range(0, i+1):
                lower_left_list.append(Matrix[i][j])    # 左下三角形矩陣

        for k in range(size):
            for l in range(0, size-index):
                upper_left_list.append(Matrix[k][l])
            index += 1
        index = 0                                       # 左上三角形矩陣
        
        for i in range(size):
            for j in range(index, size):
                upper_right_list.append(Matrix[i][j])
            index += 1
        index = 0                                       # 右上三角形矩陣
        
        for k in range(size):
            for l in range(size-index-1, size):
                lower_right_list.append(Matrix[k][l])
            index +=1
        index = 0                                       # 右下三角形矩陣
        

    #比較各矩陣0的數量，將最少的矩陣設為best_tri_array    
    if upper_right_list.count(0) < upper_left_list.count(0):
        best_tri_array = upper_right_list
    else:
        best_tri_array = upper_left_list
    
    if lower_right_list.count(0) < best_tri_array.count(0):
        best_tri_array = lower_right_list
    
    if lower_left_list.count(0) < best_tri_array.count(0):
        best_tri_array = lower_left_list

    #回傳 best_tri_array
    return best_tri_array

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[1,2,3,4],
                    [5,6,7,0],
                    [8,9,0,0],
                    [0,0,0,0]]
    output_array = to_1D_array(input_matrix, "c")

    print(output_array)


#留言板