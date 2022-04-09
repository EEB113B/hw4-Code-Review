def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    lst = Matrix
    m = Major
    total_top_right = 0
    total_top_left = 0
    total_lower_right = 0
    total_lower_left = 0
    lst_tri = []
       
    #用0的位置 來判斷三角形位置
    for i in range(0,len(lst)):   #判斷左下三角形矩陣   
        for j in range(i+1, len(lst[i])):
            total_lower_left += lst[i][j]
    if total_lower_left == 0:
        t_l_l = True
    else:
        t_l_l = False

    for i in range(1,len(lst)):   #判斷右上三角形矩陣   
        for j in range(0, i):
            total_top_right += lst[i][j]
    if total_top_right == 0:
        t_t_r = True
    else:
        t_t_r = False
    
    for i in range(0,len(lst)):   #判斷右下三角形矩陣
        for j in range(0, len(lst[i])-i-1):
            total_lower_right += lst[i][j]    
    if total_lower_right == 0:
        t_l_r = True
    else:
        t_l_r = False

    for i in range(1,len(lst)):   #判斷左上三角形矩陣
        for j in range(len(lst[i])-i, len(lst[i])):
            total_top_left += lst[i][j]
    if total_top_left ==0:
        t_t_l = True
    else:
        t_t_l = False
    
    #判斷Major並回傳題目要的東西
    if m =="r":   
        if t_l_l:
            for i in range(0,len(lst)):   #左下三角形矩陣  
                for j in range(0, i+1):
                    lst_tri.append(lst[i][j])

        elif t_t_r:
            for i in range(0,len(lst)):   #右上三角形矩陣   
                for j in range(i, len(lst[i])):
                    lst_tri.append(lst[i][j])

        elif t_l_r:
            for i in range(1,len(lst)):   #右下三角形矩陣
                for j in range(3-i, len(lst[i])):
                    lst_tri.append(lst[i][j])
        
        elif t_t_l:
            for i in range(0,len(lst)):   #左上三角形矩陣
                for j in range(0, len(lst[i])-i):
                    lst_tri.append(lst[i][j])

    
    if m =="c":
        if t_l_l:    #左下三角形矩陣            
            for j in range(0, len(lst[j])):
                for i in range(j, len(lst)):
                    lst_tri.append(lst[i][j])
                
            

        elif t_t_r:   #右上三角形矩陣
            for j in range(0, len(lst[j])):
                for i in range(0, j+1):
                    lst_tri.append(lst[i][j])

        elif t_l_r:   #右下三角形矩陣
            for j in range(0, len(lst[j])):
                for i in range(3-j, len(lst)):
                    lst_tri.append(lst[i][j])
        
        elif t_t_l:   #左上三角形矩陣
            for j in range(0, len(lst[j])):
                for i in range(0, 4-j):
                    lst_tri.append(lst[i][j])



    return  lst_tri# 回傳值型態:list

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