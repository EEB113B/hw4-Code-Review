from tkinter import N


def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    n = len(Matrix)                                 # Matrix是一個n*n的矩陣
    new_lst = []                                    # 創個新list
    
    upper_right = []                                # 創個list檢查右上角是否都是0
    for y in range(n-1, -1, -1):                    # 把左上角的字元都存進upper_lst
        for x in range(y+1, n):
            upper_right.append(Matrix[y][x])
    if upper_right == [0] * ((n-1) * n // 2):       # 如果都是0再根據Major決定是橫的還是直的把左下角存入new_lst
        if Major == "r":
            for y in range(0, n):
                for x in range(0, y+1):
                    new_lst.append(Matrix[y][x])
        if Major == "c":
            for x in range(0, n):
                for y in range(x, n):
                    new_lst.append(Matrix[y][x])

    lower_left = []                                 # 創個list檢查左下角是否都是0
    for y in range(1, n):                           # 把左下角的字元都存進upper_lst
        for x in range(0, y):
            lower_left.append(Matrix[y][x])
    if lower_left == [0] * ((n-1) * n // 2):        # 如果都是0再根據Major決定是橫的還是直的把右上角存入new_lst
        if Major == "r":
            for y in range(0, n):
                for x in range(y, n):
                    new_lst.append(Matrix[y][x])
        if Major == "c":
            for x in range(0, n):
                for y in range(0, x+1):
                    new_lst.append(Matrix[y][x])

    lower_right = []                                 # 創個list檢查左上角是否都是0
    count = n-1                                      # 把右上角的字元都存進upper_lst
    for y in range(0, n-1):                          
        for x in range(0, count):
            lower_right.append(Matrix[y][x])
        count -= 1
    if lower_right == [0] * ((n-1) * n // 2):        # 如果都是0再根據Major決定是橫的還是直的把右下角存入new_lst
        if Major == "r":
            count2 = n - 1 
            for y in range(0, n):
                for x in range(count2, n):
                    new_lst.append(Matrix[y][x])
                count2 -= 1
        if Major == "c":
            count2 = n - 1
            for x in range(0, n):
                for y in range(count2, n):
                    new_lst.append(Matrix[y][x])
                count2 -= 1

    lower_right = []                                 # 創個list檢查右下角是否都是0
    count = n - 1                                    # 把右下角的字元都存進upper_lst
    for y in range(1, n):                          
        for x in range(count, n):
            lower_right.append(Matrix[y][x])
        count -= 1
    if lower_right == [0] * ((n-1) * n // 2):        # 如果都是0再根據Major決定是橫的還是直的把左上角存入new_lst
        if Major == "r":
            count2 = n 
            for y in range(0, n):
                for x in range(0, count2):
                    new_lst.append(Matrix[y][x])
                count2 -= 1
        if Major == "c":
            count2 = n
            for x in range(0, n):
                for y in range(0, count2):
                    new_lst.append(Matrix[y][x])
                count2 -= 1
       
    return new_lst                                   # 回傳新的list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,0,0,0,0,0],
                    [0,0,0,0,7,8],
                    [0,0,0,5,5,9],
                    [0,0,1,6,4,1],
                    [0,0,5,8,4,9],
                    [0,7,2,6,9,0]]

    output_array = to_1D_array(input_matrix, "c")
    print(output_array)


#留言板