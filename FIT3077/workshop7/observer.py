import threading
from abc import ABC, abstractmethod
import time
import pdb

class Observer():
    def update(self):


class Subject(ABC, threading.Thread):
    observers = []

    def attach(self, newObserver: Observer):
        self.observers + [newObserver]


    def detach(self, observerToRemove):
        for i, observer in enumerate(self.observers):
            if observerToRemove is observer:
                self.observers.pop(i)

    @abstractmethod
    def notify(self):
        pass


class Wicket(subject):
    def notify(self):
        for observer in observers:
            observer.update()


class Boundary(subject):
    def notify(self):
        for observer in observers:
            observer.update()

class Observer(ABC):
    def notify(self):
        for observer in observers:
            observer.update()


class Downloader(threading.Thread):

   def run(self):
      print 'downloading'
      for i in range(1,5):
         self.i = i
         time.sleep(2)
			print 'unfunf'
         return 'hello world'


class Worker(threading.Thread):
   def run(self):
      for i in range(1,5):
         print 'worker running: %i (%i)' % (i, t.i)
         time.sleep(1)
         t.join()

         print 'done'

# t = Downloader()
# t.start()

# time.sleep(1)

# t1 = Worker()
# t1.start()

# t2 = Worker()
# t2.start()

# t3 = Worker()
# t3.start()
