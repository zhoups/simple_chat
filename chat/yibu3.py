# coding:utf-8

import time
import thread

def gen_coroutine(f):
    def wrapper(*args, **kwargs):
        gen_f = f()  # gen_f为生成器req_a
        r = gen_f.next()  # r为生成器long_io
        def fun(g):
            ret = g.next() # 执行生成器long_io
            try:
                gen_f.send(ret) # 将结果返回给req_a并使其继续执行
            except StopIteration:
                pass
        thread.start_new_thread(fun, (r,))
    return wrapper

def long_io():
    print "开始执行IO操作"
    time.sleep(5)
    print "完成IO操作，yield回操作结果"
    yield "io result"

@gen_coroutine
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
    req_a()
    req_b()
    while 1:
        pass

if __name__ == '__main__':
    main()