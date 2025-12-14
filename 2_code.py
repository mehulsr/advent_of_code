data = open("2_input.txt", "r").read().strip().split(",")
# data = open("2_example.txt", "r").read().strip().split(",")

invalid_ids = []
sum = 0

def is_invalid(num:str):
    l = len(num)
    if l == 1:
        return False
    if l%2==1:
        return False

    mid = l//2
    for i in range(mid):
        if num[i] == num[mid+i]:
            continue
        else:
            return False
    return True

factors = {}

def get_factors(num:int):
    # print("hi", num)
    f = []

    for i in range(2, num//2+1):
        # print(i)
        if num%i==0:
            f.append(i)

    return f

def is_invalid_flex(num:str):
    l = len(num)
    if l == 1:
        return False
    
    # print("a")
    
    if num == ''.join(num[0]*l):
        return True
    
    # print(get_factors(l))
    
    if l in factors:
        f = factors[l]
    else:
        f = get_factors(l)
        factors[l] = f        
    if len(f) == 0: # prime number
        return False
    
    for fi in f:
        repeats_for_this_factor = True
        sub = num[:fi]
        for str_i in range(fi, l, fi):
            if num[str_i: str_i+fi] != sub:
                repeats_for_this_factor = False
                break
        if repeats_for_this_factor:            
            return True
    return False


# data = ['1010-1010']

for line in data:
    nums = line.split('-')
    start, end = nums[0], nums[1]

    for num in range(int(start), int(end)+1):
        if num in invalid_ids:
            # don't double count
            continue
        if is_invalid_flex(str(num)):
            sum += num
            invalid_ids.append(num)

print(invalid_ids)

print(sum)


