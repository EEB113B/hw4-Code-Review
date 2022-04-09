
ARRAY_SIZE=4

num=int(ARRAY_SIZE*(1+ARRAY_SIZE)/2)
B=[None]*(num+1)

def getValue(i,j):
    index = int(ARRAY_SIZE*i - i*(i+1)/2 + j)
    return B[index]
input_matrix = [[7,0,0,0],
                [8,3,0,0],
                [4,6,5,0],
                [0,5,6,7]]
output_array = ARRAY_SIZE(input_matrix, "r")
print(output_array)

 


#留言板