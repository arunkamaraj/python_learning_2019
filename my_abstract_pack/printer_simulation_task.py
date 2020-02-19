import random
import my_abstract_pack.abstract_pack as abstrat_type
# class Printer:
#     def __init__(self, ppm):
#         self.cur_task = None
#         self.expected_time = 0
#         self.page_per_min = ppm
#
#     def is_printer_free(self):
#         return self.cur_task == None
#
#     def tick(self):
#
#         # if self.cur_task != None and self.expected_time > 0:
#         #     self.expected_time = self.expected_time -1
#         #
#         # self.cur_task = None
#         if self.cur_task != None:
#             self.expected_time = self.expected_time - 1
#             if self.expected_time <= 0:
#                 self.cur_task = None
#
#     def assigning_task(self, task):
#         self.cur_task = task
#         self.expected_time = task.get_page_no() * 60//self.page_per_min
#
# class Task:
#     def __init__(self, cur_time):
#         self.time_stamp = cur_time
#         self.page_no = random.randrange(1,21)
#         print("Page no", self.page_no)
#
#     def get_task_time_stap(self):
#         return self.time_stamp
#
#     def get_task_waiting_time(self, picking_time):
#         return picking_time - self.time_stamp
#
#     def get_page_no(self):
#         return self.page_no
#
# def simulation(lab_time, taskname):
#     queue = abstrat_type.Queue()
#     printer = Printer(5)
#     avg_waiting_time =[]
#
#     for cur_time in range(lab_time):
#         if new_print_task():
#             task = Task(cur_time)
#             queue.enqueue(task)
#
#         if printer.is_printer_free() and (not queue.is_empty()):
#             cur_task = queue.dequeue()
#             avg_waiting_time.append(task.get_task_waiting_time(cur_time))
#             printer.assigning_task(cur_task)
#
#         printer.tick()
#
#     print ("Printing avg timing",avg_waiting_time, 'length', len(avg_waiting_time), "task name:", taskname )
#
# def new_print_task():
#     num = random.randrange(1, 181)
#     if num == 180:
#         return True
#     else:
#         return  False
#
# person_count_in_lab = [1]
# total_lab_time =  3600 # in secs
#
# for i in person_count_in_lab:
#     print ('It is for person', i)
#     simulation(total_lab_time, i)



class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
        print("Page no", self.pages)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute, taskname):

    labprinter = Printer(pagesPerMinute)
    printQueue = abstrat_type.Queue()
    waitingtimes = []
    print ("waiting time", waitingtimes, "queue size",printQueue.size())

    for currentSecond in range(numSeconds):

      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.is_empty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append( nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    print("Printing avg timing", waitingtimes, 'length', len(waitingtimes), "task name:", taskname)
    # averageWait=sum(waitingtimes)/len(waitingtimes)
    # print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5, i)