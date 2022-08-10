import datetime, time
class MyTimer():
    def __init__(self) -> None:
        self.starttime = datetime.datetime.now()
        self.stoptime=self.starttime
        self.laptime=datetime.datetime.now() - self.starttime
        self.elapsetime = self.stoptime - self.starttime
    
    def start(self):
        self.starttime = datetime.datetime.now()
        print("Timer Started at ",self.starttime)

    def lap(self):
        self.laptime=datetime.datetime.now() - self.starttime
        print("Timer lapping at ",self.laptime)
        return "Timer lapping at "+str(self.laptime)

    def stop(self):
        self.stoptime = datetime.datetime.now()
        self.elapsetime = self.stoptime-self.starttime
        print("Timer stopped at ",self.stoptime)
        print("Elapsed time is ",self.elapsetime)

timer=MyTimer()
def diamond(name="Capsule Labs"):
    rows = int(len(name)/2)
    print(f"Length of input name \' {name} \'is {len(name)} \nMidpoint length is {rows}")

    # It is used to print the space  
    k = 2 * rows - 2  
    # Outer loop to print number of rows  
    for i in range(0, rows):  
        # Inner loop is used to print number of space  
        for j in range(0, k):  
            print(end=" ")  
        # Decrement in k after each iteration  
        k = k - 1  
        # This inner loop is used to print stars  
        for j in range(0, i):  
            print("* ", end="")  
        print("")  
    
    # Downward triangle Pyramid  
    # It is used to print the space  
    k = rows - 2  
    # Output for downward triangle pyramid  
    for i in range(rows, -1, -1):  
        # inner loop will print the spaces  
        for j in range(k, 0, -1):  
            print(end=" ")  
        # Increment in k after each iteration  
        k = k + 1  
        # This inner loop will print number of stars  
        for j in range(0, i):  
            print("* ", end="")  
        print("")  
timer.start()
diamond()
timer.stop()