#!/usr/bin/env python

# Markov chain for weechat-logs
# Copyright (C) 2016 Gavekort

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import sys
from Reader import Reader
from random import randint

version = 0.8

class Markov(object):
    # dict-index of words in chain
    word_idx = {}

    def __init__(self, sentences):
        start = Node("<s>")
        end = Node("<\s>")
        self.word_idx[hash(start.word)] = start
        self.word_idx[hash(end.word)] = end

        for sent in sentences:  # for each sentence
            sent[len(sent)-1] = sent[len(sent)-1].rstrip('\n')
            self.add_chain(sent)  # build chain out of words

    def add_chain(self, sentence):
        previous = self.word_idx[hash("<s>")]
        sentence.append("<\s>") # Add termination to end
        for word in sentence:
            if hash(word) in self.word_idx:  # if word in index
                node = self.word_idx[hash(word)]
            else:
                node = Node(word)
                self.word_idx[hash(word)] = node

            previous.link_to(node)
            previous = node # Move up chain

    # eta_s: lower tolerance of observations
    def traverse(self, eta_s, minlen):
        total_links = 0
        iteration = 0
        node = self.word_idx[hash("<s>")]
        list_links = []
        if len(self.word_idx) is 0:
            print("Index empty - Build chain first")
            raise
        while node is not self.word_idx[hash("<\s>")]: # While not end
            for key in node.links: # Get all the links
                link = node.links[key]
                if link.count > int(eta_s):
                    # Skip if end and iteration is not minlen
                    if link.to is self.word_idx[hash("<\s>")] \
                                and iteration < int(minlen):
                        continue
                    else:
                        # Put links in a roulette
                        total_links = total_links + link.count
                        for i in range(0, link.count):
                            list_links.append(link)
            if iteration is not 0:
                print(node.word, "", end="")
            iteration = iteration + 1
            if total_links > 2:
                # Roll roulette with 1 position per observation
                node = list_links[randint(0, total_links - 1)].to
            else:
                break
            # Reset
            total_links = 0
            list_links = []



class Node(object):
    def __init__(self, word):
        self.word = word
        self.links = {}

    # Note that links are hashed by their to-Node
    def link_to(self, to):
        if hash(to) in self.links:  # if link already established
            link = self.links[hash(to)]
            link.count = link.count + 1  # increment link counta
        else:
            link = Link(self, to)
            self.links[hash(to)] = link

class Link(object):
    def __init__(self, fr, to):
        self.fr = fr
        self.to = to
        self.count = 1

if __name__ == '__main__':
    # Args
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', metavar='/path/to/data',
                        help='Path to training-data (Required)')
    parser.add_argument('-m', '--minlen', default=5, nargs='?', metavar='number',
                        help='Minimum sentence length to try (Not guaranteed)')
    parser.add_argument('-e', '--eta-s', default=0, nargs='?', metavar='number',
                        help='Minimum amount of observations required')
    parser.add_argument('-nh', '--no-handles', action='store_true',
                        help='Remove "<s> </s>" handles from output')
    parser.add_argument('--version', action='store_true',
                        help='Print version info')
    args = parser.parse_args()

    if args.version is True:
        print(sys.argv[0], version, " -  (C) 2016 Gavekort")
        print("Released under GNU GPLv3")
        sys.exit(0)

    if args.filename is not None:
        try:
            r = Reader(args.filename)
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)
        if args.no_handles is False:
            print("<s> ", end="")
            m = Markov(r.get_sentences)
            m.traverse(args.eta_s, args.minlen)
            print("<\s>")
        else:
            m = Markov(r.get_sentences)
            m.traverse(args.eta_s, args.minlen)
            print("")
    else:
        print("No filename")

