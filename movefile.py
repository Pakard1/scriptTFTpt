import os
import shutil

# Move a file by renaming it's path
os.rename('D:/Pythonprojects/tftptscript/listarank.csv', 'D:/Pythonprojects/tftptscript/old/listarank.csv')
os.rename('D:/Pythonprojects/tftptscript/listarank.jpeg', 'D:/Pythonprojects/tftptscript/old/listarank.jpeg')
os.rename('D:/Pythonprojects/tftptscript/listarank.png', 'D:/Pythonprojects/tftptscript/old/listarank.png')

# Move a file from the directory d1 to d2
#shutil.move('/Users/billy/d1/xfile.txt', '/Users/billy/d2/xfile.txt')