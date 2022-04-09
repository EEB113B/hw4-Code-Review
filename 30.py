def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    rows = len(Matrix)

    def r_leftdown(tlen, matrix):
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

    count = 0
    compress = []

    while True:
        for row in range(rows):
            for column in range(row+1, rows):
                count = Matrix[row][column] + count

        if count == 0:
            if Major == "r":
                compress = r_leftdown(rows, Matrix)
                break
            if Major == "c":
                Matrix = list(map(list, zip(*Matrix)))
                compress = r_rightup(rows, Matrix)
                break
        count = 0
        for row in range(1, rows):
            for column in range(row):
                count = Matrix[row][column] + count

        if count == 0:
            if Major == "r":
                compress = r_rightup(rows, Matrix)
                break

            if Major == "c":
                Matrix = list(map(list, zip(*Matrix)))
                compress = r_rightup(rows, Matrix)
                break

        count = 0
        for row in range(1, rows):
            for column in range(row-1, rows-row-1, -1):
                count = Matrix[row][column] + count

        if count == 0:
            if Major == "r":
                compress = r_leftup(rows, Matrix)
                break

            if Major == "c":
                Matrix = list(map(list, zip(*Matrix)))
                compress = r_leftup(rows, Matrix)
                break

        count = 0
        for row in range(rows-1):
            for column in range(rows-1-row):
                count = Matrix[row][column] + count

        if count == 0:
            if Major == "r":
                compress = compress.r_rightdown(rows, Matrix)
                break

            if Major == "c":
                Matrix = list(map(list, zip(*Matrix)))
                compress = compress.r_rightdown(rows, Matrix)
                break

        if count != 0:
            return "wrong"
            break

    return compress



if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[7,0,0,0],
                    [8,3,0,0],
                    [4,6,5,0],
                    [0,5,6,7]]
    input_matrix = [[1,2,3,4],
                    [5,6,7,0],
                    [8,9,0,0],
                    [0,0,0,0]]

    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板