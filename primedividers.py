def factors(x):
    a = []
    n = x 
    i = 2
    while (i * i) <= n:
        while (n % i) == 0:
            a.append(i)
            n //= i            
        i += 1
    if (n > 1) and (n != x):
        a.append(n)
    return a

print('Enter natural number more than 1 : ')
n = int(input()) # 600851475143
if n > 1: 
    f = factors(n)
    if len(f) == 0:
        print(f'{n} is prime')
    else:
        print(f'{n} is divided by (prime) dividers {sorted(set(f))}')
else:
    print('Number must be Natural and more thaan 1!')
