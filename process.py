def func(name, queue):
    print("Start {0}".format(name))
    while True:
        print("{0}: {1}".format(name, queue.get()))
