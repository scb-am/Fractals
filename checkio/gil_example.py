# current file show main difference in time between python2 and 3, single process and several


from threading import Thread
import time

def count(n):
    while n > 0:
        n -= 1

COUNT = 50000000


# t1 = Thread(target=count, args=(COUNT//2,))
# t2 = Thread(target=count, args=(COUNT//2,))

start = time.time()

# t1.start(); t2.start()
# t1.join(); t2.join()

count(COUNT)

end = time.time()
print(end - start)