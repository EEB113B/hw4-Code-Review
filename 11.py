#from os import major

def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)
    #print(size)
    #看每行(列)的0 遞增還是遞減 預設它是上左三角(上面那行0都比下面那行少，左邊那列0都比右變那列少)
    uptri = ltri = True
    x=0 #抓出要比較的兩行
    for k in range(size-1):#$總共要比size-1次
        countUP=countDN=countL=countR=0
        for j in range(size):#數前一行、列出現0的次數
            if(Matrix[x][j]==0):#行
                countUP+=1
            if(Matrix[j][x]==0):#列
                countL+=1
        x+=1
        for j in range(size):#數後一行、列出現0的次數
            if(Matrix[x][j]==0):#行
                countDN+=1
            if(Matrix[j][x]==0):#列
                countR+=1
        if(countUP > countDN):#如果上面那行0比下面的多-->下三角
            uptri = False
        if(countL >countR):#如果左邊那列0比右邊那列多-->右三角
            ltri = False
    #print('uptri :',uptri)
    #print('ltri: ',ltri)

    output=[None] * ((1 + size) * size // 2)
    if(Major=='r'):
        if(uptri==True and ltri==True):#上左三角R
            index = 0
            for i in range(size):
                for j in range(0,size-i):
                    output[index] = Matrix[i][j]
                    index += 1
        if(uptri==True and ltri==False):#上右三角R
            index = 0
            for i in range(size):
                for j in range(i, size):
                    output[index] = Matrix[i][j]
                    index += 1
        if(uptri==False and ltri==True):#下左三角R
            index=0
            for i in range(size):
                for j in range(0,i+1) :
                    output[index] = Matrix[i][j]
                    index += 1
        if(uptri==False and ltri==False):#下右三角R
            index = 0
            for i in range(size):
                for j in range(size-i-1,size):
                    output[index] = Matrix[i][j]
                    index += 1
    if(Major=='c'):
        if(uptri==True and ltri==True):#上左三角C
            index = 0
            for i in range(size):
                for j in range(0,size-i):
                    output[index] = Matrix[j][i]
                    index += 1
        if(uptri==True and ltri==False):#上右三角C
            index=0
            for i in range(size):
                for j in range(0,i+1) :
                    output[index] = Matrix[j][i]
                    index += 1
        if(uptri==False and ltri==True):#下左三角C
            index = 0
            for i in range(size):
                for j in range(i, size):
                    output[index] = Matrix[j][i]
                    index += 1
        if(uptri==False and ltri==False):#下右三角C
            index = 0
            for i in range(size):
                for j in range(size-i-1,size):
                    output[index] = Matrix[j][i]
                    index += 1

    return output # 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[7,0,0,0],
                    [8,3,0,0],
                    [4,6,5,0],
                    [0,5,6,7]]

    output_array = to_1D_array(input_matrix, "c")
    print(output_array)


#留言板