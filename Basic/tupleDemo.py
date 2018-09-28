def calculate(nums):
    if nums is None:
        raise ValueError('nums must be provied.')
    if not isinstance(nums, (tuple,list)):
        raise ValueError('nums is invalid, must be tuple or list')
    print('Type: {type}, Values: {va}'
        .format(type=type(nums),
                va = {num: num * num for num in nums if num%2==1}))

def tSort(nums):
    if nums is None:
        raise ValueError('nums must be provied.')
    if not isinstance(nums, (tuple,list)):
        raise ValueError('nums is invalid, must be tuple or list')
    nums.sort(key=str.lower, reverse=True)
    print nums

if __name__ == "__main__":
    calculate((1,2,3,4,5,6,7,8,9))
    calculate([1,2,3,4,5,6,7,8,9])
    lst=['t','s','a','x','b','c']
    tSort(lst)
    lst_1 = ['t', 's', 'a', 'x', 'b', 'c']
    lst_2=sorted(lst_1,key=str.lower,reverse=True)
    print(lst_1)
    print(lst_2)
    lst_3 = [1,2,3]
    lst_3.append([4,5,6])
    print len(lst_3)
    lst_3.extend(['s','d'])
    print(len(lst_3))
    print(lst_3)