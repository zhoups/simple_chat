# coding:utf-8

import time
import thread

gen = None # 全局生成器，供long_io使用

def long_io():
    def fun():
        print "开始执行IO操作"
        global gen
        time.sleep(5)
        try:
            print "完成IO操作，并send结果唤醒挂起程序继续执行"
            gen.send("io result")  # 使用send返回结果并唤醒程序继续执行
        except StopIteration: # 捕获生成器完成迭代，防止程序退出
            pass
    thread.start_new_thread(fun, ())

def req_a():
    print "开始处理请求req_a"
    ret = yield long_io()
    print "ret: %s" % ret
    print "完成处理请求req_a"

def req_b():
    print "开始处理请求req_b"
    time.sleep(2)
    print "完成处理请求req_b"

def main():
    global gen
    gen = req_a()
    gen.next() # 开启生成器req_a的执行
    req_b()
    while 1:
        pass

if __name__ == '__main__':
    main()