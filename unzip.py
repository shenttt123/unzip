from zipfile import ZipFile
import os
from termcolor import colored

count = 0


def walk(startroot):
    print('Current directory: ', startroot)
    for root, dirs, files in os.walk(startroot):
        for filenames in files:
            if filenames.endswith('.zip'):
                print('zipfile {} found in: {}'.format(filenames, root))
                currentdir = unziponce(root, filenames)
                walk(currentdir)


def unziponce(currentdir, zipfilename):
    global count
    with ZipFile(currentdir + '/' + zipfilename) as zipObject:
        copytofoldername = zipfilename.split('.')[-2].rstrip()
        if copytofoldername in os.listdir(currentdir):
            print(colored('a folder with same name already exist take note: ' + currentdir +"/"+ zipfilename, 'red'))
            with open('note.txt', 'a') as f:
                f.write(currentdir + " " + zipfilename + "\n")
            copytofoldername += 'fromzip'
        print('unziping: {} in {}'.format(zipfilename, currentdir))
        zipObject.extractall(currentdir + '/' + copytofoldername)
        print('unzipped: {} in {}'.format(zipfilename, currentdir))
        count += 1
        return currentdir + "/" + copytofoldername


with open('note.txt', 'w') as f:
    f.write('')
walk('D:/unzip')
with open('note.txt', 'a') as f:
    f.write('total zip file number: ' + str(count))
