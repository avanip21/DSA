#1.print hello world
'''def hello():
    print("Helloo world!!")
hello()'''

#2.print name
'''def greet(name):
    print("Hello",name)
name=(input("Enter ur name:"))
greet(name)'''

#3.add two number
'''def add(a,b):
    return a+b
a=int(input("Enter first num:"))
b=int(input("Enter second num:"))
print("Sum",(a+b))'''

#4.find square
'''def eo(num):
        if num%2==0:
            print("Even num")
        else:
            print("Odd num")
num=int(input("Enter a num:"))
eo(num)'''

#5.even or odd
'''def sq(num):
    return num*num
a=int(input("Enter a number:"))
print("Square is:",sq(a))'''

#6.find max of two num
'''def maximum(a,b):
    if a>b:
        return a
    else:
        return b
a=int(input("Enter first num:"))
b=int(input("Enter sencond num:"))
print("Maximum num is :",maximum(a,b))'''

#7.celsius to fahrenhit
'''def celsius(num):
    return(num*9/5)+32
num=float(input("Enter celsius:"))
print("fahrenheit=",num)'''

#8.area of circle
'''def area(radius):
    return 3.14*radius*radius
radius=float(input("Enter radius:"))
print("Area of circle=",area(radius))'''

#9.factorial of number
'''def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
num=int(input("Enter number:"))
print("Facctorial:",factorial(num))'''

#10.number is positive,negative or zero
'''def number(num):
    if num>0:
        print("Positive")
    elif num<0:
        print("Nagetive")
    else :
        print("Num is zero")
num=int(input("Enter a num:"))
number(num)'''

#11.max of three num
'''def maximum(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

print("Maximum:",maximum(a,b,c))'''

#12.vowel in string
'''def count_vowel(text):
    count=0
    for ch in text:
        if ch in "aeiouAEIOU":
            count=count+1
    return count
text=(input("Enter string:"))
print("Number of volwel:",count_vowel(text))'''

#13.reverse string
'''def reverse_string(text):
    return text[::-1]
text=(input("Enter string:"))
print("Reverse:",reverse_string(text))'''

#14.string is palidrome
'''def palidrome(text):
    if text==text[::-1]:
        return True
    else:
        return False
text=(input("Enter string:"))
if palidrome(text):
    print("Palidrome")
else:
    print("Not palidrome")'''

#15.sum of all element in a list
'''def list_sum(numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total

numbers = [10, 20, 30, 40,50]

print("Sum:", list_sum(numbers))'''

#16.largest element in a list
'''def largest(numbers):
    big = numbers[0]

    for num in numbers:
        if num > big:
            big = num

    return big

numbers = [10, 25, 15, 40, 20]

print("Largest:", largest(numbers))'''

#17.remove duplicate value from the list
'''def remove_duplicates(numbers):
    new_list = []

    for num in numbers:
        if num not in new_list:
            new_list.append(num)

    return new_list

numbers = [10, 20, 10, 30, 20, 40]

print("Original List:", numbers)
print("Without duplicates:", remove_duplicates(numbers))'''

#18.how many times an element appears in a list
'''def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count = count + 1

    return count

numbers = [10, 20, 10, 30, 10, 40]

element = int(input("Enter element: "))

print("Count:", count_element(numbers, element))'''

#19.check number is prime or not
'''def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")'''

#20.all prime numbers between two numbers
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def prime_numbers(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

prime_numbers(start, end)

#21.fibonacci numbers
'''def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        a, b = b, a + b

n = int(input("Enter number of terms: "))

fibonacci(n)'''

#22.second largest number in list
'''def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

numbers = [10, 30, 20, 50, 40]

print("Second largest:", second_largest(numbers))'''

#23.sort list without using sort()
'''def sort_list(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers

numbers = [40, 10, 30, 20, 50]

print("Sorted List:", sort_list(numbers))'''

#24.Merge two lists and remove duplicates
'''def merge_lists(list1, list2):
    result = []

    for num in list1:
        if num not in result:
            result.append(num)

    for num in list2:
        if num not in result:
            result.append(num)

    return result'''


list1 = [10, 20, 30]
list2 = [20, 30, 40, 50]

print("Merged List:", merge_lists(list1, list2))

    
        










