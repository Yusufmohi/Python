try:
    a=int(input())
    b=int(input())
    print(a+b)
except ValueError as e:
    print("Something",e)
except Exception as e:
    print("Try Again",e)
finally:
    print("Done")
