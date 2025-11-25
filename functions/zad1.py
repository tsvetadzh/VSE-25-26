array = [1, 2, 3, 11, 23] 
def suma(array):
    sum = 0
    for i in array: #tova obhozhda chislata ot array
        sum += i #tova dobavq kym sumata porednoto chislo
    return sum
answer = suma(array)
print(answer)

def sum_recursive(array):
    if not array: #ako ne e vqrno i se e oburkal
        return 0 #nishto ne stava
    else:
        return array[0] + sum_recursive(array[1:]) #pyrviq element i vikame funkciqta za ostanalite elementi
answer_r =sum_recursive(array)
print(answer_r)
