#!/usr/bin/env python

# Markov chain for weechat-logs
# Copyright (C) 2016 Gavekort

# This file is part of Markov.

# Markov is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Markov is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

import re

class Reader(object):
    def __init__(self, path):
        self.sentences = []
        self.path = path
        self.f = open(path, 'r', encoding='utf-8')

    @property
    def get_sentences(self):
        f = self.f
        sentences = self.sentences

        if re.match('(.*).weechatlog', self.path) is not None: # if weechat
            for line in f:
                tmpsentences = line.split('\t')
                datetime = tmpsentences[0]
                user = tmpsentences[1]
                msg = tmpsentences[2]
                if re.match('<--|-->|--', user) is None:
                    sentences.append(msg.split(' '))
        else:
            for line in f:
                sentences.append(line.split(' '))

        return sentences
