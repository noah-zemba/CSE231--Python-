n_str = input("\nInput an integer (0 terminates): ")

# Good stuff goes here
n_int = int(n_str)
odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count = 0


while n_int != 0:
    if n_int >= 0:
        positive_int_count +=1
        if n_int % 2 != 0:
            odd_count +=1
            odd_sum += abs(n_int)
        
        else:
            even_count +=1
            even_sum += abs(n_int)
              
    n_int = int(input("\nInput an integer (0 terminates): "))
#Do not change the following lines of code
print("\n")
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)