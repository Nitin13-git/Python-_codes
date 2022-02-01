#find the distance  b\w words
#c,e distance=2
def distance(word1,word2):
    if len(word1)!=len(word2):
        return -1
    else:
        word_distance=0
        letters='abcdefghijklmnopqrstuvwxyz'
        for i in range(len(word1)):
            word_distance=abs(letters.index(word1[i])-letters.index(word2[i]))
        return word_distance

