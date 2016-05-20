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
            print("Weechat-log mode")
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
