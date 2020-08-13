#!/usr/bin/env python3


def main():
    for i in range(1,11):
        def triple():
            n1 = i*3
            return n1
        def square():
            n2 = i**2
            return n2
        print(f"triple({i})=={triple()} square({i})=={square()}")

if __name__ == "__main__":
    main()
