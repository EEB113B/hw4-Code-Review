from asyncio.windows_events import NULL
from pickle import APPEND


def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str

    right = False
    left = False
    up = False
    down = False

    for x in range(len(Matrix)):
        count = 0
        for y in range(len(Matrix)):
            if Matrix[x][y] == 0:
                count+=1
        if count >= len(Matrix)-1 and x == 0:
            up = True
            break
        if count >= len(Matrix)-1 and x == len(Matrix)-1:
            down = True
            break
    for x in range(len(Matrix)):
        count = 0
        for y in range(len(Matrix)):
            if Matrix[y][x] == 0:
                count+=1
        if count >= len(Matrix)-1 and x == 0:
            left = True
            break
        if count >= len(Matrix)-1 and x == len(Matrix)-1:
            right = True
            break

    output = []
    if Major == "r" :
        if right and up:
            count = 1
            for x in range (len(Matrix)):
                for y in range(count):
                    output.append(Matrix[x][y])
                count+=1
        
        if right and down:
            count = 0
            for x in range (len(Matrix)):
                for y in range(len(Matrix)-count):
                    output.append(Matrix[x][y])
                count+=1
            
        if left and up:
            count = 1
            for x in range (len(Matrix)):
                for y in range(count):
                    output.append(Matrix[x][len(Matrix)-y-1])
                count+=1

        if left and down:
            count = 0
            for x in range (len(Matrix)):
                for y in range(len(Matrix)-count):
                    output.append(Matrix[x][y+count])
                count+=1
        
            
            
    if Major == "c" :

        if right and up:
            count = 0
            for x in range (len(Matrix)):
                for y in range(len(Matrix)-count):
                    output.append(Matrix[y+count][x])
                count+=1
        
        if right and down:
            count = 0
            for x in range (len(Matrix)):
                for y in range(len(Matrix)-count):
                    output.append(Matrix[y][x])
                count+=1
            
        if left and up:
            count = 1
            for x in range (len(Matrix)):
                for y in range(count):
                    output.append(Matrix[len(Matrix)-count+y][x])
                count+=1

        if left and down:
            count = 1
            for x in range (len(Matrix)):
                for y in range(count):
                    output.append(Matrix[y][x])
                count+=1
    

    
    return output # 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix =     [[0,5,2,0],
[0,0,3,1],
[0,0,0,7],
[0,0,0,0]]


    output_array = to_1D_array(input_matrix, "r")
    print(output_array)
   


#留言板