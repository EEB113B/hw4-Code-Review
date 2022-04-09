def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    r = len(Matrix)       #判斷列的個數，list裡一維代表列
    c = len(Matrix[0])    #判斷行的個數，利用第一列有幾項判斷

    ll = lu = rl = ru =0   
    for i in Matrix[0][1:]: #left-lower判斷式
        ll = ll + i         #將矩陣第一列由第二項開始依序將值放入ll
    for i in Matrix[1][2:]: 
        ll = ll + i         #將矩陣第二列由第三項開始依序將值放入ll
    for i in Matrix[0][0:-1]: #right-lower判斷式
        rl = rl + i           #將矩陣第一列由第一項開始至最後項依序將值放入rl
    for i in Matrix[1][0:-2]: 
        rl = rl + i           #將矩陣第二列由第一項開始至次後項依序將值放入rl
    for i in Matrix[-1][1:]: #left-upper判斷式
        lu = lu + i          #將矩陣最後列由第二項開始依序將值放入lu
    for i in Matrix[-2][2:]: 
        lu = lu + i          #將矩陣次後列由第三項開始依序將值放入lu
    for i in Matrix[-1][0:-1]: #right-upper判斷式
        ru = ru + i            #將矩陣最後列由第一項開始至最後項依序將值放入ru
    for i in Matrix[-2][0:-2]: 
        ru = ru + i            #將矩陣次後列由第一項開始至次後項依序將值放入ru

    array = []
    if Major == "r":
        if ll == 0: #left-lower row壓縮
            for i in range(len(Matrix)):
                for j in range(i+1):
                    array = array + [Matrix[i][j]]
        elif rl == 0: #right-lower row壓縮
            for i in range(len(Matrix)):
                for j in range(-(i+1), 0):
                    array = array + [Matrix[i][j]]
        elif lu == 0: #left-upper row壓縮
            for i in range(len(Matrix)):
                for j in range(0, len(Matrix)-i):
                    array = array + [Matrix[i][j]]
        elif ru == 0: #right-upper row壓縮
            for i in range(len(Matrix)):
                for j in range(i, len(Matrix)):
                    array = array + [Matrix[i][j]]


    elif Major == "c":
        if ll == 0: #left-lower column壓縮
            for i in range(len(Matrix)):
                for j in range(i, len(Matrix)):
                    array = array + [Matrix[j][i]]
        elif rl == 0: #right-lower column壓縮
            for i in range(len(Matrix)):
                for j in range(-(i+1), 0):
                    array = array + [Matrix[j][i]]
        elif lu == 0: #left-upper column壓縮
            for i in range(len(Matrix)):
                for j in range(0, len(Matrix)-i):
                    array = array + [Matrix[j][i]]
        elif ru == 0: #right-upper column壓縮
            for i in range(len(Matrix)):
                for j in range(i+1):
                    array = array + [Matrix[j][i]]
        
    return array  # 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrixc = [[7,0,0,0],
                    [8,3,0,0],
                    [4,6,5,0],
                    [0,5,6,7]]
    output_arrayc = to_1D_array(input_matrixc, "c")
    input_matrixr = [[7,0,0,0],
                    [8,3,0,0],
                    [4,6,5,0],
                    [0,5,6,7]]
    output_arrayr = to_1D_array(input_matrixr, "r")
    print(output_arrayc,output_arrayr)


#留言板