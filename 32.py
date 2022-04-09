def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)
    ans_list = [None]*((size*(size + 1))//2)
    ans_list_len = len(ans_list)
    zero_count = size*size - ans_list_len     #計算n*n矩陣若是左、右/上、下角矩陣必須有幾個0才符合條件
    right_upper_zero_count = 0
    right_lower_zero_count = 0
    left_upper_zero_count = 0
    left_lower_zero_count = 0
    index = 0
    #對角線為左上到右下
    for i in range(size):
        for j in range(size):
            if j > i:       #對角線([0,0],[1,1]...)以上(不包含)算出0的個數
                if Matrix[i][j] == 0:
                    right_upper_zero_count +=1 
            if j < i:       #對角線([0,0],[1,1]...)以下(不包含)算出0的個數
                if  Matrix[i][j] == 0:
                    left_lower_zero_count +=1
    if right_upper_zero_count == zero_count:    #判斷是否為左下三角矩陣
        if Major == "r":
            for i in range(size):
                for j in range(i+1):
                    ans_list[index] = Matrix[i][j]        #依序將對角線以下(包含)的數值以row為主的方式填寫到ans_list
                    index +=1
        if Major == "c":
            for j in range(size):
                for i in range(j, size):
                    ans_list[index] = Matrix[i][j]        #依序將對角線以下(包含)的數值以column為主的方式填寫到ans_list
                    index +=1

    if left_lower_zero_count == zero_count:    #判斷是否為右上三角矩陣
        if Major == "r":
            for i in range(size):
                for j in range(i, size):
                    ans_list[index] = Matrix[i][j]        #依序將對角線以上(包含)的數值以row為主的方式填寫到ans_list
                    index +=1
        if Major == "c":
            for j in range(size):
                for i in range(j+1):
                    ans_list[index] = Matrix[i][j]        #依序將對角線以上(包含)的數值以column為主的方式填寫到ans_list
                    index +=1
    #對角線為右上到左下
    for i in range(size):
        for j in range(size):
            if i + j < size -1:     #對角線(ex:[2,0],[1,1],[0,2])以下(不包含)算出0的個數
                if  Matrix[i][j] == 0:
                    left_upper_zero_count +=1

            if i + j > size -1:     #對角線(ex:[2,0],[1,1],[0,2])以上(不包含)算出0的個數
                if  Matrix[i][j] == 0:
                    right_lower_zero_count +=1

    if left_upper_zero_count == zero_count:    #判斷是否為右下三角矩陣
        if Major == "r":
            for i in range(size):
                for j in range((size-1)-i, size):
                    ans_list[index] = Matrix[i][j]        #依序將對角線以下(包含)的數值以row為主的方式填寫到ans_list
                    index +=1
        if Major == "c":
            for j in range(size):
                for i in range((size-1)-j, size):            
                    ans_list[index] = Matrix[i][j]        #依序將對角線以下(包含)的數值以column為主的方式填寫到ans_list
                    index +=1

    if right_lower_zero_count == zero_count:    #判斷是否為左上三角矩陣
        if Major == "r":
            for i in range(size):
                for j in range(size -i):
                    ans_list[index] = Matrix[i][j]        #依序將對角線以上(包含)的數值以row為主的方式填寫到ans_list
                    index +=1
        if Major == "c":
            for j in range(size):
                for i in range(size -j):
                    ans_list[index] = Matrix[i][j]        #依序將對角線以上(包含)的數值以column為主的方式填寫到ans_list
                    index +=1

    return  ans_list     # 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,5,2,0],
                    [0,0,3,1],
                    [0,0,0,7],
                    [0,0,0,0]]

    output_array = to_1D_array(input_matrix, "c")
    print(output_array)

#留言板