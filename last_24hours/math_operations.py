"""
def basic_operations(a, b):
    results={"Addition":a+b,"Subtraction":a-b,"Multiplication":a*b,"Divisiom":a/b if b != 0 else "Can not divide"}
    return results
    results=basic_operations(a,b)
    print(results)
"""
"""
def power_operation(base, exponent, **kwargs):
    result = base ** exponent
    
    
    if 'modulo' in kwargs:
        modulo_value = kwargs['modulo']
        result %= modulo_value
    
    return result
result= power_operation(2, 2)
print(result) 
"""



def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def power(base, exponent):
    try:
        result = base ** exponent
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

def apply_operations(operation_list):
    results = []
    for operation, args in operation_list:
        result = operation(*args)
        results.append(result)
    return results

operations = [
    (divide, (10, 2)),
    (divide, (9, 0)),  # Division by zero error
    (power, (2, 3)),
    (power, ('a', 2)),  # Invalid input error
]

results = apply_operations(operations)
print(results)
     



Updated at: 2023-12-12 22:06:33.717053