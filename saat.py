import time
import datetime

class Time():

    def __init__(self):
        self.taketime()

    def taketime(self):

        taketime = datetime.datetime.now()

        self.year = taketime.year    
        self.month = taketime.month    
        self.day = taketime.day    
        self.hour = taketime.hour    
        self.minute = taketime.minute    
        self.second = taketime.second    

    def output(self):

        while True:

            print("\rBugünün tarihi {}/{}/{} ve şu an saat {}:{}:{}".format(self.day, self.month, self.year, self.hour, self.minute, self.second)) 
            time.sleep(1)
            self.taketime()


if __name__ == "__main__":

    p = Time()
    p.output()



