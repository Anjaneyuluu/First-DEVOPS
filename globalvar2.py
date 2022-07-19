# if we a create avariable with the same name inside the funtion, this variable will be local, and can only be used inside the function.The global variable with the same name will remains as it is was,global ans with the original.

x = "awesome"
def myfunc():
    x = "fantastic"
    print("pythin is " + x)
myfunc()
print("python is " + x)
