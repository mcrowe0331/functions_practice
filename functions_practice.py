def hello():
    print("Good afternoon")

def pack(x,y,z):
    return [x,y,z]

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")

