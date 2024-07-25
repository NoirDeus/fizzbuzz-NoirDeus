#Create initial list of integers
List = list(range(100))            
#Iterate the values in List to replace values that are divisable by "3" with "Fizz", "5" with "Buzz", and both "3 and 5" with "FizzBuzz"
for x in List:
    if List[x]%3 == 0 and List[x]%5 == 0:
        List[x] = "FizzBuzz"
    elif List[x]%3 == 0:
        List[x] = "Fizz"
    elif List[x]%5 == 0:
        List[x] = "Buzz"
#print the updated list
print(List)




