import numpy as np

a =np.array([1,3,4,5])
a = np.reshape(a,(2,-1))
print(a)
print(a.shape)


# 開啟檔案
fp = open("zero.txt", "a")

for i in range(600):
    fp.write("4 ")

# 關閉檔案
fp.close()