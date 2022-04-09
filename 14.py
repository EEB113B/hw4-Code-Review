def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    matrix = Matrix
    size = len(matrix)
    Matrix = [None] * ((1 + size) * size // 2)
    row0_count = 0
    row_end_count = 0   #計算第0列0的數量和最後一列0的數量
    for i in range(size):
        for j in range(size):
            if matrix[0][j] == 0:
                row0_count += 1
            if matrix[i][j] == 0:
                row_end_count += 1    
    
    column_0_count = 0 
    column_end_count = 0  #計算第0行0的數量和最後一行0的數量
    for i in range(size):
            for j in range(size):
                if matrix[i][0] == 0:
                     column_0_count += 1
                if matrix[i][j] == 0:
                     column_end_count += 1
    if  row0_count > row_end_count:   # index第0列的0總數>index最後一列的0總數，代表為下三角形
        if column_0_count > column_end_count: # index第0行的0總數>index最後一行的0總數，代表為右下三角形
            index = 0
            for i in range(size):
                for j in range(i-2,size):
                    Matrix[index] = matrix[i][j]
                    index += 1
            print('[', end='')
            for i in range(size):
                print(f' {Matrix[i]}', end='')
            print(' ]')
        
        if column_0_count < column_end_count: # index第0行的0總數<index最後一行的0總數，代表為左下三角形
            index = 0
            for i in range(size):
                for j in range(0,i+1):
                    Matrix[index] = matrix[i][j]
                    index += 1
            print('[', end='')
            for i in range(size):
                print(f' {Matrix[i]}', end='')
            print(' ]')
    
    if  row0_count < row_end_count: # index第0列的0總數<index最後一列的0總數，代表為上三角形
        if column_0_count > column_end_count: # index第0行的0總數>index最後一行的0總數，代表為右上三角形
            index = 0
            for i in range(size):
                for j in range(i, size):
                    Matrix[index] = matrix[i][j]
                    index += 1
            print('[', end='')
            for i in range(size):
                print(f' {Matrix[i]}', end='')
            print(' ]')
        if column_0_count < column_end_count: # index第0行的0總數<index最後一行的0總數，代表為左上三角形
            index = 0
            for i in range(size):
                for j in range(i, size-1):
                    Matrix[index] = matrix[i][j]
                    index += 1
            print('[', end='')
            for i in range(size):
                print(f' {Matrix[i]}', end='')
            print(' ]')

    return # 回傳值型態:list

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