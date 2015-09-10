'''
The code I'm writing for this has, in effect, a list that must be
applied to a function one-by-one. Simple paralellisation

Will this increase the frequency of bugs?


Created on 10 Sep 2015

@author: chris
'''
import multiprocessing as mp

def cube(x):
    return x**3


def main():
    
    # ordered
    
    pool = mp.Pool(processes=3) # real case has 3 calls to the function
    results = [pool.apply(cube,args=(x,)) for x in range(1,7)]
    
    print(results)
    
    
    # ordered version 2
    
    pool = mp.Pool(processes=3)
    results = pool.map(cube, range(1,7))
    
    print(results)
    
    
    # unordered version - order doesn't strictly matter for my case 
    #                     equivalently, neither does freeing up the head
    #                     node, but while I'm here
    
    pool = mp.Pool(processes=4)
    results = [pool.apply_async(cube, args=(x,)) for x in range(1,7)]
    output = [p.get() for p in results]
    
    print(output)
    
    # okay, that's all straight forwards so far

if __name__ == '__main__':
    main()