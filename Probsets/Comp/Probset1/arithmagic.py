 
def arithmagic():
    
    step_1 = input("Enter a 3-digit number where the first and last "
                                           "digits differ by 2 or more: ")
    if int(step_1) < 100 or int(step_1) > 999:
        raise ValueError("not a 3-digit number")
        
    if abs(int(step_1[0]) - int(step_1[-1])) < 2:
        raise ValueError("first and last digits must differ by 2 or more")
    step_2 = input("Enter the reverse of the first number, obtained "
                                              "by reading it backwards: ")
                                              
    reverse = ''
    for i in step_1:
        reverse = ''.join((i, reverse))
    print(reverse)
    if step_2 != reverse:
        raise ValueError("not the reverse of the first number")
    
    step_3 = input("Enter the positive difference of these numbers: ")
    
    diff = abs(int(step_1) - int(step_2))
    if int(step_3) != diff:
        raise ValueError("not the positive difference")
    
    step_4 = input("Enter the reverse of the previous result: ")
    
    reverse_diff = ''
    for i in str(diff):
        reverse_diff = ''.join((i, reverse_diff))
    if step_4 != reverse_diff:
        raise ValueError("not the reverse of the previous number")
    
    print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")
    
arithmagic()