def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)
    index = 0
    output_array = [None] * ((size + 1) * size // 2) #生成一個空list來存放壓縮的資料
    right_upper = True
    left_upper = True
    right_lower = True
    left_lower = True #假設四種三角形都成立
    
    for i in range(1, len(Matrix)): #檢查右上三角形矩陣應為0的項
        for j in range(i):
            if Matrix[i][j] != 0: #假如這個範圍有不是0的項
                right_upper = False #則此矩陣不是右上三角形矩陣
    
    for i in range(1, len(Matrix)): #檢查左上三角形矩陣應為0的項
        for j in range(len(Matrix) - i, len(Matrix)):
            if Matrix[i][j] != 0: #假如這個範圍有不是0的項
                left_upper = False #則此矩陣不是左上三角形矩陣

    for i in range(len(Matrix) - 1): #檢查右下三角形矩陣應為0的項
        for j in range(len(Matrix) - i - 1):
            if Matrix[i][j] != 0: #假如這個範圍有不是0的項
                right_lower = False #則此矩陣不是右下三角形矩陣

    for i in range(len(Matrix) - 1): #檢查左下三角形矩陣應為0的項
        for j in range(1 + i, len(Matrix)):
            if Matrix[i][j] != 0: #假如這個範圍有不是0的項
                left_lower = False #則此矩陣不是左下三角形矩陣
    
    if right_upper: #如果是右上矩陣
        if Major == "r": #如果要以列為主
            for i in range(len(Matrix)):
                for j in range(i, len(Matrix)):
                    output_array[index] = Matrix[i][j] #逐項加入out_put_array
                    index += 1 #將存取壓縮資料的index移至下一項
        
        elif Major == "c": #如果要以行為主
            for j in range(len(Matrix)):
                for i in range(j + 1):
                    output_array[index] = Matrix[i][j] #逐項加入out_put_array
                    index += 1 #將存取壓縮資料的index移至下一項
    
    if left_upper:
        if Major == "r": #如果要以列為主
            for i in range(len(Matrix)):
                for j in range(len(Matrix) - i):
                    output_array[index] = Matrix[i][j] #逐項加入out_put_array
                    index += 1 #將存取壓縮資料的index移至下一項
        
        elif Major == "c": #如果要以行為主
            for j in range(len(Matrix)):
                for i in range(len(Matrix) - j ):
                    output_array[index] = Matrix[i][j] #逐項加入out_put_array
                    index += 1 #將存取壓縮資料的index移至下一項
    
    if right_lower:
        if Major == "r": #如果要以列為主
            for i in range(len(Matrix)):
                for j in range(len(Matrix) - i - 1, len(Matrix)):
                    output_array[index] = Matrix[i][j] #逐項加入out_put_array
                    index += 1 #將存取壓縮資料的index移至下一項
        
        elif Major == "c": #如果要以行為主
            for j in range(len(Matrix)):
                for i in range(len(Matrix) - j -1, len(Matrix)):
                    output_array[index] = Matrix[i][j] #逐項加入out_put_array
                    index += 1 #將存取壓縮資料的index移至下一項
    
    if left_lower:
        if Major == "r": #如果要以列為主
            for i in range(len(Matrix)):
                for j in range(0, i+1):
                    output_array[index] = Matrix[i][j] #逐項加入out_put_array
                    index += 1 #將存取壓縮資料的index移至下一項
       
        elif Major == "c": #如果要以行為主
            for j in range(len(Matrix)):
                for i in range(len(Matrix) - j ):
                    output_array[index] = Matrix[i + j][j] #逐項加入out_put_array
                    index += 1 #將存取壓縮資料的index移至下一項
    
    return output_array #回傳存取壓縮資料的list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,5,2,0],
                    [0,0,3,1],
                    [0,0,0,7],
                    [0,0,0,0]]

    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板