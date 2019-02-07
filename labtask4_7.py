def sed(pattern,replace,filein,fileout):
        try:
                fin=open(filein,'r')
                fout=open(fileout,'w')
        except:
                print('sorry something went wrong!')

        for line in fin:
                line=line.replace(pattern,replace)
                fout.write(line)
        fin.close()
        fout.close()

pattern='pattern'
replace='replace'

filein='testfile.txt'
fileout=filein+'.replaced'

sed(pattern,replace,filein,fileout)




