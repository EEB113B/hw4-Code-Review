def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    lst = Matrix
    row_or_column_major = Major
    Upp_right = 0
    Upp_left = 0
    Low_right = 0
    Low_left = 0
    #lst_Compress儲存壓縮的一維矩陣
    lst_Compress = []
    #判斷矩陣大小
    a = len(lst)

    #用 0 的位置分布判斷為哪種矩陣
    for i in range(1,a):            #判斷是否為右上三角形矩陣
        for j in range(0,i):
            Upp_right += lst[i][j]
    if Upp_right == 0:
        Upp_r = True
    else:
        Upp_r = False

    for i in range(1,a):            #判斷是否為左上三角形矩陣
        for j in range(-1,-i,-1):
            Upp_left += lst[i][j]
    if Upp_left == 0:
        Upp_l = True
    else:
        Upp_l = False

    for i in range(0,a-1):            #判斷是否為右下三角形矩陣
        for j in range(0,-i):
            Low_right += lst[i][j]
    if Low_right == 0:
        Low_r = True
    else:
        Low_r = False

    for i in range(0,a-1):            #判斷是否為左下三角形矩陣
        for j in range(i+1,a):
            Low_left += lst[i][j]
    if Low_left == 0:
        Low_l = True
    else:
        Low_l = False

    #判斷 Major  為何，並以它要求的方式進形壓縮
    #以下是 Major 為row-major的狀況
    if row_or_column_major == "r":
        if Upp_r:                                       #壓縮右上三角形矩陣
            for i in range(0,a):
                for j in range(i,a):
                    lst_Compress.append(lst[i][j])


        elif Upp_l:                                       #壓縮左上三角形矩陣
            for i in range(0,a):
                for j in range(0,a-i):
                    lst_Compress.append(lst[i][j])

        elif Low_r:                                       #壓縮右下三角形矩陣
            for i in range(0,a):
                for j in range(-i,a):
                    lst_Compress.append(lst[i][j])

        elif Low_l:                                       #壓縮左下三角形矩陣
            for i in range(0,a):
                for j in range(0,i+1):
                    lst_Compress.append(lst[i][j])

    #以下是 Major 為column-major的狀況
    if row_or_column_major == "C":
        if Upp_r:                                       #壓縮右上三角形矩陣
            for j in range(0,a):
                for i in range(0,j):
                    lst_Compress.append(lst[i][j])

        elif Upp_l:                                       #壓縮左上三角形矩陣
            for j in range(0,a):
                for i in range(0,a-j):
                    lst_Compress.append(lst[i][j])

        elif Low_r:                                       #壓縮右下三角形矩陣
            for j in range(0,a):
                for i in range(-j-1,a):
                    lst_Compress.append(lst[i][j])

        elif Low_l:                                       #壓縮左下三角形矩陣
            for j in range(0,a):
                for i in range(j,a):
                    lst_Compress.append(lst[i][j])
    return lst_Compress# 回傳值型態:list

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