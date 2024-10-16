
a = 5
b = 2

try:
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print('in finally')
    
