def is_palindrome(num):

    '''
    Question 4: Largest palindrome product
    
    three_digits = [x for x in range(100, 1000)]
    possible_solutions = [x for x in range(10000, 999000) if is_palindrome(x)]
    answers = [x*y for x in nums for y in nums if x*y in answers]
    final_answer = max(answers)
    '''

    num = str(num)
    if num[:1] == num [-1:]:
        if len(num) in [2,3]:
            return True
        return is_palindrome(num[1:-1])
    else:
        return False
