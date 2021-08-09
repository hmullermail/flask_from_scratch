from flask import current_app

from app import db
from app.main import bp

import os, base64, shutil, errno
import threading, multiprocessing
import time, datetime, logging, functools, math

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

count_threads=0
count_processes=0
all_functions=[]

def exec_time(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print(f'Decorated function {f.__name__!r} being executed...')
        t1 = time.time()
        result = f(*args, **kwargs)
        print(f"[{f.__name__!r}] took {time.time() - t1} seconds")
        return result
    return wrapper

def reg_func(f):
	all_functions.append(f)
	return f


@exec_time
def find_factor(number):
    logging.debug('LOL ')
    flag=True
    for j in range(2,round(number/2)+1):
        if (number%j==0):
            flag=False
            break

    if(flag==True):
        return(number)
    return(j)

@reg_func
def sayhello():
	logging.debug(f'Hello at {datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")}')

@reg_func
def cpu_thread(function, arg):
	global count_threads
	count_threads +=1
	threadObj = threading.Thread(name=''.join(['thread', '_', function.__name__, '_', str(count_threads)]), target=function, args=arg)
	threadObj.setDaemon(True)
	threadObj.start()
	return threadObj

@reg_func
def core_process(function, arg):
  processObj = multiprocessing.Process(name='process'+str(function), target=function, args=arg)
  processObj.start()
  return processObj

@reg_func
def OnBoot():
  threadObj = threading.Thread(name='OnBoot', target=boot, args=[current_app._get_current_object()])
  threadObj.setDaemon(True)
  threadObj.start()


def boot(app):
    with app.app_context():      
        logging.debug(f'Starting Up at {datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")}') 
        
        number = 191111113

        p1=core_process(find_factor, [number])
        p2=core_process(find_factor, [number])
        p3=core_process(find_factor, [number])
        p4=core_process(find_factor, [number])
        
        p1.join()
        p2.join()
        p3.join()
        p4.join()

        t1=cpu_thread(find_factor, [number])
        t2=cpu_thread(find_factor, [number])
        t3=cpu_thread(find_factor, [number])
        t4=cpu_thread(find_factor, [number])
        
        t1.join()
        t2.join()
        t3.join()
        t4.join()

        logging.debug('Boot... done!')

@reg_func
def cyclic_task(f):
    threadObj = threading.Thread(name='Cyclic_Task' , target=the_task, args=[current_app._get_current_object(), f])
    threadObj.setDaemon(True)
    threadObj.start()

def the_task(app, f):
    with app.app_context():
        while True:
            delta = datetime.timedelta(seconds=app.config['DELTA'])
            f()
            next_cycle = datetime.datetime.now()+delta
            while datetime.datetime.now() < next_cycle:
                time.sleep(1)











