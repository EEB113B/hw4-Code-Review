def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
     x = y = z = l = 0
     ans = []
    
     for i in Matrix[0][1:]: #左下三角
        x = x + i
     for i in Matrix[0][0:-1]: #右下三角
        y = y + i
     for i in Matrix[-1][1:]: #左上三角
        z = z + i
     for i in Matrix[-1][0:-1]: #右上三角
        l = l + i

     if x == 0 and Major == 'r': #左下三角row
        for i in range(len(Matrix)):
            for j in range(i+1):
                ans = ans + [Matrix[i][j]]
     if y == 0 and Major == 'r': #右下三角row
        for i in range(len(Matrix)):
            for j in range(-(i+1), 0):
                ans = ans + [Matrix[i][j]]
     if z == 0 and Major == 'r': #左上三角row
        for i in range(len(Matrix)):
            for j in range(0, len(Matrix)-i):
                ans = ans + [Matrix[i][j]]
     if l == 0 and Major == 'r': #右上三角row
        for i in range(len(Matrix)):
            for j in range(i, len(Matrix)):
                ans = ans + [Matrix[i][j]]

     if x == 0 and Major == 'c': #左下三角column
        for i in range(len(Matrix)):
            for j in range(i, len(Matrix)):
                ans = ans + [Matrix[j][i]]
     if y == 0 and Major == 'c': #右下三角column
        for i in range(len(Matrix)):
            for j in range(-(i+1), 0):
                ans = ans + [Matrix[j][i]]
     if z == 0 and Major == 'c': #左上三角column
        for i in range(len(Matrix)):
            for j in range(0, len(Matrix)-i):
                ans = ans + [Matrix[j][i]]
     if l == 0 and Major == 'c': #右上三角column
        for i in range(len(Matrix)):
            for j in range(i+1):
                ans = ans + [Matrix[j][i]]
    
     return ans # 回傳值型態:list

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