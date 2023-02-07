from fastapi import FastAPI

import asyncio

import time
import psutil 
import datetime

fast_api = FastAPI()

@fast_api.get("/")
def root_path():
    return "test"

@fast_api.get("/sync")
def sync_test():
    proc(5)
    proc(7)
    return "sync"

@fast_api.get("/async")
def sync_test():
    
    fire_and_forget(proc, 10)

    return "async"

def proc(t):

    for i in range(t):
        print(i)
        mem = psutil.virtual_memory()
        print(mem.used / mem.total)
        time.sleep(1)

def fire_and_forget(task, *args, **kwagrs):
    loop = asyncio.new_event_loop()

    if callable(task):
        loop.run_in_executor(None, task, *args, **kwagrs)
    else:
        raise TypeError('Task is not callable')
    

def write_s3():

    file_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    f = open('./test/' + file_name,  'w')
    f.write(file_name)
    f.close()