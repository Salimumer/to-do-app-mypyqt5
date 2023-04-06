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
        my_label = qtw.QLabel("select the port for communication")
        # chhange the font size
        my_label.setFont(qtg.QFont('helvetica',19))
        
        
        self.layout().addWidget(my_label)
        
         
        # #entry the box replace to combo box
        # my_entry = qtw.QLineEdit()
        # my_entry.setObjectName("name_filed")
        # my_entry.setText("")
        # self.layout().addWidget(my_entry) 
        
        
        # create the combo box 
        
        # my_combo = qtw.QComboBox(self,editable=True,insertPolicy=qtw.QComboBox.InsertAtTop)
        # # add  item to combo box
        
        # my_combo.addItem("port1","something")
        # my_combo.addItem("port2",2)
        # my_combo.addItem("port3",qtw.QWidget)
        # my_combo.addItem("port4")
        # my_combo.addItem("por5")
        # my_combo.addItem("port6")
        # my_combo.addItems(["one","two"])
        # my_combo.addItems(2,"Third thing")
        
        
        
        
        # put the combo on the screen
        self.layout().addWidget(my_combo)
        
        
        
        # create the button
        my_button = qtw.QPushButton("press me!", clicked= lambda:press_it(self))
        self.layout().addWidget(my_button) 

        
        
        self.show()
        
        
        def press_it(self):
            # add name to label
            
            my_label.setText(f'selcted {my_combo.currentText()}!')      #text - for giving same output #data - for specific data from us
            

        
        
app = qtw.QApplication([]) 
mw = MainWindow()


# run app 
app.exec_()