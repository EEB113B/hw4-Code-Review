def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    len_matrix = len(Matrix) #因為是方陣，所以用len_matrix來代表階層
    count0 = 0 #count0用來計算三角形矩陣裡為0的那一側有幾個0
    count1 = 0 #count1~4分別用來存取右下、左下、右上、左上三角形裡有幾個0
    count2 = 0
    count3 = 0
    count4 = 0
    final_list = []#最後要return的矩陣list

    for k in range(1, len_matrix):#計算三角形矩陣中三角形為0的那一側有幾個0，若為n階，則會有1+2+...+(n-1)個0
        count0 = count0+k
    if Major == "c":
        for i in range(0,len_matrix-1):#13、14行的for用來計算左上三角形裡是否都為0
            for j in range(0,len_matrix-1-i):
                if Matrix[i][j] == 0:
                    count1 = count1 + 1
                if count1 == count0: #如果左上三角形裡的0數量等於該階層三角形矩陣為0那一側的0數量，代表此矩陣為右下三角矩陣
                    for n in range(0,len_matrix):#因為是右下三角矩陣，所以18、19行的for用來將右下三角的元素依照垂直壓縮放進list裡
                        for m in range(len_matrix-n-1,len_matrix):
                            final_list.append(Matrix[m][n])
                    return final_list
                
            for j in range(i+1,len_matrix):#13、23行的for用來計算右上三角形裡是否都為0
                if Matrix[i][j] == 0:
                    count2 = count2 + 1
                if count2 == count0:#如果右上三角形裡的0數量等於該階層三角形矩陣為0那一側的0數量，代表此矩陣為左下三角矩陣
                    for n in range(0,len_matrix):#因為是左下三角矩陣，所以18、19行的for用來將左下三角的元素依照垂直壓縮放進list裡
                        for m in range(n,len_matrix):
                            final_list.append(Matrix[m][n])
                    return final_list
            for j in range(0,i+1):#13、31行的for用來計算左下三角形裡是否都為0
                if Matrix[i+1][j] == 0:
                    count3 = count3 + 1
                if count3 == count0:#如果左下三角形裡的0數量等於該階層三角形矩陣為0那一側的0數量，代表此矩陣為右上三角矩陣
                    for n in range(0,len_matrix):#因為是右上三角矩陣，所以18、19行的for用來將右上三角的元素依照垂直壓縮放進list裡
                        for m in range(0,n+1):
                            final_list.append(Matrix[m][n])
                    return final_list
            for j in range(len_matrix-1-i,len_matrix):#13、39行的for用來計算右下三角形裡是否都為0
                if Matrix[i+1][j] == 0:
                    count4 = count4 + 1
                if count4 == count0:#如果右下三角形裡的0數量等於該階層三角形矩陣為0那一側的0數量，代表此矩陣為左上三角矩陣
                    for n in range(0,len_matrix):#因為是左上三角矩陣，所以18、19行的for用來將左上三角的元素依照垂直壓縮放進list裡
                        for m in range(0,len_matrix-n):
                            final_list.append(Matrix[m][n])
                    return final_list
    if Major == "r":#抓取元素的順序不同，其他都一樣
        for i in range(0,len_matrix-1):
            for j in range(0,len_matrix-1-i):
                if Matrix[i][j] == 0:
                    count1 = count1 + 1
                if count1 == count0:
                    for m in range(0,len_matrix):#因為是右下三角矩陣，所以53、54行的for用來將右下三角的元素依照水平壓縮放進list裡
                        for n in range(len_matrix-m-1,len_matrix):
                            final_list.append(Matrix[m][n])
                    return final_list
                
            for j in range(i+1,len_matrix):
                if Matrix[i][j] == 0:
                    count2 = count2 + 1
                if count2 == count0:
                    for m in range(0,len_matrix):#因為是左下三角矩陣，所以62、63行的for用來將左下三角的元素依照水平壓縮放進list裡
                        for n in range(0,m+1):
                            final_list.append(Matrix[m][n])
                    return final_list
            for j in range(0,i+1):
                if Matrix[i+1][j] == 0:
                    count3 = count3 + 1
                if count3 == count0:
                    for m in range(0,len_matrix):#因為是右上三角矩陣，所以70、71行的for用來將右上三角的元素依照水平壓縮放進list裡
                        for n in range(m,len_matrix):
                            final_list.append(Matrix[m][n])
                    return final_list
            for j in range(len_matrix-1-i,len_matrix):
                if Matrix[i+1][j] == 0:
                    count4 = count4 + 1
                if count4 == count0:
                    for m in range(0,len_matrix):#因為是左上三角矩陣，所以78、79行的for用來將左上三角的元素依照水平壓縮放進list裡
                        for n in range(0,len_matrix-m):
                            final_list.append(Matrix[m][n])
                    return final_list
    
    #return # 回傳值型態:list

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