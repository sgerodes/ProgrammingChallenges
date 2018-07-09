def solution(digits):
    largest_digit=0
    largest_digit_indices=[]
    for i,digit in enumerate(digits[:-4]):
        int_digit=int(digit)
        if int_digit==largest_digit:
            largest_digit_indices.append(i)
        if int_digit>largest_digit:
            largest_digit=int_digit
            largest_digit_indices=[i]
    largest_number=0
    for i in largest_digit_indices:
        num=int(digits[i:i+5])
        if num>largest_number:
            largest_number=num
    return largest_number;