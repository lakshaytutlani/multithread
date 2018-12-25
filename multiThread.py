import threading

def print_sq(a):
    print a*a
    
def print_cube(a):
    print a*a*a
    
if __name__ == "__main__":
    p1 = threading.Thread(target=print_sq, args=(10,))
    p2 = threading.Thread(target=print_cube, args=(10,))
    
    p1.start()
    p2.start()
    
    
    p1.join()
    p2.join()
    
    print "Done"
    
    
