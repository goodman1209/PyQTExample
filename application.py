#!/usr/bin/env python
import sys
import ui.homepage.uihomeentry as uihome
import example
#from  ui.homepage.uihomeentry import str
#print(str)
print(uihome.str)
print("Allan")
print(__name__)


if __name__ == '__main__':
    #import sys
    from PyQt5.QtWidgets import QApplication
 
    app = QApplication(sys.argv)
    #addressBook = uihome.Application()
    addressBook = example.ExampleApp()
    addressBook.show()

    sys.exit(app.exec_())