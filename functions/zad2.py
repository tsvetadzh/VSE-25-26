string = "Hello"

def reverse(string):
    s = ""
    for i in string: #obhozhda stringa
        s = i + s #kum noviq dobavq segashniq
    return s

def reverce(string):
    if len(string) <= 1: #ne ok sluchai
        return string
    return reverce(string[1:]) + string[0] #vzimame stringa bez purviq sumvol i oryshtame go s rekursiq i dobavqme pyrviq simvol
print(reverse(string))
print(reverce(string))
