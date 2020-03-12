#reading a file's input
fw = open('sample text','w')
fw.write('writing some stuff in my text file \n')
fw.write('I like bacon \n')
fw.close()

fr = open('sample text','r')
text = fr.read()
print(text)
fr.close()