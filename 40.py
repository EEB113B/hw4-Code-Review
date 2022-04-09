from tarfile import LENGTH_PREFIX


def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    
    length = len(input_matrix)
    upright = True
    downright = True
    upleft = True
    downleft = True
    
    #判斷是哪種三角形 
    #右上三角形       
    for i in range(length):
        for j in range(0,i):
            if input_matrix[i][j] != 0:
                upright = False
        
    #右下三角形
    for i in range(length):
        for j in range(length-i-1):
            if input_matrix[i][j] != 0:
                downright = False
            
    #左上三角形
    for i in range(length):
        for j in range(length-i,length):
            if input_matrix[i][j] != 0:
                upleft = False
    
    #左下三角形        
    for i in range(length):
        for j in range(i+1,length):
            if input_matrix[i][j] != 0:
                downleft = False
    #判斷相應位置是否為0，若不是0，則非那個三角形矩陣
    
    B = [None] * ((1 + length) * length // 2)#B為相應大小的list
    
    #將矩陣壓縮成一為陣列
    if upright:#經過上面的判斷如果是True則會繼續執行
        if Major == "r":#判斷輸入是"r"或"c"再做處理
            index = 0
            for i in range(length):
                for j in range(i, length):
                    B[index] = input_matrix[i][j]
                    index += 1#將三角形矩陣放入B list
        
        elif Major == "c":#判斷輸入是"r"或"c"再做處理
            index = 0
            for j in range(length):
                for i in range(j+1):
                    B[index] = input_matrix[i][j]
                    index += 1#將三角形矩陣放入B list
        
    elif downright:#經過上面的判斷如果是True則會繼續執行
        if Major == "r":#判斷輸入是"r"或"c"再做處理
            index = 0
            for i in range(length):
                for j in range(length-i-1,length):
                    B[index] = input_matrix[i][j]
                    index += 1#將三角形矩陣放入B list
        
        elif Major == "c":#判斷輸入是"r"或"c"再做處理
            index = 0
            for j in range(length):
                for i in range(length-j-1,length):
                    B[index] = input_matrix[i][j]
                    index += 1#將三角形矩陣放入B list
        
    elif upleft:#經過上面的判斷如果是True則會繼續執行
        if Major == "r":#判斷輸入是"r"或"c"再做處理
            index = 0
            for i in range(length):
                for j in range(length-i):
                    B[index] = input_matrix[i][j]   
                    index += 1#將三角形矩陣放入B list
        
        elif Major == "c":#判斷輸入是"r"或"c"再做處理
            index = 0
            for j in range(length):
                for i in range(length-j):
                    B[index] = input_matrix[i][j]
                    index += 1#將三角形矩陣放入B list
        
    elif downleft:#經過上面的判斷如果是True則會繼續執行
        if Major == "r":#判斷輸入是"r"或"c"再做處理
            index = 0
            for i in range(length):
                for j in range(0, i+1):
                    B[index] = input_matrix[i][j]
                    index += 1#將三角形矩陣放入B list
        
        elif Major == "c":#判斷輸入是"r"或"c"再做處理
            index = 0
            for j in range(length):
                for i in range(j,length):
                    B[index] = input_matrix[i][j]
                    index += 1#將三角形矩陣放入B list
        
    
    return B
# 回傳值型態:list

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