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

def doit(string="Capsule Lab"):
    char_list=[]
    for x in string:
        char_list.append(x)
    sorter = []
    i=0
    while (len(char_list)):
        i+=1
        temp = char_list.pop()
        try:
            if sorter[-1] > temp:
                sorter.append(temp)
            else:
                char_list.append(sorter.pop())
                sorter.append(temp)
        except IndexError:
            sorter.append(temp)
            
        print(f"Round {i} {char_list} -> {sorter}")
timer.start()
print("Challenge 6 Output: ")
doit()
timer.stop()