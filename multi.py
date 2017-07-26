from multiprocessing import Process,Lock,freeze_support,Queue
import tempfile
import time
import tail
#from cStringIO import StringIO

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.read()
        if not line:
            time.sleep(0.1)
            continue
        print line

def tail(queue):
    fn = queue.get()
    print str(fn)+ "in tail"
    logfile = open("temp.txt","r",0)
    loglines = follow(logfile)

def run(queue):
    fn = queue.get()
    print str(fn)+ "in run"
    for i in xrange(10):
        with open(fn,'a')as fd:
            fd.write(str(i))
            fd.flush()
        

if __name__ == "__main__":
    #freeze_support()
    queue = Queue()
    fn = "temp.txt"

    queue.put(fn)
    queue.put(fn)
    print "file just put"
    q = Process(target = tail, args = (queue,))
    q.start()
    run(queue)
    print "hellp"
    
