import datetime, time
file = open('log.txt','w')
log = open('log.txt')

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
for i in range(1,7):
    time.sleep(1)
    file.write(f"Log Entry {i} {timer.lap()}\n")
print(" Printing contents of Log file: ")
content = log.readlines()
print(content)
for i in range(len(content)):
    print(content[i])
timer.stop()
file.close()
log.close()