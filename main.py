import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # add a title
        self.setGeometry(100,200,300,300)   #size the box
        self.setWindowTitle("hello world")
        
        # set layout
        self.setLayout(qtw.QVBoxLayout())  #vertical v and horizontall H
        
        # craete label
        my_label = qtw.QLabel("hello world what is the your name")
        # chhange the font size
        my_label.setFont(qtg.QFont('helvetica',19))
        
        
        self.layout().addWidget(my_label)
        
         
        #entry the box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_filed")
        my_entry.setText("")
        self.layout().addWidget(my_entry) 
        
        
        # create the button
        my_button = qtw.QPushButton("press me!", clicked= lambda:press_it())
        self.layout().addWidget(my_button) 

        
        
        self.show()
        
        
        def press_it(self):
            my_label.setText(f'hello{my_entry.text}')
            my_entry.setText("")

        
        
app = qtw.QApplication([]) 
mw = MainWindow()


# run app 
app.exec_()