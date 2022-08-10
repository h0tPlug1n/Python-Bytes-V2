import datetime
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

def drawCircle(name="Capsule"):
    r=len(name)
    print(f"Entered name is {name} and its length is {r}")
    N = 2 * r + 1
    for i in range(N):
        for j in range(N):
            x = i - r
            y = j - r
            if x==0 and y==0:
                print("7",end=' ')
            elif x * x + y * y <= r * r + 1:
                print("x", end = " ")
            else:
                print(" ", end = " ")
        
        print()
timer.start()
drawCircle()
timer.stop()