import sys

input=sys.stdin.readline
output=sys.stdout.write
def reverseanumber(num) -> int:
    m=num
    rev=0
    while num!=0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    return rev


#Using slicing and string we can reverse a number in one line

def reverse_a_number_using_slicing(num):
    string_number_reverse=str(num)[::-1]
    return string_number_reverse

num=int(input())
output(str(reverseanumber(num))+"\n")
output(reverse_a_number_using_slicing(num))
