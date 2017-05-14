import time

def func(queue):
    print("StartProcess")
    while True:
        print(queue.get())
