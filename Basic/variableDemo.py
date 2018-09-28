
if __name__ == "__main__":
    '''
    referencing 
    '''
    v = 110
    print(v)
    '''
    assign multiple values at once
    '''
    tu=('a',1,3)
    (x,y,z) = tu
    print("X:{x},Y:{y},Z:{z}".format(x=x,y=y,z=z))
    '''
    assign consecutive values
    '''
    (MON,TUE,WED,THU,FRI,SAT,SUN)=range(1,8)
    print MON
