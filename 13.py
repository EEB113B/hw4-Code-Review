def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    rows=len(Matrix) #計算邊長

    def r_leftdown(tlen, matrix):  #以raw major 為基準 排列三角形
        tri_compress = []
        for x in range(tlen):
            for y in range(0, x+1):  
                tri_compress.append(matrix[x][y])
        return tri_compress
        
    def r_rightup(tlen, matrix):
        tri_compress = []
        for x in range(tlen): 
            for y in range(x, tlen):
                tri_compress.append(matrix[x][y])
        return tri_compress
        
    def r_leftup(tlen, matrix): 
        tri_compress = []
        for x in range(tlen):
            for y in range(tlen-x):   
                tri_compress.append(matrix[x][y])
        return tri_compress
        
    def r_rightdown(tlen, matrix):
        tri_compress = []
        for x in range(tlen):
            for y in range(tlen-x-1, tlen):
                tri_compress.append(matrix[x][y])
        return tri_compress
    
    count=0
    compress  = [] 
    
    while True:                                                                           
        for row in range(rows):
            for column in range(row+1,rows): #判斷三角左下
                count = Matrix[row][column] + count
            
        if count ==0:
            if Major == "r":                         
                compress = r_leftdown(rows, Matrix)
                break
                
            if Major == "c":                            
                Matrix = list(map(list, zip(*Matrix)))  ##作轉置矩陣 行列互換 
                compress = r_rightup(rows, Matrix) #上下左右顛倒         
                break
             
        count=0            
        for row in range(1, rows):
            for column in range(row): #右上
                count = Matrix[row][column] + count
        
        if count ==0:
            if Major == "r":
                compress = r_rightup(rows, Matrix)                             
                break
                
            if Major == "c":
                Matrix = list(map(list, zip(*Matrix)))  ##作轉置矩陣 行列互換 
                compress = r_leftdown(rows, Matrix)        #上下左右顛倒                          
                break
                
            
        count=0
        for row in range(1, rows):
            for column in range(rows-1,rows-row-1,-1):#左上
                count = Matrix[row][column] + count   
        
        if count ==0:
            if Major == "r":
                compress = r_leftup(rows, Matrix)               
                break
                
            if Major == "c":
                Matrix = list(map(list, zip(*Matrix)))  ##作轉置矩陣 行列互換 
                compress = r_leftup(rows, Matrix)   #ˇ不變
                break
            
            
        count=0 
        for row in range(rows-1):
            for column in range(rows-1-row):#右下
                count = Matrix[row][column] + count
        
        if count ==0:
            if Major == "r":
                compress = r_rightdown(rows, Matrix)                      
                break
                
            if Major == "c":
                Matrix = list(map(list, zip(*Matrix)))  ##作轉置矩陣 行列互換
                compress = r_rightdown(rows, Matrix)    #不變                              
                break          
        
        if count !=0:                #如果四個都不是 跳出迴圈並報錯
            return "wrong matrix"
            break
            
    return compress

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[7,0,0,0],
                    [8,3,0,0],
                   [4,6,5,0],
                   [0,5,6,7]]
    input_matrix = [[0,0,0,0,0,0],
[0,0,0,0,7,8],
[0,0,0,5,5,9],
[0,0,1,6,4,1],
[0,0,5,8,4,9],
[0,7,2,6,9,0]]
    


    output_array = to_1D_array(input_matrix, "r")
    print(output_array)
                                
#                                                          __----~~~~~~~~~~~------___
#                                   .  .   ~~//====......          __--~ ~~
#                    -.            \_|//     |||\\  ~~~~~~::::... /~
#                 ___-==_       _-~o~  \/    |||  \\            _/~~-
#         __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
#     _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
#   .~       .~       |   \\ -_    /  /-   /   ||      \   /
#  /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
#  |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\                                 
#           '         ~-|      /|    |-~\~~       __--~~
#                       |-~~-_/ |    |   ~\_   _-~            /\
#                            /  \     \__   \/~                \__
#                        _--~ _/ | .-~~____--~-/                  ~~==.
#                       ((->/~   '.|||' -_|    ~~-/ ,              . _||
#                                  -_     ~\      ~~---l__i__i__i--~~_/
#                                  _-~-__   ~)  \--______________--~~
#                                //.-~~~-~_--~- |-------~~~~~~~~
#                                       //.-~~~--\
#                                神獸保佑，程式碼沒Bug!
#                                      
#                                      rayyichen


#留言板