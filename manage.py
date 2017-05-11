from multiprocessing import Process, Pipe
import tcp_recv
import process
import time

def main():
    parent_conn, child_conn = Pipe()
    parent_conn, child_conn = Pipe()
    p1 = Process(target=process.func, args=(child_conn,))
    p2 = Process(target=process.func, args=(child_conn,))

    p1.start()
    p2.start()
    parent_conn.send([20, None, 'hello'])
    parent_conn.close
    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
