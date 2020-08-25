#!/usr/bin/env python3

def distinct_characters(L):

    final_dict = {}
    for x in L:
        entry = set(x)
        final_dict[x] = len(entry)
    return final_dict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
