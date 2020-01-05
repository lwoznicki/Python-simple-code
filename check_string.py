inputStr=input()
is_alphanumeric = False
is_alphabets = False
is_digit = False
is_lower_case = False
is_upper_case = False
for i in inputStr:
    if(i.isalnum()):
        is_alphanumeric=True
    if(i.isalpha()):
        is_alphabets=True
    if(i.isdigit()):
        is_digit=True
    if(i.islower()):
        is_lower_case=True
    if(i.isupper()):
        is_upper_case=True

print()  
print('Text: ' + str(inputStr))	
print()
print('Alnum: ' + str(is_alphanumeric))
print('Alphabets: ' + str(is_alphabets))
print('Digit: ' + str(is_digit))
print('Lowercase: ' + str(is_lower_case))
print('Uppercase: ' + str(is_upper_case))