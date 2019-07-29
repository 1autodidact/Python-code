
for i in range(1,10):
    for k in range(1,i + 1):       
        if k != i:
            #判断是否乘到了最后一个数
            result = k * i
            print('{} × {} = {}  '.format(k,i,str(result)),end = '')
            #end = ''表示print输出不换行
        else:
            result = k * i
            print('{} × {} = {}'.format(k,i,str(result)))
            
        
    
        
