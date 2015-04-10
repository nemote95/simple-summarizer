import sys
sys.path.insert(0, 'C:\\Users\\NEGAR\\Desktop\\proj2\\lib')

from mainWidget import *
#==========================================================================================
class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.initUI()
#----------------------------------------------------------------------------------------------------------------------------- 
    def initUI(self):
        """displays main window ui """
        self.setWindowTitle('Simple Auto Summarize ')
        self.setWindowIcon(QIcon('data\summ.png'))
        
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("data\summbg.jpg")))
        self.setPalette(palette)

        self.setGeometry(300,150,600,500)

        widget=AutoSummarization()
        self.setCentralWidget(widget)
        
        openAction= QAction(QIcon('data\open.png'), 'Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(widget.summFile)
        
        saveAction= QAction(QIcon('data\save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(widget.saveFile)
        
        exitAction= QAction(QIcon('data\exit.gif'), 'Exit', self)
        exitAction.setShortcut('Ctrl+E')
        exitAction.triggered.connect(self.close)

        menubar = self.menuBar()
        windowMenu = menubar.addMenu('&File')
        windowMenu.addAction(openAction)
        windowMenu.addAction(saveAction)
        windowMenu.addAction(exitAction)
        
        self.show()
#-----------------------------------------------------------------------------------------------------------------------------         
    def closeEvent(self, event):
        """shows a message box when user wants to close the app"""
        reply = QMessageBox.question(self, 'Message',"Are you sure you want to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
#-----------------------------------------------------------------------------------------------------------------------------         
def main():
    
    app =QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()   

        
