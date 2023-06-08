import numpy as np
import scipy

A=np.array([[2,1,-2,3],[3,2,-1,2],[1,1,1,-1]]) #创建矩阵A
m=A.shape[0] #行数
n=A.shape[1] #列数
rank_A=np.linalg.matrix_rank(A) #求解A的秩，rank(A)
print(f"rank_A={rank_A},n={n}")
if rank_A==n: #判断解的情况
    print("rank(A)=n，方程只有零解")
    x = np.zeros(m)
    print(f"x={x}")
else:
    print("rank(A)<n，方程有非零解")
    x=scipy.linalg.null_space(A) #求解A的化零矩阵x，特解
    #x=x[:,1][:,np.newaxis] #取其中的任意一列即为方程的一个特解
    print(f"x={x}")
result=A@x #验证解的正确性
print(f"Ax={result}")

