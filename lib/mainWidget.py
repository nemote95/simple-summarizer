import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from summary import *
from html import *
from title import *
#=========================================================================================
class AutoSummarization(QWidget):
    def __init__(self): 
        super(AutoSummarization,self).__init__()
        self.initUI()
        
    def initUI(self):
        """initializes the ui including buttons and text fields"""
        self.grid=QGridLayout()

        self.urlField=QLineEdit('enter the url of the page you want to summarize.')
        self.urlField.setStyleSheet("font: 10pt \"SansSerif \"; background-color: white; ")
        self.grid.addWidget(self.urlField,1,0,1,1)
        
        self.urlBtn=QPushButton(' Summarize a Page')
        self.urlBtn.setIcon(QIcon('data\url.png'))
        self.urlBtn.setIconSize(QSize(22,22))
        self.urlBtn.setStyleSheet("font: 10pt \"SansSerif \";")
        self.urlBtn.clicked.connect(self.summUrl)
        self.grid.addWidget(self.urlBtn,1,1,1,1)

        self.fileLabel=QLabel('No File')
        self.fileLabel.setStyleSheet("font: 10pt \"SansSerif \"; background-color: white; ")
        self.grid.addWidget(self.fileLabel,2,0,1,1)

        self.fileBtn=QPushButton(' Summarize a File')
        self.fileBtn.setIcon(QIcon('data\open.png'))
        self.fileBtn.setIconSize(QSize(22,22))
        self.fileBtn.setStyleSheet("font: 10pt \"SansSerif \";")
        self.fileBtn.clicked.connect(self.summFile)
        self.grid.addWidget(self.fileBtn,2,1,1,1)

        self.titleLabel=QLabel('No Title')
        self.titleLabel.setStyleSheet("font: 10pt \"SansSerif \"; background-color: white; ")
        self.grid.addWidget(self.titleLabel,3,0,1,1)

        self.titleBtn=QPushButton('Extract a Title   ')
        self.titleBtn.setIcon(QIcon('data\extract.png'))
        self.titleBtn.setIconSize(QSize(22,22))
        self.titleBtn.setStyleSheet("font: 10pt \"SansSerif \";")
        self.titleBtn.clicked.connect(self.extractTitle)
        self.grid.addWidget(self.titleBtn,3,1,1,1)
        
        self.sumText=QTextEdit()
        self.sumText.setStyleSheet("font: 11pt \"SansSerif \";")
        self.grid.addWidget(self.sumText,4,0,1,1)

        self.saveBtn=QPushButton('Save The Summary')
        self.saveBtn.setStyleSheet("font: 10pt \"SansSerif \";")
        self.saveBtn.setIcon(QIcon('data\save.png'))
        self.saveBtn.setIconSize(QSize(22,22))
        self.saveBtn.clicked.connect(self.saveFile)
        self.grid.addWidget(self.saveBtn,7,1,1,1)

        self.statusLabel=QLabel('')
        self.statusLabel.setStyleSheet("font: 10pt \"SansSerif \"; background-color: white; ")
        self.grid.addWidget(self.statusLabel,5,1,1,1)

        self.setLayout(self.grid)

#------------------------------------------------------saveFile------------------------------------------------------------
    def saveFile(self):
        """saves the contant of the summary text field"""
        fileName = QFileDialog.getSaveFileName(self, "Save Text File:")
        if fileName:
            file_ = open(fileName, 'w')
            text= self.sumText.toPlainText()
            file_.write(text)
            file_.close()
#-------------------------------------------------------summFile---------------------------------------------------------        
    def summFile(self):
        """summarizes the given text file , shows the summary in the text field """
        fileName=QFileDialog.getOpenFileName(self, "Open Text File:")
        self.fileLabel.setText(fileName)
        if fileName:
            file_=open(fileName,'r')
            con=file_.read()
            st = Summary(con)
            sentences_dic = st.rank() 
            summary = st.getSummary(sentences_dic)
            self.sumText.setText(summary)
            file_.close()
            self.statusLabel.setText(" %f percent of the \n text has been summarized"%(100-(100*len(summary)/float(len(con)))))
            #except:
                #QMessageBox.warning(self, 'Error',"open a valid file please !", QMessageBox.Ok)
#-----------------------------------------------------summUrl-------------------------------------------------------------            
    def summUrl(self):
        """finds a text in the given page and then summarizes it """
        if self.urlField.text():
            try:
                con=findText(urlopen(unicode(self.urlField.text())).read())
                st = Summary()
                sentences_dic = st.get_senteces_ranks(con) 
                summary = st.get_summary(con, sentences_dic)
                self.sumText.setText(summary)
                self.statusLabel.setText("%f percent of the \ntext has been summarized"%(100-(100*len(summary)/float(len(con)))))
            except :
                QMessageBox.warning(self, 'Error',"url is not valid or the connection failed !", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, 'Error',"Enter a Url !", QMessageBox.Ok)
#------------------------------------------------------extractTitle---------------------------------------------------------
    def extractTitle(self):
        """extracts a title from the summary,ignores the words that the user enters in the input dialog"""
        content=self.sumText.toPlainText()
        if content:
            ignorelist, ok = QInputDialog.getText(self,'Ignore List', 'split the ignore words with , or space')
            if ok :
                ignorelist=unicode(ignorelist).replace(',',' ').split()
                title=Title(unicode(content),ignorelist).getTitle()
                self.titleLabel.setText("Title: "+title)
        else:
            QMessageBox.warning(self, 'Error',"you should summarize a file or a url at first !", QMessageBox.Ok)   
        
