#!/usr/bin/env python3

def reverse_dictionary(d):
    dict_FtE= {}
    for key in d.keys():
        for x in d[key]:
            if x in dict_FtE.keys():
                dict_FtE[x].append(key)
            else:
                dict_FtE[x] = [key]
    return dict_FtE

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa','salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reverse_dictionary(d)
    pass

if __name__ == "__main__":
    main()
