from os import major
def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    
    return # 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[7,0,0,0],
                    [8,3,0,0],
                    [4,6,5,0],
                    [0,5,6,7]]
    mayjor = input("r or c")
    size = len(input_matrix)
    B = [None]*((1 + size) * size // 2)
    index = 0
    if major == "r":
        for i in range(size):
            for j in range(size-1, size-i-2, -1):
                B[index] = input_matrix[i][j]
                index += 1

    if major == "c":
        for i in range(size):
            for j in range(size-1, size-i-2, -1):
                B[index] = input_matrix[i][j]
                index += 1   

    finist = []
    for i in B:
        finist.append(i)
    print(finist)

    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板