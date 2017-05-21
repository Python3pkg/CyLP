import urllib.request, urllib.parse, urllib.error
import os

f = urllib.request.urlopen("http://www.netlib.org/lp/data/")
lines = f.read().splitlines()

for line in lines:
    if line[:4] == 'file':
        ind_start = line.index('>')
        line = line[(ind_start+1):]
        ind_end = line.index('<')
        line = line[:ind_end]
        print('Downloading ', line, '...')
        urllib.request.urlretrieve("http://www.netlib.org/lp/data/"+line, line)
        print('emps-ing ', line, '...')
        os.system('./emps ' + line + ' > ' + line + '.mps')

f.close()
