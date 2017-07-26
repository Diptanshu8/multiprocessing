from multiprocessing import Process,Lock,freeze_support,Queue
import tempfile
import time
import tail
#from cStringIO import StringIO

def run(queue):
    time.sleep(3)
    fn = queue.get()
    print str(fn)+ "in run"
    for i in xrange(10):
        with open(fn,'a')as fd:
            fd.write(str(i))
        

if __name__ == "__main__":
    #freeze_support()
    queue = Queue()
    fn = "temp.txt"

    queue.put(fn)
    print "file just put"
    q = Process(target = tail.tail, args = (queue,))
    q.start()
    #p = Process(target = run,args = (queue,))
    #p.start()
    run(queue)
    print "hellp"
    
