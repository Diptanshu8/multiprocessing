import time
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def tail(queue):
    fn = queue.get()
    print str(fn)+ "in tail"
    logfile = open("temp.txt","r")
    loglines = follow(logfile)
    for line in loglines:
            print line
