#codewars_test1.py
#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if (number%2) ==0:
        return"Even"
    else:
        return"Odd"
    

def even_or_odd2(number):
    if (number%2) ==0:
        return"Even"
    return"Odd"
    
print(even_or_odd(2));
print(even_or_odd(3));
print(even_or_odd2(2));
print(even_or_odd2(3));

#print(even_or_odd2("3"));
print(even_or_odd2('3'));

    
#import codewars_test as test
#from solution import even_or_odd

#@test.describe("Fixed Tests")
#def fixed_tests():
    #@test.it('Basic Test Cases')
    #def basic_test_cases():test.assert_equals(even_or_odd(2), "Even")
        #test.assert_equals(even_or_odd(1), "Odd")
        #test.assert_equals(even_or_odd(0), "Even")
        #test.assert_equals(even_or_odd(1545452), "Even")
        #test.assert_equals(even_or_odd(7), "Odd")
        #test.assert_equals(even_or_odd(78), "Even")
        #test.assert_equals(even_or_odd(17), "Odd")
        #test.assert_equals(even_or_odd(74156741), "Odd")
        #test.assert_equals(even_or_odd(100000), "Even")
        #test.assert_equals(even_or_odd(-123), "Odd")
        #test.assert_equals(even_or_odd(-456), "Even")