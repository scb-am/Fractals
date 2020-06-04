# def count_consecutive_summers(num):
#     list = [x for x in range(1, num + 1)]
#     return [True if sum(list[x-1:y]) == num else False for x in list for y in list[x-1:]].count(True)

def count_consecutive_summers(num):
    list = [x for x in range(1, num + 1)]
    answer = 0
    for i in list:
        sum = 0
        for j in list[i-1:]:
            sum += list[j-1]
            if sum > num:
                break
            elif sum == num:
                answer += 1
    return answer

"""Very fast"""
# def count_consecutive_summers(num):
#     count = 1 + (num%2)*(not not num//2)
#     for i in range(3,1+num//2,2):
#         if not num%i:
#             count += 1
#     return count

"""More faster"""
# def count_consecutive_summers(num):
#     count = 0
#     for n in range(0, num):
#         denominator = num - n * (n + 1) // 2
#         if denominator <= 0:
#             break
#         if denominator % (n + 1) == 0:
#             count += 1
#     return count

"""Coolest"""
# def count_consecutive_summers(num):
#     # your code here
#     #number of ways to express as sum of consecutive positive integers is equal to the number of odd factors that number has
#     odd_factors = []
#     x = 1
#     while x <= num:
#         print(x, num % x, x % 2)
#         if num % x ==0 and x % 2:
#             odd_factors.append(x)
#         x += 1
#     return len(odd_factors)

# count_consecutive_summers = lambda n: sum(not n%k for k in range(1, n+1, 2))

print(count_consecutive_summers(2835))# == 20
