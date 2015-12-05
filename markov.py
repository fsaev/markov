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
        previous = self.hash_table[hash("<s>")]  #Initialize start of chain
        for word in sentence:
            try:
                n = self.hash_table[hash(word)]  #see if we have word
                print("word ", n.word, " exists")
                previous.add_link(n, False)  #add word as seen
            except:  #if we don't have word
                self.count += 1
                n = Node(word)  #create
                previous.add_link(n, True)  #add as unseen

            self.hash_table[hash(n.word)] = n  #dump in HT
            previous = n

        previous.add_link(hash("<\s>"), 1)  #Add end link of chain

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

    def add_link(self, node, unseen):
        if unseen:
            link = [1, node]  #count, and node it's pointing towards
            self.links_ht[hash(node.word)] = link
        else:
            link = self.links_ht[hash(node.word)]
            link[0] += 1
            print("Updated link it is now " + link[0])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', default=None, nargs='?')
    args = parser.parse_args()
    print(args)
    if args.filename is not None:
        r = Reader(args.filename)
        sentences = r.get_sentences
        m = Markov()

        for sent in sentences:  #for each sentence
            sent[len(sent)-1] = sent[len(sent)-1].rstrip('\n')  #split into words
            m.add_chain(sent)  #build chain out of words

        print(m.count)
       # m.traverse(0)
        print("done")
    else:
        print("No filename")





