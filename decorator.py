#encoding=utf-8
#修饰器
import functools
def log(text):
    if callable(text):
        @functools.wraps(text)
        def wrapper(*args,**kw):
            print 'begin call %s:' %text.__name__
            text(*args,**kw)
            print 'end call %s:' %text.__name__
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print 'begin %s call %s:' % (text,func.__name__)
                func(*args,**kw)
                print 'end  %s call %s:' % (text,func.__name__)
            return wrapper
        return decorator



@log
def f1():
    print 'f1ing'

@log('excute')
def f2():
    print 'f2ing'


f1()
f2()
