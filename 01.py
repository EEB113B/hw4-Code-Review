from numpy import tri


def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    Size = len(Matrix)#計算矩陣size

    #以四邊0的數量判斷為何種三角矩陣
    top_zero_num = Matrix[0].count(0)#第一列0的數量
    botton_zero_num = Matrix[Size-1].count(0)#最後一列0的數量
    left_zero_num = 0
    right_zero_num = 0
    for i in range(Size):
        if Matrix[i][0]==0:
            left_zero_num += 1#第一行0的數量
        if Matrix[i][Size-1]==0:
            right_zero_num += 1#最後一行0的數量
    #第一列和第一行最多0，則為右下三角矩陣
    if top_zero_num >= Size-1 and left_zero_num >= Size-1:
        tri_detection = 'right_lower_Matrix'
    #第一列和最後一行最多0，則為左下三角矩陣
    if top_zero_num >= Size-1 and right_zero_num >= Size-1:
        tri_detection = 'left_lower_Matrix'
    #最後一列和第一行最多0，則為右上三角矩陣
    if botton_zero_num >= Size-1 and left_zero_num >= Size-1:
        tri_detection = 'right_upper_Matrix'
    #最後一列和最後一行最多0，則為左上三角矩陣
    if botton_zero_num >= Size-1 and right_zero_num >= Size-1:
        tri_detection = 'left_upper_Matrix'

    index = 0
    B = [None]*((1+Size)*Size//2)#創建新矩陣，存放壓縮後的值
    #水平壓縮進入此迴圈
    if Major == 'r':
        if tri_detection == 'right_lower_Matrix':#右下三角進行水平壓縮
            for i in range(Size):
                for j in range((-i+Size-1), Size):
                    B[index] = Matrix[i][j]
                    index+=1
        if tri_detection == 'left_lower_Matrix':#左下三角進行水平壓縮
            for i in range(Size):
                for j in range(0, i+1):
                    B[index] = Matrix[i][j]
                    index+=1
        if tri_detection == 'right_upper_Matrix':#右上三角進行水平壓縮
            for i in range(Size):
                for j in range(i,Size):
                    B[index] = Matrix[i][j]
                    index+=1
        if tri_detection == 'left_upper_Matrix':#左上三角進行水平壓縮
            for i in range(Size):
                for j in range(0,Size-i):
                    B[index] = Matrix[i][j]
                    index+=1
    #垂直壓縮進入此迴圈
    if Major == 'c':
        if tri_detection == 'right_lower_Matrix':#右下三角進行垂直壓縮
            for j in range(Size):
                for i in range(-j+Size-1,Size):
                    B[index] = Matrix[i][j]
                    index+=1
        if tri_detection == 'left_lower_Matrix':#左下三角進行垂直壓縮
            for j in range(Size):
                for i in range(j, Size):
                    B[index] = Matrix[i][j]
                    index+=1
        if tri_detection == 'right_upper_Matrix':#右上三角進行垂直壓縮
            for j in range(Size):
                for i in range(0,j+1):
                    B[index] = Matrix[i][j]
                    index+=1
        if tri_detection == 'left_upper_Matrix':#左上三角進行垂直壓縮
            for j in range(Size):
                for i in range(0,Size-j):
                    B[index] = Matrix[i][j]
                    index+=1
    #回傳壓縮後的矩陣
    return B

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