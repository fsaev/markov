
class Reader(object):
    def __init__(self, path):
        self.sentences = []
        self.f = open(path, 'r')

    @property
    def get_sentences(self):
        f = self.f
        sentences = self.sentences

        for line in f:
            sentences.append(line.split(' '))

        return sentences
