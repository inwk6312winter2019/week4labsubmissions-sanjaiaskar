import os

def print_file(dir):
        for path in os.listdir():
                if os.path.isfile(path):
                        print(path)
print_file('.')



def print_dir(dirname):
        for name in os.listdir(dirname):
                path = os.path.join(dirname,name)
                if os.path.isfile(path):
                        print(path)
                else:
                        walk(path)
print_dir('.')





