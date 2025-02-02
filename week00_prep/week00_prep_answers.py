def greet(name):
    print(f'Hello, {name}!')

print("Exercise 1, GREETINGS")
greet("Jenni")

print("")
def goldilocks(length):
    if length < 140:
        print("Too small!")
    elif length > 150:
        print("Too large!")
    else:
        print("Just right! :)")

print("Exercise 2, GOLDILOCKS")
goldilocks(139)
goldilocks(140)
goldilocks(151)
goldilocks(150)

print("")
def square_list(list):
    new_list = [0 for i in range(len(list))]
    for i in range(len(list)):
        new_list[i] = list[i]**2
    return new_list

print("Exercise 3, SQUARE LIST")

test_list = [1,2,3]
new = square_list(test_list)
print(new)


print("")
def fibonacci_stop(length):
    curr_fibo = 0
    fibo_list = []
    while curr_fibo <= length:
        if len(fibo_list) < 2:
            curr_fibo = 1
        else:
            curr_fibo = curr_fibo + fibo_list[-2]
        
        if curr_fibo < length:
            fibo_list.append(curr_fibo)
    print(fibo_list)
    return fibo_list
print("Exercise 4, FIBONACCI")
fibonacci_stop(4)
fibonacci_stop(30)

print("")
def clean_pitch(pitch, status):
    for i in range(len(pitch)):
        if status[i] != 0 and (pitch[i] < 0 or pitch[i] > 90):
            pitch[i] = -999
        
    return pitch, status
print("Exercise 5, PITCH STATUS")

x = [-1,2,6,95,30]
signal = [1,0,0,0,1]

pitch, status = clean_pitch(x,signal)
print(pitch)
