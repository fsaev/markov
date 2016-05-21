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
# along with Markov.  If not, see <http://www.gnu.org/licenses/>.

import re

class Reader(object):
    def __init__(self, path):
        self.fh = open(path, 'r', encoding='utf-8')

        # https://tools.ietf.org/html/rfc1459#section-2.3.1
        # https://tools.ietf.org/html/rfc2812#section-2.3.1
        self.irc_nick_pat = '[a-zA-Z0-9\[\]\\\`_\-^{|}]+'
        self.irc_user_status = ('@', '~', '+', '%', '&')

    @property
    def get_sentences(self):
        if re.match('(.*).weechatlog', self.fh.name):
            return self._get_irc_sentences('weechat')
        else:
            # default to all words in line
            return [line.split(' ') for line in self.fh.readlines()]

    def _get_irc_sentences(self, client):
        sentences = []

        for line in self.fh.readlines():
            try:
                # dynamic function call, e.g. _parse_weechat
                nick, msg = getattr(self, '_parse_' + client)(line)

                # slower than matching 'not nick', but more versatile
                if re.match(self.irc_nick_pat, nick):
                    sentences.append(msg.split(' '))
            except TypeError:
                # invalid line, e.g. False returned from _parse function
                continue

        return sentences

    def _parse_weechat(self, line):
        try:
            nick, msg = line.split('\t')[1:]

            # strip user status
            if nick.startswith(self.irc_user_status):
                nick = nick[1:]

            return nick, msg.rstrip()
        except Exception:
            return False
