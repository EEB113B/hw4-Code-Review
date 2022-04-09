def to_1D_array(A, Major): 
    size = len(A)
    B = [None] * ((1 + size) * size // 2)
    A_type = ""
    count = {'ur':0, 'ul':0, 'll':0, 'lr':0}
    #在三角形矩陣中空白處是否都為零
    #利用方形矩陣的特性判斷
    for i in range(size):
        for j in range(size):
            #判斷右上三角形矩陣
            if i > j and A[i][j] == 0:
                count['ur'] += 1 #upper_right

            #判斷左上三角形矩陣
            if i + j > size-1 and A[i][j] == 0:
                count['ul'] += 1 #upper_left

            #判斷左下三角形矩陣
            if i < j and A[i][j] == 0:
                count['ll'] += 1 #lower_left

            #判斷右下三角形矩陣
            if i + j < size-1 and A[i][j] == 0:
                count['lr'] += 1 #lower_right

    #利用三角形區域內零的出現次數來判斷
    s_count = sorted(count.items(), key=lambda d : -d[1])
    A_type = s_count[0][0]
    #判斷要求為行還是列
    index = 0
    
    if Major == "r":
        for i in range(size):
                for j in range(size):
        #分為不同矩陣討論
                    if A_type == "ur":
                        if i <= j:
                            B[index] = A[i][j]
                            index += 1
        
                    elif A_type == "ul":
                        if i + j < size:
                            B[index] = A[i][j]
                            index += 1
        
                    elif A_type == "lr":
                        if i + j > size:
                            B[index] = A[i][j]
                            index += 1

                    elif A_type == "ll":
                        if i >= j:
                            B[index] = A[i][j]
                            index += 1

    if Major == "c":
        for i in range(size):
                for j in range(size):
        
                    if A_type == "ur":
                        if i >= j:
                            B[index] = A[j][i]
                            index += 1

                    elif A_type == "ul":
                        if i + j <= size-1:
                            B[index] = A[j][i]
                            index += 1

                    elif A_type == "lr":
                        if i+j >= size-1:
                            B[index] = A[j][i]
                            index += 1

                    elif A_type == "ll":
                        if i <= j:
                            B[index] = A[j][i]
                            index += 1

    return B            
if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,5,2,0], [0,0,3,1], [0,0,0,7], [0,0,0,0]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板