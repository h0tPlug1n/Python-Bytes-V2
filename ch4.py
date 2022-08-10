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

def listManipulation(name="Capsule Labs"):
    nameList = []
    dirArray = []
    for i in range(0,len(name)):
        nameList.append(name[i])
        if(ord(name[i])<ord(name[i-1])):
            dirArray.append('-')
        else:
            dirArray.append('+')
    count = 0
    for j in range(0,len(dirArray)-1):
        if(dirArray[j]!=dirArray[j+1]):
            count+=1
    print(f"Name Array: {nameList}")
    print(f"Dir Array: {dirArray}")
    print(f"No. of direction changes: {count}")

timer.start()
listManipulation()
timer.stop()