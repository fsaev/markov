#!/usr/bin/env python
import argparse
from Reader import Reader
from random import randint


class Markov(object):
    # dict-index of words in chain
    word_idx = {}

    def __init__(self):
        start = Node("<s>")
        end = Node("<\s>")
        self.word_idx[hash(start.word)] = start
        self.word_idx[hash(end.word)] = end

    def add_chain(self, sentence):
        previous = self.word_idx[hash("<s>")]
        sentence.append("<\s>")
        for word in sentence:
            if hash(word) in self.word_idx:  # if word in index
                node = self.word_idx[hash(word)]
                # print(node.word, " exists : ", hash(node.word))
            else:
                node = Node(word)
                self.word_idx[hash(word)] = node
                # print(word, " was created : ", hash(word))

            previous.link_to(node)
            previous = node

    # eta_s: lower tolerance of observations
    def traverse(self, eta_s, minlen):
        if len(self.word_idx) is 0:
            print("Index empty - Build chain first")
            raise
        total_links = 0
        list_links = []
        node = self.word_idx[hash("<s>")]
        iteration = 0
        while node is not self.word_idx[hash("<\s>")]:
            for key in node.links:
                link = node.links[key]
                if link.count > eta_s:
                    if link.to is self.word_idx[hash("<\s>")] \
                            and iteration < int(minlen):
                        continue
                    else:
                        total_links = total_links + link.count
                        for i in range(0, link.count):
                            list_links.append(link)
            print(node.word, "", end="")
            iteration = iteration + 1
            if total_links > 2:
                node = list_links[randint(0, total_links - 1)].to
            else:
                break
            total_links = 0
            list_links = []
        print("<\s>")




class Node(object):
    def __init__(self, word):
        self.word = word
        self.links = {}

    # Note that links are hashed by their to-Node
    def link_to(self, to):
        if hash(to) in self.links:  # if link already established
            link = self.links[hash(to)]
            link.count = link.count + 1  # increment link counta
            # print(self.word, "->", to.word, "(", link.count, ")")
        else:
            link = Link(self, to)
            self.links[hash(to)] = link
            # print(self.word, "->", to.word, " (new)")


class Link(object):
    def __init__(self, fr, to):
        self.fr = fr
        self.to = to
        self.count = 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', default=None, nargs='?')
    parser.add_argument('minlen', default=0, nargs='?')
    args = parser.parse_args()
    if args.filename is not None:
        r = Reader(args.filename)
        sentences = r.get_sentences
        m = Markov()

        for sent in sentences:  # for each sentence
            sent[len(sent)-1] = sent[len(sent)-1].rstrip('\n')
            m.add_chain(sent)  # build chain out of words

#        the = m.hash_table[hash("<s>")]
#        links = the.links_ht
#        for key in links:
#            link = links[key]
#            n = link[1]
#            cnt = link[0]
#            print(n.word + " counted: " + str(cnt))
        m.traverse(0, args.minlen)
    else:
        print("No filename")
