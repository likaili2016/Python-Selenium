#coding=utf-8
import sys

# print >> sys.stderr, 'Fatal error: invalid input !'  # >> 表示定向输出
# print >> sys.stderr, 'Fatal error: invalid input !'

# logfile = open('/mylog.txt', 'a')
# print >> logfile, 'Fatal error: invalid input !'
# logfile.close()

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print ('2015-03-25')

now()


def test():
    print ( 'Hello, %s' % 'world')

test()

