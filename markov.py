import argparse
from Reader import Reader


class Markov(object):
    def add_chain(self, sent):
        print(sent)


class Node(object):
    def __init__(self, word):
        self.word = word


class Vertex(object):
    def __init__(self, f, t):
        self.f = f
        self.t = t

if __name__ == '__main__':
    print("HELLO")
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', default=None, nargs='?')
    args = parser.parse_args()
    print(args)
    if args.filename is not None:
        r = Reader(args.filename)
        sentences = r.get_sentences
        m = Markov();

        for sent in sentences:
            sent[len(sent)-1] = sent[len(sent)-1].rstrip('\n')
            m.add_chain(sent)
    else:
        print("No filename")





