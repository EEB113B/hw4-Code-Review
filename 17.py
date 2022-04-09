def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix) #先計算出該矩陣大小
    lst = [None] * ((1 + size) * size // 2) #lst為最後要回傳的list
    a = 0    #a,b,c,d分別代表四種矩陣判斷標準
    b = 0
    c = 0
    d = 0
    right_up = False    #右上三角形    #一開始先設四種矩陣均為False，若判斷出是哪種矩陣，則該類型矩陣轉為True，接著跳到下一步計算
    right_down = False  #右下三角形
    left_up = False     #左上三角形
    left_down = False   #左下三角形
#--------------------------------------------------右上三角形矩陣判斷--------------------------------------------------
    for y in range(size):
        for x in range(0, y):
            if (Matrix[y][x]==0):                #依照右上三角形矩陣特性設計判斷式
                a += 1                           #a計算左下角由0組成的三角形中0的數量
    if a == ((1+(size-1))*(size-1))//2:          #若左下角由0組成的三角形中0的數量符合理論值(((1+(size-1))*(size-1))//2)
        right_up = True                          #則代表該矩陣為右上三角形矩陣
#--------------------------------------------------左上三角形矩陣判斷--------------------------------------------------
    if right_up == False :  #若非右上三角形矩陣，再判斷是否為左上三角形矩陣(節省計算時間)
        for y in range(size):
            for x in range(size-y, size):        
                if (Matrix[y][x]==0):            #依照左上三角形矩陣特性設計判斷式
                    b += 1                       #b計算右下角由0組成的三角形中0的數量
        if b == ((1+(size-1))*(size-1))//2:      #若右下角由0組成的三角形中0的數量符合理論值(((1+(size-1))*(size-1))//2)
            left_up = True                       #則代表該矩陣為左上三角形矩陣
#--------------------------------------------------左下三角形矩陣判斷-------------------------------------------------- 
    if right_up == left_up == False : #若非右上三角形、左上三角形矩陣矩陣，再判斷是否為左下三角形矩陣(節省計算時間)
        for y in range(size-1):
            for x in range(y+1, size):
                if (Matrix[y][x]==0):            #依照左下三角形矩陣特性設計判斷式
                    c += 1                       #c計算右上角由0組成的三角形中0的數量
        if c == ((1+(size-1))*(size-1))//2:      #若右上角由0組成的三角形中0的數量符合理論值(((1+(size-1))*(size-1))//2)
            left_down = True                     #則代表該矩陣為左下三角形矩陣
#--------------------------------------------------右下三角形矩陣判斷--------------------------------------------------     
    if right_up == left_up == left_down == False : #若非右上三角形、左上三角形、左下三角形矩陣矩陣，再判斷是否為右下三角形矩陣(節省計算時間)
        for y in range(size-1):
            for x in range(0, size-(y+1)):        
                if (Matrix[y][x]==0):            #依照右下三角形矩陣特性設計判斷式
                    d += 1                       #d計算左上角由0組成的三角形中0的數量
        if d == ((1+(size-1))*(size-1))//2:      #若左上角由0組成的三角形中0的數量符合理論值(((1+(size-1))*(size-1))//2)
            right_down = True                    #則代表該矩陣為右下三角形矩陣
#------------------------------------------------------------------------------
    if right_up == True:   #若矩陣為右上三角形矩陣，則進行這一區塊程式
        if Major == 'r':   #輸入選擇Row-Major                          
            index = 0      #變數index為最後要回傳的list之index
            for y in range(size):                 #依照Row-Major之特性把二維矩陣壓縮成一維矩陣
                for x in range(y, size):
                    lst[index] = Matrix[y][x]     #利用for迴圈一個一個紀載數值進lst中   
                    index += 1                       
        elif Major == 'c': #輸入選擇Column-Major
            index = 0      #變數index為最後要回傳的list之index
            for x in range(size):                 #依照Column-Major之特性把二維矩陣壓縮成一維矩陣
                for y in range(0, x+1):
                    lst[index] = Matrix[y][x]     #利用for迴圈一個一個紀載數值進lst中
                    index += 1   
#-------------------------------------------------------------------------------                 
    if left_up == True:   #若矩陣為左上三角形矩陣，則進行這一區塊程式
        if Major == 'r':  #輸入選擇Row-Major
            index = 0
            for y in range(size):                  #內容參考右上三角形矩陣壓縮過程，依照類似邏輯更改x,y範圍已達成壓縮左上三角形矩陣目標
                for x in range(0, size-y):
                    lst[index] = Matrix[y][x]
                    index += 1
        elif Major == 'c': #輸入選擇Column-Major
            index = 0
            for x in range(size):
                for y in range(0, size-x):
                    lst[index] = Matrix[y][x]
                    index += 1               
#-------------------------------------------------------------------------------
    if left_down == True:  #若矩陣為左下三角形矩陣，則進行這一區塊程式
        if Major == 'r': #輸入選擇Row-Major
            index = 0
            for y in range(size):
                for x in range(0, y+1):
                    lst[index] = Matrix[y][x]     #內容參考右上三角形矩陣壓縮過程，依照類似邏輯更改x,y範圍已達成壓縮左下三角形矩陣目標
                    index += 1
        elif Major == 'c': #輸入選擇Column-Major
            index = 0
            for x in range(size):
                for y in range(x, size):
                    lst[index] = Matrix[y][x]
                    index += 1            
#-------------------------------------------------------------------------------
    if right_down == True:  #若矩陣為右下三角形矩陣，則進行這一區塊程式
        if Major == 'r': #輸入選擇Row-Major
            index = 0
            for y in range(size):
                for x in range(size-1-y, size):
                    lst[index] = Matrix[y][x]     #內容參考右上三角形矩陣壓縮過程，依照類似邏輯更改x,y範圍已達成壓縮右下三角形矩陣目標
                    index += 1
        elif Major == 'c': #輸入選擇Column-Major
            index = 0
            for x in range(size):
                for y in range(size-1-x, size):
                    lst[index] = Matrix[y][x]
                    index += 1    
    return lst # 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,0,0,0,0,0],
                    [0,0,0,0,7,8],
                    [0,0,0,5,5,9],
                    [0,0,1,6,4,1],
                    [0,0,5,8,4,9],
                    [0,7,2,6,9,0]]

    output_array = to_1D_array(input_matrix, "c")
    print(output_array)


#留言板