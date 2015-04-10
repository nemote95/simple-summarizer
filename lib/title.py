import re 
class Title(object):
    """this class finds 2 title for a text (or a summary) by getTitle  method"""
    def __init__(self,summary,ignorelist):
        self.summary=summary
        self.ignorelist=ignorelist
        
    def getTitle(self):
        """this method removes nonkeywords from the text and
            rank other words by the tehir number of occurrence in the text"""
        
        nonkeywords="""where when what why who whose yes no and or into would like does does'nt not 
        could might will can may wont am is are was if were been has have had do done did the of
        a an to in as off on up i he she it we by since because you they me her him us them mine hers
        his its it's ours yours theirs my his our their this that these those so since in with too less more
        most least at then be been for just only out with ; : \' , ! ? > < / \  \" [ ] ( ) { } . + - * & ^ % $ # ~  """.split()+self.ignorelist
        wordList=self.summary.lower().split()
        keywords=[]
        for i in wordList:
            if not(i  in nonkeywords) and not re.match('.*\W.*',i) and not re.match('.*\d.*',i):
               keywords.append(i)
               
        scoreDic={}
        titles=[]
        for word in keywords:
            scoreDic[word]=keywords.count(word)
        for i in range(2):
            title=''
            maxScore=0
            for word in scoreDic.keys():
                if scoreDic[word]>maxScore:
                    maxScore=scoreDic[word]
                    title=word
            titles.append(title)
            del scoreDic[title]
        return titles[0]+' & '+titles[1]
        
