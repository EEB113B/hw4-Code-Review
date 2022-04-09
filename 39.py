def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    matrix_size = len(Matrix)
    
    # 因為還不需確定此矩陣為四個三角矩陣中的哪一個，因此先把四個三角矩陣都先列出來，晚點再去判斷
    upper_right_list = []
    upper_left_list = []
    lower_right_list = []
    lower_left_list = []
    
    # 設參數，初始化為 0
    index = 0

    # 以 Row-Major 形式壓縮
    if Major == "r":
        for i in range(matrix_size):
            for j in range(0,i+1):
                lower_left_list.append(Matrix[i][j])   # 列出左下三角矩陣

        for k in range(matrix_size):
            for l in range(0,matrix_size-index):
                upper_left_list.append(Matrix[k][l])
            index = index + 1
        index = 0                                       # 列出左上三角矩陣
                        
        for i in range(matrix_size):
            for j in range(index,matrix_size):
                upper_right_list.append(Matrix[i][j])    
            index = index + 1
        index = 0                                       # 列出右上三角矩陣

        for k in range(matrix_size):
            for l in range(matrix_size-index-1,matrix_size):
                lower_right_list.append(Matrix[l][k])
            index = index + 1
        index = 0                                       # 列出右下三角矩陣


    # 以 Column-Major 形式壓縮
    if Major == "c":
        for i in range(matrix_size):
            for j in range(0,i+1):
                upper_right_list.append(Matrix[j][i])   # 列出右上三角矩陣

        for i in range(0,matrix_size):
            for j in range(0,matrix_size-index):
                upper_left_list.append(Matrix[j][i])
            index = index + 1
        index = 0                                       # 列出左上三角矩陣
                        
        for k in range(matrix_size):
            for l in range(k,matrix_size):
                lower_left_list.append(Matrix[l][k])    # 列出左下三角矩陣

        for k in range(0,matrix_size):
            for l in range(matrix_size-index-1,matrix_size):
                lower_right_list.append(Matrix[l][k])
            index = index + 1
        index = 0                                       # 列出右下三角矩陣

    

    # 比較四個三角矩陣 0 的數量，將最少 0 的矩陣設為 target_tri_array
    if upper_right_list.count(0) < upper_left_list.count(0):
        target_tri_array = upper_right_list
    else:
        target_tri_array = upper_left_list

    if lower_right_list.count(0) < target_tri_array.count(0):
        target_tri_array = lower_right_list
    
    if lower_left_list.count(0) < target_tri_array.count(0):
        target_tri_array = lower_left_list


    
    return target_tri_array                               # 回傳值型態:list

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