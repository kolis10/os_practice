import os

# print(os.listdir('/'))

# print(os.path.isdir('/temp'))

list_to_avoid = []

def f(path):
    lst = []
    for x in os.listdir(path):
        new_path = os.path.join(path,)
        if x not in list_to_avoid:
            if os.path.isdir(new_path):
                f(new_path)

for x in f('/lib/systemd/system'):
    print(x)
