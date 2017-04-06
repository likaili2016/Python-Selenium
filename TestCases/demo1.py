#coding=utf-8
'''题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？'''

con = 0  # 用于计数
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print i*100+j*10+k
                con += 1

print con

