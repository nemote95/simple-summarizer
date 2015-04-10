# coding=UTF-8
from __future__ import division
import re
 
class Summary(object):
    def __init__(self,article):
        self.article=article
    def splitToSentences(self, content):
        content = content.replace("\n", ". ")
        return content.split(". ")
 
    def splitToParagraphs(self):
        return self.article.split("\n\n")
 
    def sentencesIntersection(self, sent1, sent2):
        nonkeywords="""where when what why who whose yes no and or into would like does does'nt not 
        could might will can may wont am is are was if were been has have had do done did the of
        a an to in as off on up i he she it we by since because you they me her him us them mine hers
        his its it's ours yours theirs my his our their this that these those so since in with too less more
        most least at then be been for just only out with ; : \' , ! ? > < / \  \" [ ] ( ) { } . + - * & ^ % $ # ~  """.split()
        s1 = set(sent1.split(" "))
        s2 = set(sent2.split(" "))
        nk=set(nonkeywords)
        s1s2=s1.intersection(s2)
        k=s1s2-nk
        if (len(s1) + len(s2)) == 0:
            return 0
        return len(k) / ((len(s1) + len(s2)))
 
    def removeNonAlphabetic(self, sentence):
        sentence = re.sub(r'\W+', '', sentence)
        return sentence
 
 
    def rank (self):

        sentences = self.splitToSentences(self.article)
        n = len(sentences)
        values = [[0 for x in xrange(n)] for x in xrange(n)]
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.sentencesIntersection(sentences[i], sentences[j])
        sentences_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            sentences_dic[self.removeNonAlphabetic(sentences[i])] = score
        return sentences_dic
    
    def getBest(self, paragraph, sentences_dic):
 
        sentences = self.splitToSentences(paragraph)
        if len(sentences) < 2:
            return ""
        best_sentence = ""
        max_value = 0
        for s in sentences:
            strip_s = self.removeNonAlphabetic(s)
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s]
                    best_sentence = s
 
        return best_sentence
 
    def getSummary(self,  sentences_dic):
 
        # Split the self.article into paragraphs
        paragraphs = self.splitToParagraphs()
 
        # Add the title
        summary = []
        summary.append("")
 
        # Add the best sentence from each paragraph
        for p in paragraphs:
            sentence = self.getBest(p, sentences_dic).strip()
            if sentence:
                summary.append(sentence)
 
        return ("\n").join(summary)
