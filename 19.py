def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    
    a = b = c = d = 0
    ans = []
    
    for i in Matrix[0][1:]: #判斷左下三角矩陣
        a = a + i
    for i in Matrix[0][0:-1]: #判斷右下三角矩陣
        b = b + i
    for i in Matrix[-1][1:]: #判斷左上三角矩陣
        c = c + i
    for i in Matrix[-1][0:-1]: #判斷右上三角矩陣
        d = d + i
#================================================================
    if a == 0 and Major == 'r': #左下三角矩陣 row-major
        for i in range(len(Matrix)):
            for j in range(i+1):
                ans = ans + [Matrix[i][j]]
    if b == 0 and Major == 'r': #右下三角矩陣 row-major
        for i in range(len(Matrix)):
            for j in range(-(i+1), 0):
                ans = ans + [Matrix[i][j]]
    if c == 0 and Major == 'r': #左上三角矩陣 row-major
        for i in range(len(Matrix)):
            for j in range(0, len(Matrix)-i):
                ans = ans + [Matrix[i][j]]
    if d == 0 and Major == 'r': #右上三角矩陣 row-major
        for i in range(len(Matrix)):
            for j in range(i, len(Matrix)):
                ans = ans + [Matrix[i][j]]
#================================================================
    if a == 0 and Major == 'c': #左下三角矩陣 column-major
        for i in range(len(Matrix)):
            for j in range(i, len(Matrix)):
                ans = ans + [Matrix[j][i]]
    if b == 0 and Major == 'c': #右下三角矩陣 column-major
        for i in range(len(Matrix)):
            for j in range(-(i+1), 0):
                ans = ans + [Matrix[j][i]]
    if c == 0 and Major == 'c': #左上三角矩陣 column-major
        for i in range(len(Matrix)):
            for j in range(0, len(Matrix)-i):
                ans = ans + [Matrix[j][i]]
    if d == 0 and Major == 'c': #右上三角矩陣 column-major
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