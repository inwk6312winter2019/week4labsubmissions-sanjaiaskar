import os
def sed(pattern, replacement, fin, fout):
    finMem = open(fin)
    foutMem = open(fout, 'w+')
    for line in finMem:
        if pattern in line:
            print 'pattern found'
            newLine = line.replace(pattern,replacement)
            foutMem.write(newLine)
        else:
            foutMem.write(line)

if __name__ == '__main__':
    print os.getcwd()
    pattern = 'oy'
    replacement = 'it'
    fin = "/home/bhavna/desktop/pythonlab/lab4/output.txt"
    fout = "/home/bhavna/desktop/pythonlab/lab4/output.txt"
    sed(pattern, replacement, fin, fout)