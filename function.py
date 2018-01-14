#encoding=utf-8
pi=3.14
def area_of_circle(r):
    return pi*r**2;

def sum(start,end,func):
    total=0;
    for x in range(start,end):
        total+=func(x);
    return total;


def func1(x):
    return x;

def func2(x):
    return x**2+1


print area_of_circle(2);
print sum(1,100,func1);
print sum(1,100,func2);
