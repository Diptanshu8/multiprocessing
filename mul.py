import multiprocessing


def reader(q):
    while True:
        print "from reader : %s" % q.get(block=True)


def writer(q, s):
    print "putting %s" % s
    q.put(s)

q = multiprocessing.Queue()
p1=multiprocessing.Process(target=reader, args=[q])
p2=multiprocessing.Process(target=writer, args=[q,'sumit'])
p1.start()
p2.start()

[multiprocessing.Process(target=writer, args=[q,i]).start() for i in range(10)]

[multiprocessing.Process(target=writer, args=[q,'qwertyuiopasdfghjklzxcvbnm'[:i]]).start() for i in range(26)]


# Every process using reader as target will be blocked for ever waiting for reading from queue.
# We can pass an ending value in the queue, or may be use a separate variable to tell it to stop
# waiting and just return.
