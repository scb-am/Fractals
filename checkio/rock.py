d=lambda x,y,z:{'':-x,'0':-x,'1':0,'2':x,'3':x+x,'4':x+x+x,'5':x+x+x+x,'6':x+x+x+x+x,'7':x+x+x+x+x+x,'8':x+x+x+x+x+x+x,'9':x+x+x+x+x+x+x+x}[str(y)[-z:-z+1]]+x
davasaan=lambda x:d(1,x,2)+d(10,x,3)+d(100,x,4)+d(1000,x,5)+d(10000,x,6)+d(100000,x,7)+d(1000000,x,8)+d(10000000,x,9)+d(100000000,x,10)

print(davasaan(1_123_456_789))
print(type(davasaan(1_123_456_789)))


# m=lambda x:{
# '0':        0,
# '1':        x,
# '2':       x+x,
# '3':      x+x+x,
# '4':     x+x+x+x,
# '5':    x+x+x+x+x,
# '6':   x+x+x+x+x+x,
# '7':  x+x+x+x+x+x+x,
# '8': x+x+x+x+x+x+x+x,
# '9':x+x+x+x+x+x+x+x+x
# }
# f=lambda n,b=1:n!=''and m(b)[n[\
# -1]] + f(n[:-1], (b<<3)+ (b<<1))
# davasaan=lambda n:f(str(n)[:-1])




# V=vars()
# S=str(V)
# davasaan=lambda x:V[S[2:14]][S[4506:4512]](x,10)[0]



# davasaan=d=lambda x:x and((x>>1)%10>4)|d(x>>1)<<1