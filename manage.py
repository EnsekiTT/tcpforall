from multiprocessing import Process, Pipe, Queue
import tcp_recv
import process
import time
import threading

def main():
    queue1 = Queue()
    queue2 = Queue()
    queues = [queue1, queue2]
    thread = threading.Thread(target=tcp_recv.OpenRecv, args=(queues,))
    p1 = Process(target=process.func, args=(queue1,))
    p2 = Process(target=process.func, args=(queue2,))

    thread.start()
    p1.start()
    p2.start()
    input("waiting>")
    thread.join()
    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
