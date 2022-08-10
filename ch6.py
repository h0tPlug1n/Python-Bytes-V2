import math, datetime
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
def checkPrime(n=1147797409030815779):
    prime_flag = 0
    
    if(n > 1):
        if n%2==0:
            return None
        for i in range(3, int(math.sqrt(n)) + 1,10):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            print(f"{n} is prime")
        else:
            return None
    else:
        return None

timer.start()
checkPrime()
timer.stop()