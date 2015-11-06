'''
Want to do memory monitoring of the test cases, in case the 
memory jumps start happening again. Requires communicating 
between processes, and I'd like to be able to do this properly.

Created on 2 Nov 2015

@author: chris
'''
import time
import multiprocessing as mp

def main():
    
    # process to wait for exit command from parent node (have it
    # count each second).
    
    def child_function(q):
        
        # waits for 10s for the termination by the main process,
        # checking each second. 
        
        i = 0
        for i in range(10):
            time.sleep(1)
            print i
            
            # Catch terminate communication, stop
            
            if not q.empty():
                print "broken by main process"
                break
        else:
            print "hit loop limiter"
    
    
    # Spawn processes, with a pipe
    
    q = mp.Queue()
    p = mp.Process(target=child_function,args=(q,))
    p.start()
    
    
    # Wait for 3 seconds
    
    time.sleep(3)
    
    
    # Send terminate communication
    
    q.put(1)
    

if __name__ == '__main__':
    main()