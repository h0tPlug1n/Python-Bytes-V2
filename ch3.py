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


timer.start()

def string(name="Capsule Labs"):
    print(f"Input String: {name}")
    count = {}
    for s in name:
        s=s.lower()
        if not s.isalpha():
            continue
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    lst = []
    for key in count:
        lst.append(key+str(count[key]))  
    lst.sort()
    print(f"Output String: {''.join(lst)}")
string() # Calling the function
timer.stop()