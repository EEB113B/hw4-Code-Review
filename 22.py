def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    r = len(Matrix)    #r
    c = len(Matrix[0])    #c, r*c Matrix

    left_down = right_down = left_up = right_up =0   
    for i in Matrix[0][1:]:                 #left_down  左下
        left_down = left_down + i
    for i in Matrix[1][2:]: 
        left_down = left_down + i
    for i in Matrix[0][0:-1]:               #right_down 右下
        right_down = right_down + i
    for i in Matrix[1][0:-2]: 
       right_down = right_down + i
    for i in Matrix[-1][1:]:                #left_up    左上
        left_up = left_up + i
    for i in Matrix[-2][2:]: 
        left_up = left_up + i
    for i in Matrix[-1][0:-1]:              #right_up   右上
        right_up = right_up + i
    for i in Matrix[-2][0:-2]: 
        right_up = right_up + i

    ans = []
    if Major == "r":
        if left_down == 0:                  #左下三角排壓縮
            for i in range(len(Matrix)):
                for j in range(i+1):
                    ans = ans + [Matrix[i][j]]
        elif right_down == 0:               #右下三角排壓縮
            for i in range(len(Matrix)):
                for j in range(-(i+1), 0):
                    ans = ans + [Matrix[i][j]]
        elif left_up == 0:                  #左上三角排壓縮
            for i in range(len(Matrix)):
                for j in range(0, len(Matrix)-i):
                    ans = ans + [Matrix[i][j]]
        elif right_up == 0:                 #右上三角排壓縮
            for i in range(len(Matrix)):
                for j in range(i, len(Matrix)):
                    ans = ans + [Matrix[i][j]]


    elif Major == "c":
        if left_down == 0:                  #左下三角行壓縮
            for i in range(len(Matrix)):
                for j in range(i, len(Matrix)):
                    ans = ans + [Matrix[j][i]]
        elif right_down == 0:               #右下三角行壓縮
            for i in range(len(Matrix)):
                for j in range(-(i+1), 0):
                    ans = ans + [Matrix[j][i]]
        elif left_up == 0:                  #左上三角行壓縮
            for i in range(len(Matrix)):
                for j in range(0, len(Matrix)-i):
                    ans = ans + [Matrix[j][i]]
        elif right_up == 0:                 #右上三角行壓縮
            for i in range(len(Matrix)):
                for j in range(i+1):
                    ans = ans + [Matrix[j][i]]
        
    return ans



    
    return # 回傳值型態:list

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