import argparse
from Reader import Reader
from random import randint


class Markov(object):
    hash_table = {}

    def __init__(self):
        self.count = 0
        start = Node("<s>")
        end = Node("<\s>")
        self.hash_table[hash(start.word)] = start
        self.hash_table[hash(end.word)] = end
        print(hash(start.word))

    def add_chain(self, sentence):
        previous = self.hash_table[hash("<s>")]
        for word in sentence:
            try:
                n = self.hash_table[hash(word)]
                print("word ", n.word, " exists")
            except:
                self.count += 1
                n = Node(word)

            previous.add_link(n)
            self.hash_table[hash(n.word)] = n
            previous = n

        previous.add_link(hash("<\s>"))

    def get_count(self):
        print(self.count)


class Node(object):

    def __init__(self, word):
        self.word = word
        self.links = []

    def add_link(self, Vertex):
        self.links.append(Vertex)


class Vertex(object):
    def __init__(self, f, t):
        self.f = f
        self.t = t
        self.count = 0

    def inc_count(self, by):
        self.count += by

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', default=None, nargs='?')
    args = parser.parse_args()
    print(args)
    if args.filename is not None:
        r = Reader(args.filename)
        sentences = r.get_sentences
        m = Markov()

        for sent in sentences:
            sent[len(sent)-1] = sent[len(sent)-1].rstrip('\n')
            m.add_chain(sent)

        m.get_count()
        print("done")
    else:
        print("No filename")





