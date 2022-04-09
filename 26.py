def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    A=Matrix
    #ans=[]
    size = len(A)
    size_1= len(A)-1
    B = [None] * ((1 + size) * size // 2)   #宣告大小為((1 + size) * size // 2)的串列B
    D=[0]*((1 + size_1) * size_1 // 2)  #宣告大小為((1 + size_1) * size_1 // 2)的全0串列D
    rd=[None] * ((1 + size_1) * size_1 // 2)  #宣告大小為((1 + size_1) * size_1 // 2)的串列rd
    lu=[None] * ((1 + size_1) * size_1 // 2)
    ru=[None] * ((1 + size_1) * size_1 // 2)
    ld=[None] * ((1 + size_1) * size_1 // 2)
    

    #右下三角形
    index=0 
    for i in range(size-1):
        for j in range(size-i-2,-1,-1): #抓出左上小三角形
            rd[index] = A[i][j] #壓縮成一維陣列rd
            index += 1
    if rd==D:   #如果左上小三角形全是0
        if Major=="r":  #用列運算
            index=0
            for i in range(size):
                for j in range(size-i-1,size):
                    B[index] = A[i][j]  #壓縮成一維陣列B
                    index += 1
            return B    #回傳B用列運算的右下三角形
        if Major=="c":  #用行運算
            index=0
            for i in range(size):
                for j in range(size-i-1,size):
                    B[index] = A[j][i]  #壓縮成一維陣列B
                    index += 1
            return B    #回傳B用行運算的右下三角形




    #左上三角形
    index=0 #歸0
    for i in range(1,size):
        for j in range(size-1,size-i-1,-1): #抓出右下小三角形
            lu[index] = A[i][j] #壓縮成一維陣列lu
            index += 1
    if lu==D:   #如果右下小三角形全是0
        if Major=="r":  #用列運算
            index=0
            for i in range(size):
                for j in range(0,size-i):
                    B[index] = A[i][j]  #壓縮成一維陣列B
                    index += 1
            return B    #回傳B用列運算的左上三角形
        if Major=="c":  #用行運算
            index=0
            for i in range(size+1):
                for j in range(0,size-i):
                    B[index] = A[j][i]  #壓縮成一維陣列B
                    index += 1
            return B    #回傳B用行運算的左上三角形




    #右上三角形
    index=0
    for i in range(1,size):
        for j in range(i):  #抓出左下小三角形
            ru[index] = A[i][j] #壓縮成一維陣列ru
            index += 1

    if ru==D:   #如果左下小三角形全是0
        if Major=="r":  #用列運算
            index=0
            for i in range(size):
                for j in range(i, size):
                    B[index] = A[i][j]  #壓縮成一維陣列B
                    index += 1
            return B    #回傳B用列運算的右上三角形
        if Major=="c":  #用行運算
            index=0
            for i in range(size):
                for j in range(0,i+1):
                    B[index] = A[j][i]  #壓縮成一維陣列B
                    index += 1
            return B    #回傳B用行運算的右上三角形



    #左下三角形    
    index=0
    for i in range(size-1):
        for j in range(i+1, size):  #抓出右上小三角形
            ld[index] = A[i][j] #壓縮成一維陣列ld
            index += 1
    if ld==D:   #如果右上小三角形全是0
        if Major=="r":  #用列運算
            index = 0
            for i in range(size):
                for j in range(0,i+1):
                    B[index] = A[i][j]  #壓縮成一維陣列B
                    index += 1
            return B    #回傳B用列運算的左下三角形
        if Major=="c":  #用行運算
            index=0
            for i in range(size):
                for j in range(i,size):
                    B[index] = A[j][i]  #壓縮成一維陣列B
                    index+=1
            return B    #回傳B用行運算的左下三角形

   
    #return ans

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix =   [[0,5,2,0],
[0,0,3,1],
[0,0,0,7],
[0,0,0,0]]
    output_array = to_1D_array(input_matrix, "c")
    print(output_array)


#留言板