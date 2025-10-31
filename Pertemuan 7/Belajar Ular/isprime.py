num = 0
limit = 500
while num <= limit :
    if num == 0 or num == 1:
        pass
    elif num > 1 :
        bil = 2
        is_prime = True
        while bil <= (num // 2) :
            if num % bil == 0 :
                is_prime = False
                break
            bil += 1
        if is_prime :
            print(num)

    num += 1