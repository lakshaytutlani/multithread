import multiprocessing


def withdraw(balance, lock):     
    for _ in range(10000): 
        lock.acquire() 
        balance.value = balance.value - 5
        lock.release() 
  
# function to deposit to account 
def deposit(balance, lock):     
    for _ in range(10000): 
        lock.acquire() 
        balance.value = balance.value + 5
        lock.release() 
  


def perform_trans():
    data = multiprocessing.Value('i',100)
    lock = multiprocessing.Lock()
    
    p1 = multiprocessing.Process(target=withdraw, args=(data,lock))
    p2 = multiprocessing.Process(target=deposit, args=(data,lock))
    
    p1.start()
    p2.start()
    
    
    p1.join()
    p2.join()
    
    print("Final balance = {}".format(data.value)) 
    
    print "Done"

if __name__ == "__main__": 
    perform_trans()