count = 0
def hanuoi(n, src, dst, mid):
    global count
    if n == 1:       
        print('{}: {}>{}'.format(1,src, dst))
        #两个塔以上的第一步在这执行
        count += 1
    else:
        hanuoi(n-1 ,src, mid , dst)
        print('{}: {}>{}'.format(n,src,dst ))
        #这是移动的第二步骤
        count += 1
        hanuoi(n-1 ,mid, dst, src)
hanuoi(2,'a','c','b')


