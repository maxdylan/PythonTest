arr = [1000000,600000,400000,200000,100000,0]
rate = [0.01,0.015,0.03,0.05,0.075,0.1]
p = 0
inp = int(input("净利润: "))
for i in range(0,6):
    if inp>arr[i]:
        p+=arr[i]*rate[i]
print("总收入: %d"%(p))
