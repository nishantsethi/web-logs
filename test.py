from time import sleep


with open('example.log') as f:
            while True:
                print(f.read())
                sleep(1)