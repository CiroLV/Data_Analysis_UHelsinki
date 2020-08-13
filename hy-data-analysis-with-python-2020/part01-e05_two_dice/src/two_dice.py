#!/usr/bin/env python3

def main():
    d1 = [1,2,3,4,5,6]
    d2 = [1,2,3,4,5,6]
    for i in d1:
        for j in d2:
            if i + j == 5:
                pair = (i,j)
                print(pair)

if __name__ == "__main__":
    main()
