def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    ##以下三角皆以0做例
    ##例:三角形中0若尖端朝上且靠右==上右三角形，如下
    ## 110
    ## 100
    ## 000

    m=Matrix                                             ##將引數給予m
    decide=[]                                            ##設立空list，做後面判斷用，後面稱此為判斷list

    size = len(m)                                          ##計算矩陣長度
    inverter_m = [[None]*size for i in range(size)]        ##設立轉置矩陣需要的空矩陣
    count1_0 = []                                          ##計算原矩陣0數，所需要的list
    count2_0 = []                                          ##計算轉置矩陣0數，所需要的list
    
    ##上下三角判斷
    for i in range(size):
        count1_0.append(m[i].count(0))                   ##計算原矩陣每列0的數目，放入count1_0   

    if count1_0 == sorted(count1_0):                       ##若原矩陣每列0為小到大，則為上矩陣，將"上"加入判斷list中
        decide.append("上")
    else:                                                ##相反，若是原矩陣每列0為大到小，則為下矩陣，將"下"加入判斷list中
        decide.append("下")                              
    
    ##產生轉置矩陣
    for i in range(size):                                ##將原矩陣轉置後放入前面所製作的空轉置矩陣中
        for j in range(size):
            inverter_m[j][i] = m[i][j]
            
    ##左右三角形判斷    
    for i in range(size):                                ##計算轉置後的矩陣每列0的數目，放入count2_0
        count2_0.append(inverter_m[i].count(0))
        
    if count2_0 == sorted(count2_0):                        ##若轉置後的矩陣每列0為小到大，則為右矩陣，將"右"加入判斷list中
        decide.append("右")
    else:
        decide.append("左")                               ##相反，若是轉置後的矩陣每列0為大到小，則為左矩陣，將"左"加入判斷list中
        
        
        
    ##輸入為r    
    if "上" in decide and "左" in decide and Major == "r":  ##判斷list 若有上左兩字，且引數為r，則執行下列程式
        index = 0                                           ##建立指標
        B = [None] * ((1 + size) * size // 2)               ##建立空的一維陣列
        for i in range(size):                               ##每行掃入
            for j in range(i, size):                        ##掃入所需要的列
                B[index] = m[i][j]                          ##用空的一維陣列，將剛剛掃入m行列的值加入指標指入B的位置
                index += 1                                  ##指標+1
        
    
    if "上" in decide and "右" in decide and Major == "r":   ##判斷list 若有上右兩字，且引數為r，則執行下列程式
        index = 0                                            ##建立指標
        B = [None] * ((1 + size) * size // 2)                ##建立空的一維陣列
        for i in range(size):                                ##每行掃入
            for j in range(0,size-i):                        ##掃入所需要的列
                B[index] = m[i][j]                           ##用空的一維陣列，將剛剛掃入m行列的值加入指標指入B的位置
                index += 1                                   ##指標+1

    if "下" in decide and "左" in decide and Major == "r":   ##判斷list 若有下左兩字，且引數為r，則執行下列程式
        index = 0                                            ##建立指標
        B = [None] * ((1 + size) * size // 2)                ##建立空的一維陣列
        for i in range(size):                                ##每行掃入
            for j in range(size-i-1,size):                   ##掃入所需要的列
                B[index] = m[i][j]                           ##用空的一維陣列，將剛剛掃入m行列的值加入指標指入B的位置
                index += 1                                   ##指標+1

    if "下" in decide and "右" in decide and Major == "r":   ##判斷list 若有下右兩字，且引數為r，則執行下列程式
        index = 0                                            ##建立指標
        B = [None] * ((1 + size) * size // 2)                ##建立空的一維陣列
        for i in range(size):                                ##每行掃入
            for j in range(0, i+1):                          ##掃入所需要的列
                B[index] = m[i][j]                           ##用空的一維陣列，將剛剛掃入m行列的值加入指標指入B的位置
                index += 1                                   ##指標+1
    
    ##輸入為c           
    if "上" in decide and "左" in decide and Major == "c":   ##判斷list 若有上左兩字，且引數為c，則執行下列程式
        index = 0                                            ##建立指標
        B = [None] * ((1 + size) * size // 2)                ##建立空的一維陣列
        for i in range(size):                                ##每行掃入
            for j in range(0, i+1):                          ##掃入所需要的列
                B[index] = inverter_m[i][j]                  ##用空的一維陣列，將剛剛掃入m行列的值加入指標指入B的位置
                index += 1                                   ##指標+1
                
    if "上" in decide and "右" in decide and Major == "c":   ##判斷list 若有上右兩字，且引數為c，則執行下列程式
        index = 0                                            ##建立指標
        B = [None] * ((1 + size) * size // 2)                ##建立空的一維陣列
        for i in range(size):                                ##每行掃入
            for j in range(0,size-i):                        ##掃入所需要的列
                B[index] = inverter_m[i][j]                  ##用空的一維陣列，將剛剛掃入m行列的值加入指標指入B的位置
                index += 1                                   ##指標+1

    if "下" in decide and "左" in decide and Major == "c":   ##判斷list 若有下左兩字，且引數為c，則執行下列程式
        index = 0                                            ##建立指標
        B = [None] * ((1 + size) * size // 2)                ##建立空的一維陣列
        for i in range(size):                                ##每行掃入
            for j in range(size-i-1,size):                   ##掃入所需要的列
                B[index] = inverter_m[i][j]                  ##用空的一維陣列，將剛剛掃入m行列的值加入指標指入B的位置
                index += 1                                   ##指標+1

    if "下" in decide and "右" in decide and Major == "c":   ##判斷list 若有下右兩字，且引數為c，則執行下列程式
        index = 0                                            ##建立指標
        B = [None] * ((1 + size) * size // 2)                ##建立空的一維陣列
        for i in range(size):                                ##每行掃入
            for j in range(i, size):                         ##掃入所需要的列
                B[index] = inverter_m[i][j]                  ##用空的一維陣列，將剛剛掃入m行列的值加入指標指入B的位置
                index += 1                                   ##指標+1

    return B                                                 ##回傳一維陣列 B
    # 回傳值型態:list
##=======================================================================================================================================================##
##此為另一寫法，相較上面較為簡潔，但較為難懂
##將以下程式全部解除註解即可測試

#def handle_upandleft_r_and_downandright_c_array(m,size) : ##處理上左矩陣且傳入值為r或下右矩陣且傳入值為c，壓縮成一維矩陣
#    index = 0                                            ##建立指標
#    B = [None] * ((1 + size) * size // 2)                ##建立空的一維陣列
#    for i in range(size):                                ##每行掃入
#        for j in range(i, size):                         ##掃入所需要的列
#            B[index] = m[i][j]                  ##用空的一維陣列，將剛剛掃入m行列的值加入指標指入B的位置
#            index += 1                                   ##指標+1
#    return B

#def handle_upandright_r_c_array(m,size):                 ##處理上右矩陣且傳入值為r或c，壓縮成一維矩陣
#    index = 0                                            ##建立指標
#    B = [None] * ((1 + size) * size // 2)                ##建立空的一維陣列
#    for i in range(size):                                ##每行掃入
#        for j in range(0,size-i):                        ##掃入所需要的列
#            B[index] = m[i][j]                  ##用空的一維陣列，將剛剛掃入m行列的值加入指標指入B的位置
#            index += 1                                   ##指標+1
#    return B

#def handle_downandleft_r_c_array(m,size):                ##處理下左矩陣且傳入值為r或c，壓縮成一維矩陣
#    index = 0                                            ##建立指標
#    B = [None] * ((1 + size) * size // 2)                ##建立空的一維陣列
#    for i in range(size):                                ##每行掃入
#        for j in range(size-i-1,size):                   ##掃入所需要的列
#            B[index] = m[i][j]                  ##用空的一維陣列，將剛剛掃入m行列的值加入指標指入B的位置
#            index += 1                                   ##指標+1
#    return B

#def handle_downandright_r_upandleft_c_array(m,size):     ##處理下右矩陣且傳入值為r或上左矩陣且傳入值為c，壓縮成一維矩陣
#    index = 0                                            ##建立指標
#    B = [None] * ((1 + size) * size // 2)                ##建立空的一維陣列
#    for i in range(size):                                ##每行掃入
#        for j in range(0, i+1):                          ##掃入所需要的列
#            B[index] = m[i][j]                  ##用空的一維陣列，將剛剛掃入m行列的值加入指標指入B的位置
#            index += 1                                   ##指標+1
#    return B

#def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    ##以下三角皆以0做例
    ##例:三角形中0若尖端朝上且0靠右==上右三角形，如下
    ## 110
    ## 100
    ## 000
#    m=Matrix                                             
#    decide=[]                                            ##設立空list，做後面判斷用，後面稱此為判斷list
#    size = len(m)                                          ##計算矩陣長度
#    inverter_m = [[None]*size for i in range(size)]        ##設立轉置矩陣需要的空矩陣
#    count1_0 = []                                          ##計算原矩陣0數，所需要的list
#    count2_0 = []                                          ##計算轉置矩陣0數，所需要的list
    
    ##上下三角判斷
#    for i in range(size):
#        count1_0.append(m[i].count(0))                   ##計算原矩陣每列0的數目，放入count1_0   

#    if count1_0 == sorted(count1_0):                       ##若原矩陣每列0為小到大，則為上矩陣，將"上"加入判斷list中
#        decide.append("上")
#    else:                                                ##相反，若是原矩陣每列0為大到小，則為下矩陣，將"下"加入判斷list中
#        decide.append("下")                              
    
    ##產生轉置矩陣
#    for i in range(size):                                ##將原矩陣轉置後放入前面所製作的空轉置矩陣中
#        for j in range(size):
#            inverter_m[j][i] = m[i][j]
            
    ##左右三角形判斷    
#    for i in range(size):                                ##計算轉置後的矩陣每列0的數目，放入count2_0
#        count2_0.append(inverter_m[i].count(0))
        
#    if count2_0 == sorted(count2_0):                        ##若轉置後的矩陣每列0為小到大，則為右矩陣，將"右"加入判斷list中
#        decide.append("右")
#    else:
#        decide.append("左")                               ##相反，若是轉置後的矩陣每列0為大到小，則為左矩陣，將"左"加入判斷list中
 
#    if ("上" in decide and "左" in decide and Major == "r") or ("下" in decide and "右" in decide and Major == "c"):  ##判斷list 若有上左兩字且引數為r，或是下右且引數為c，則執行下列程式
#        if Major == "r":
#            B=handle_upandleft_r_and_downandright_c_array(m,size)                                                         ##引數為r，使用原矩陣
#        else:
#            B=handle_upandleft_r_and_downandright_c_array(inverter_m,size)                                                ##引數為c，使用轉置矩陣
#    if ("上" in decide and "右" in decide and Major == "r") or ("上" in decide and "右" in decide and Major == "c"):   ##判斷list 若有上右兩字且引數為r或c，則執行下列程式
#        if Major == "r":
#            B=handle_upandright_r_c_array(m,size)                                                                         ##引數為r，使用原矩陣
#        else:
#            B=handle_upandright_r_c_array(inverter_m,size)                                                                ##引數為c，使用轉置矩陣
#    if ("下" in decide and "左" in decide and Major == "r") or("下" in decide and "左" in decide and Major == "c"):   ##判斷list 若有下左兩字且引數為r或c，則執行下列程式
#        if Major == "r":
#            B=handle_downandleft_r_c_array(m,size)                                                                        ##引數為r，使用原矩陣
#        else:
#            B=handle_downandleft_r_c_array(inverter_m,size)                                                               ##引數為c，使用轉置矩陣  

#    if ("下" in decide and "右" in decide and Major =="r") or ("上" in decide and "左" in decide and Major == "c"):   ##判斷list 若有下右兩字且引數為r，或是上左且引數為c，則執行下列程式
#        if Major =="r":
#            B=handle_downandright_r_upandleft_c_array(m,size)                                                             ##引數為r，使用原矩陣
#        else:
#            B=handle_downandright_r_upandleft_c_array(inverter_m,size)                                                    ##引數為c，使用轉置矩陣
    

#    return B                                                 ##回傳一維陣列 B
    # 回傳值型態:list


if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix =   [[1,2,3,4],
                        [5,6,7,0],
                        [8,9,0,0],
                        [0,0,0,0]]

    output_array = to_1D_array(input_matrix, "c")
    print(output_array)


#留言板