def fizzbuzz(a,b):

    sum = len(a) + len(b)

    if sum %3 and sum %5 == 0:
        return 'fizzbuzz'

    elif sum%5 == 0:
        return 'buzz'

    elif sum%3 == 0:
        return 'fizz'
    
    else:
        return'none'

print (fizzbuzz([4,6],[2,3]))











