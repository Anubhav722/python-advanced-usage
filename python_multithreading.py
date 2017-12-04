####### Multithreading Explained

# Threads can be thought of as separate programs running alongside each other.
# However they run within one process, meaning they can share data between one another easier than actual separate programs.

# The challenge of threads is that they can be hard to manage. Especially when a piece of data is being used by more than on thread.
# Threads can be used just for quick tasks like calculating a result from an algorithm or for running slow processes in the background while the program continues.

####### Asynchronous tasks

# Some tasks can take a long time. Input and Output for example can take a long time.
# Some programs are required to be real time. So we can setup threads to run in the background to write a file or search for items while the user can still interact with the interface or command line.

# That's where custom threads come into picture


from threading import Thread
import time

def timer(name, delay, repeat):
    print("Timer: "+ name+ " Started")

    while repeat >0:
        time.sleep(delay)
        print(name + ":"+ str(time.ctime(time.time()) ) )
        repeat -= 1

    print("Timer: "+name+" is completed")


def Main():
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 2, 5))
    t1.start()
    t2.start()

    print("Main completed")

if __name__ == '__main__':
    Main()
