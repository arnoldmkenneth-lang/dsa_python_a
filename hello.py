try:
    def hello():
        print("Welcome to the division calculator")
    hello()
    numerator=int(input("Enter your numerator number: "))
    denominator=int(input("Enter your denominator number: "))
    result=numerator/denominator
    
except ZeroDivisionError as e:
    print("You cannot divide by zero")
except ValueError as e:
    print("You must enter a number")
except Exception as e:
    print("An error occurred")
else:
    print(f"The result to your answer is:{round(result,2)}")
finally:
    print("This is the end of the program")
    