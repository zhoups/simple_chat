# coding:utf-8

import time
import thread

def long_io(callback):
    """将耗时的操作交给另一线程来处理"""
    def fun(cb): # 回调函数作为参数
        """耗时操作"""
        print "开始执行IO操作"
        time.sleep(5)
        print "完成IO操作，并执行回调函数"
        cb("io result")  # 执行回调函数
    thread.start_new_thread(fun, (callback,))  # 开启线程执行耗时操作

def on_finish(ret):
    """回调函数"""
    print "开始执行回调函数on_finish"
    print "ret: %s" % ret
    print "完成执行回调函数on_finish"

def req_a():
    print "开始处理请求req_a" 
    long_io(on_finish)
    print "离开处理请求req_a"

def req_b():
    print "开始处理请求req_b"
    time.sleep(2) # 添加此句来突出显示程序执行的过程
    print "完成处理请求req_b"

def main():
    req_a()
    req_b()
    while 1: # 添加此句防止程序退出，保证线程可以执行完
        pass

if __name__ == '__main__':
    main()