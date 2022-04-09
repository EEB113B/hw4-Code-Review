def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    r = len(Matrix)    #r
    c = len(Matrix[0])    #c, r*c Matrix

    ld = lu = rd = ru =0   
    for i in Matrix[0][1:]:                             #此為左下之判斷式
        ld = ld + i
    for i in Matrix[1][2:]: 
        ld = ld + i
    for i in Matrix[0][0:-1]:                           #此為右下之判斷式
        rd = rd + i
    for i in Matrix[1][0:-2]: 
        rd = rd + i
    for i in Matrix[-1][1:]:                            #此為左上之判斷式
        lu = lu + i
    for i in Matrix[-2][2:]: 
        lu = lu + i
    for i in Matrix[-1][0:-1]:                          #此為右上之判斷式
        ru = ru + i
    for i in Matrix[-2][0:-2]: 
        ru = ru + i

    ans = []
    if Major == "r":
        if ld == 0:                                     #左下三角水平壓縮major
            for i in range(len(Matrix)):
                for j in range(i+1):
                    ans = ans + [Matrix[i][j]]
        elif rd == 0:                                   #右下三角水平壓縮之major
            for i in range(len(Matrix)):
                for j in range(-(i+1), 0):
                    ans = ans + [Matrix[i][j]]
        elif lu == 0:                                   #左上三角水平壓縮major
            for i in range(len(Matrix)):
                for j in range(0, len(Matrix)-i):
                    ans = ans + [Matrix[i][j]]
        elif ru == 0:                                   #右上三角水平壓縮major
            for i in range(len(Matrix)):
                for j in range(i, len(Matrix)):
                    ans = ans + [Matrix[i][j]]


    elif Major == "c":
        if ld == 0:                                     #左下三角垂直壓縮major
            for i in range(len(Matrix)):
                for j in range(i, len(Matrix)):
                    ans = ans + [Matrix[j][i]]
        elif rd == 0:                                   #右下三角垂直壓縮major
            for i in range(len(Matrix)):
                for j in range(-(i+1), 0):
                    ans = ans + [Matrix[j][i]]
        elif lu == 0:                                   #左上三角垂直壓縮major
            for i in range(len(Matrix)):
                for j in range(0, len(Matrix)-i):
                    ans = ans + [Matrix[j][i]]
        elif ru == 0:                                   #右上三角垂直壓縮major
            for i in range(len(Matrix)):
                for j in range(i+1):
                    ans = ans + [Matrix[j][i]]
        
    return ans



    
    return # 回傳值:list

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