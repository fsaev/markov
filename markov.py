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

    def add_chain(self, sentence):
        current = self.hash_table[hash("<s>")]  # Initialize start of chain
        for word in sentence:

            if hash(current.word) in self.hash_table:
                node = self.hash_table[hash(current.word)]
            else:
                node = 0

            # Creation of next node
            if hash(word) in self.hash_table:
                next_node = self.hash_table[hash(word)]
            else:
                next_node = Node(word)  # create

            if node is not 0:
                current.add_link(next_node)  # add word as seen
                self.count += 1

            self.hash_table[hash(next_node.word)] = next_node  # dump in HT
            current = next_node  # move up chain

        current.add_link(self.hash_table[hash("<\s>")])  # Add end link of chain

    def traverse(self, stoch):
        start = self.hash_table[hash("<s>")]
        current = start
        while current.word is not '<\s>':
            total_links = len(current.links)
            print(total_links)


class Node(object):

    def __init__(self, word):
        self.word = word
        self.links_ht = {}

    def add_link(self, to):
        # print(self.word + " --> " + to.word)
        if hash(to.word) in self.links_ht:
            node = self.links_ht[hash(to.word)]
        else:
            node = 0

        if node is 0:
            link = [1, to]  # count, and node it's pointing towards
            self.links_ht[hash(to.word)] = link
        else:
            link = self.links_ht[hash(to.word)]
            link[0] += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', default=None, nargs='?')
    args = parser.parse_args()
    print(args)
    if args.filename is not None:
        r = Reader(args.filename)
        sentences = r.get_sentences
        m = Markov()

        for sent in sentences:  # for each sentence
            sent[len(sent)-1] = sent[len(sent)-1].rstrip('\n')
            m.add_chain(sent)  # build chain out of words

        print(m.count)

        the = m.hash_table[hash("<s>")]
        links = the.links_ht
        for key in links:
            link = links[key]
            n = link[1]
            cnt = link[0]
            print(n.word + " counted: " + str(cnt))
        #  m.traverse(0)
        print("done")
    else:
        print("No filename")
