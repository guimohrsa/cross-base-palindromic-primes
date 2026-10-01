import math

def is_prime(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    
    for a in bases:
        if n <= a:
            break
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
            
    return True

def generate_palindromics(limit):
    for i in range(1, 10):
        if i <= limit: yield i
    
    length = 2
    while True:
        half_len = (length + 1) // 2
        start = 10**(half_len - 1)
        end = 10**half_len
        
        for prefix in range(start, end):
            s = str(prefix)
            if length % 2 == 0:
                pal_str = s + s[::-1]
            else:
                pal_str = s + s[-2::-1]
            
            pal = int(pal_str)
            if pal > limit:
                return
            yield pal
        length += 1


limit = 10**10

f = 0
for i in generate_palindromics(limit):

    if not is_prime(i):
        continue
        

    bin_str = f"{i:b}"
    if bin_str != bin_str[::-1]:
        continue
        

    if bin_str.count('1') % 3 == 0:
        continue
        
  
    i_B = int(bin_str)
    if is_prime(i_B):
        print(f"DEC: {i} | BIN: {bin_str} | BIN_DEC: {i_B}")
        f += 1