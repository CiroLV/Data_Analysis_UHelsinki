#!/usr/bin/env python3

def interleave(*lists):
    final_list = []
    for t in zip(*lists):
        new_element = list(t)
        final_list.extend(new_element)
    return final_list

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
