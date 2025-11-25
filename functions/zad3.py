n = 1
def fibonachi_r(n):
    if n <= 1: #ne ok sluchai
        return n
    return fibonachi_r(n - 1) + fibonachi_r(n - 2)#f(n) shte e sbora na f(n-1) i f(n - 2) za da stane fibonachi

print(fibonachi_r(n))