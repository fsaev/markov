import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', default=None, nargs='?')
    args = parser.parse_args()
    if not args.filename is None:
        words = []
        f = open(args.filename, 'r')
        line = f.readline()
        for line in f:
            words.append(line.split(' '))

        print(words)
    else:
        print("no path")
