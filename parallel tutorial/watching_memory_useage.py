'''
This bit of the code gets all the processes being run by a
file, and tracks the total memory useage.

Doing this to watch to see if my code explodes with memory,
not acceptable on the server (and has been known to happen).

Created on 2 Nov 2015

@author: chris
'''
import psutil
import os

def main():
    proc = psutil.process_iter()
    
    Mb_b = 1024**2
    
    # not sure which of those is the one I'm interested in,
    # so just break the code and have a look

    mem_rss = 0 
    for p in proc:
        cmds = p.cmdline()        
        for cmd in cmds:
            if "t_auto" in cmd:
                if p.pid != os.getpid():
                    mem_rss += p.memory_info()[0]/Mb_b
    
    
if __name__ == '__main__':
    main()