def ha(n,src,dst,mid):
    if n == 1:
        print('{} {}-{}'.format(1,src,dst))
    else:
        ha(n-1,src,mid,dst)
        print('{} {}-{}'.format(n,src,dst))
ha(2,'a','b','c')

