def is_armstrong(number: int) -> bool:
    numb = [int(i) for i in (str(number))]
    degree = len(str(number))
    numb_armstrong = sum([i**degree for i in numb])
    if numb_armstrong == number:
        return True
    else: return False

assert is_armstrong(153) == True, 'Is Armstrong number'
assert is_armstrong(10) == False, 'Is not Armstrong number'