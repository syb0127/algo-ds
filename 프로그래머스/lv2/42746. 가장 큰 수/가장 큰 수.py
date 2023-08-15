def solution(numbers):
    #First, cast all items in numbers as "string" datatype by using the map function. Then turn it into a list for easy sorting.
    numbers = list(map(str, numbers))
    #In order to achieve our goal, we want numbers with big integers in the first digit to come first. Use sort method with "reverse" set to "True". 
    #However, be careful with how you sort. For example, if we have 3, 30, 39, the biggest number we can make with these would be 39330. But if I sort with no precaution, it will return 39303, which is wrong. To resolve this, I used the "lambda" keyword to repeat each item three times. In Python, "a" * 3 will return "aaa". As a result, I will end up with 333, 303030, 393939. When comparing strings in Python, "333" is smaller than "303030". Remember that lamda function does not mutate the original list and I don't need to worry about multiplied strings messing up the final result. 
    numbers.sort(key = lambda x : x*3, reverse = True)
        #As I'm joining, I cast each item as an integer to pass the edge case of ['0','0'] returning "00" as the answer.
    return str(int(''.join(numbers)))
