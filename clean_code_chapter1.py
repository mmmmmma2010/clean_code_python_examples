#### Non-cleancode example  
# no descriptive function names
# no descriptive variable names
# no docstrings  
def calc(a,b):
   if a>b:
       return a-b
   elif a<b:
       return a+b
   else:
       return a*b



#### make code more clean and readable
# add docstrings
# write descriptive function names
# write descriptive variable names
def calculate_value_based_on_condition(num1,num2):
    """
    calculate different values based on comparion of two numbers
    if first number is grater than second number return difference
    if first number is less than second number return sum
    if bothnumbers ar equal return product
    """
    
    if num1>num2:
        return num1-num2
    elif num1<num2:
        return num1+num2
    else:
        return num1*num2    

 
print(calc(1,2))
print(calculate_value_based_on_condition(1,2))
