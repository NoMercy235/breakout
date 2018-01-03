import fileinput
import hashlib
import operator


class HighScore:

    def __init__(self):
        self._high_score = HighScore.load()

    def get_scores(self):
        return self._high_score

    def add(self, name, score):
        _hash = hashlib.md5((str(name+str(score)+"pygame")).encode('utf-8'))
        self._high_score.append([name, str(score), _hash.hexdigest()])

        f = open("highscore.dat", 'w')
        for name, score, md5 in self._high_score:
            f.write(str(name)+"[::]"+str(score)+"[::]"+str(md5)+"\n")

        f.close()

    @staticmethod
    def load():
        high_score = []
        for line in fileinput.input("highscore.dat"):
            name, score, md5 = line.split('[::]')
            md5 = md5.replace('\n', '')

            if str(hashlib.md5(str.encode(str(name+score+"pygame"))).hexdigest()) == str(md5):
                high_score.append([str(name), int(score), str(md5)])

        high_score.sort(key=operator.itemgetter(1), reverse=True)
        high_score = high_score[0:11]

        return high_score
