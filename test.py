import argparse

def feb(n):
    a, b = 0, 1
    for i in range(n):
        a,b = b, a+b
    return a

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num', help="The fibonnaci number you wish to calculate",type = int)

    args = parser.parse_args()

    result = feb(args.num)
    print("the " ,str(args.num), "th number in fibonacci series is ", str(result))

main()