def a_function():
    print(" i am a function")
def function_with_args(x,y):
    print("x ",x  ," y " , y)
def loop_function():
    i =0
    while i < 10:
        print("i = " , i)
        i+=1
def for_loop():
    names =["cnas", "bhmed","amine"]
    myname = "anas"
    names.sort()
    for one in names:
        print("fruit name is ",one)
    for char in myname:
        print("[" , char,"]")
a_function() #we called here
function_with_args(13,37)
loop_function()
for_loop()