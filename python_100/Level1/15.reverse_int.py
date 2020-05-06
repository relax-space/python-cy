# 15.反转一个整数，例如-123 --> -321
a = -123


def reverse_int(a):
    b = int(str(abs(a))[::-1])
    if a < 0 :
        b = -b 
    
    print(b)
    # return b

reverse_int(a)