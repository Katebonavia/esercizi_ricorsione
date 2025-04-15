from time import sleep


def countdown(n):
    while n>=0:
        print(n)
        sleep(0.5)
        n-=1

def countdown_recursive(n):
    if n<=0:
        print("Stop")
    else:
        print(n)
        sleep(0.5)
        counter = n-1
        countdown_recursive(counter)

if __name__=="__main__":
    print("Recursive")
    countdown_recursive(10)
    print("Non recursive")
    countdown(10)