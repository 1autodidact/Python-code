def function(num):
    
    if num == 1 or num ==2:
        return 1
    else:
        result = function(num -1) + function(num -2)
       
        return result
num = int(input('请输入一个数'))
for i in range(1,num + 1):
    a = function(i)
    print(a,end = ' ')
    
