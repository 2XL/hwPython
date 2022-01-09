filename = 'helloworld.txt'

fw = open(filename, 'w')
fw.write('write some text here to the file...')
fw.close()

fr = open(filename, 'r')
message = fr.read()
fr.close()

fa = open(filename, 'a')
fa.write("\n" + 'append more text here!')
fa.close()

fr = open(filename, 'r')
message = fr.read()
fr.close()

print message
