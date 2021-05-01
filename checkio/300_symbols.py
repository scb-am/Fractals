# You have to write a function named davasaan (division with all vowels a) which calculates integer division by 10.
# The vowels "eiou" are disallowed as are the slash "/", asterisk "*", and period "." characters.
# 
# We have one more rule for this univocalic challenge. This is a code golf mission and your main goal is to make your code as short as possible: 300 characters is the maximum allowable. The shorter your code, the more remarkable you are.
# Note that your code can start/end with empty lines and commented lines, they are not considered for code length. Hence you can comment a bit your code.
# 
# Input: A non-negative number as an integer.
# 
# Output: The integer division (//10) of the input as an integer.
# 
# How it is used: This is about hacks and tricks in python which help you to shorten your code. You don't need to use this in production, but it can help for deeper comprehension of Python.
# 
# Precondition: 0 ≤ n ≤ 2,000,000,000


# My solution

d=lambda x,y,z:{'':-x,'0':-x,'1':0,'2':x,'3':x+x,'4':x+x+x,'5':x+x+x+x,'6':x+x+x+x+x,'7':x+x+x+x+x+x,'8':x+x+x+x+x+x+x,'9':x+x+x+x+x+x+x+x}[str(y)[-z:-z+1]]+x
davasaan=lambda x:d(1,x,2)+d(10,x,3)+d(100,x,4)+d(1000,x,5)+d(10000,x,6)+d(100000,x,7)+d(1000000,x,8)+d(10000000,x,9)+d(100000000,x,10)


# Other

davasaan = lambda n: [n := n + 5 - n % 10,
                      q := (n >> 1) + (n >> 2),
                      q := q + (q >> 4),
                      q := q + (q >> 8),
                      q := q + (q >> 16),
                      q >> 3][-1]


davasaan=lambda n:(s:=(v:=(a:=(d:=(n>>1)+(n>>2))+(d>>4))+(a>>8))+(v>>16)>>3)+(n-(((s<<2)+s)<<1)>9)

# def davasaan(n):
#     """Approximation of n // 10, which is exact for 0 <= n <= 2000000000."""
#     # Clear version - Not a mathematical proof, but a little explanation.
#     d = (n >> 1) + (n >> 2)    # d = (n // 2) + (n // 4)  # near n*(1/2+1/4)
#     d += d >> 4                # d += d // 16             # near *= 1+1/16
#     d += d >> 8                # d += d // 256            # near *= 1+1/256
#     d += d >> 16               # d += d // 65536          # near *= 1+1/65536
#     d >>= 3                    # d //= 8                  # near *= 1/8
#     # (1/2+1/4)*(1+1/16)*(1+1/256)*(1+1/65536)*1/8 == 0.09999999997671694
#     # With basic maths, we have -1.64215877 < d - n * 0.09999999997671694 <= 0
#     r = (((d << 2) + d) << 1)  # r == (d * 4 + d) * 2 == d * 10
#     return d + (n - r > 9)     # d += 1 if n - r > 9 else 0; return d


davasaan=d=lambda n:[n>9,(a:=n>>4)and a+d(n-(a<<3)-(a<<1))][a>0]
# recursively with the greatest power of n (let's call it a) so that 10*a is less than n
# a=n>>4 = n//16 is that greatest power, so we know that 10a is less than n
# Therefore new_n=n-10a is less than n and if we know that davasaan(n)=a+davassan(new_n)
# 
# It's now time to make this work, so let's define d=davassan (less char usage in recursion)
# new_n=n-10a=n-8a-2a=n-(a<<3)-(a<<1)
# and a is n>>4 (n//16)
# so main recursion element is d(n-(n>>4<<3)-(n>>4<<1))
# Let's now add the corner cases:
# We can do the recursion only if n>=16, so n>>4 and <recursion> ensure n>=16 only as and does not evaluate 2nd element if 1st is False
# Finally is n is less than 16, so 15 or less, we need to return 1 if n>=10 and 0 if n<10
# n>9 is the shortest condition and +(n>9) ensure it's considered as int and not boolean
# I finally used a two element list (n<=16, n>15) with a condition (n>15) to choose as 'or' is not acceptable.
#
# Last trick added (Python 3.8.1): assign n>>4 to p (a:n>>4) to reduce number of chars as it's used 4 times.
# Brackets around a:=n>>4 is mandatory as otherwise it's evaluating the 'and' part before assignment.
#
# Finally and thanks to Phil15 comments, I remove the unnecessary + sign to convert n>9 to int and the parenthesis left around one 'a' occurence



a = vars()['__b'+chr(117)+chr(105)+'lt'+chr(105)+'ns__'][chr(101)+'val']
davasaan = lambda x: a(str(x)+chr(47)+chr(47)+"10")


davasaan=d=lambda x:x and((x>>1)%10>4)|d(x>>1)<<1


m=lambda x:{
'0':        0,
'1':        x,
'2':       x+x,
'3':      x+x+x,
'4':     x+x+x+x,
'5':    x+x+x+x+x,
'6':   x+x+x+x+x+x,
'7':  x+x+x+x+x+x+x,
'8': x+x+x+x+x+x+x+x,
'9':x+x+x+x+x+x+x+x+x
}
f=lambda n,b=1:n!=''and m(b)[n[\
-1]] + f(n[:-1], (b<<3)+ (b<<1))
davasaan=lambda n:f(str(n)[:-1])
