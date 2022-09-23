from zipfile import ZipFile
import os
from termcolor import colored
import patoolib

count = 0


def walk(startroot):
    for root, dirs, files in os.walk(startroot):
        for filenames in files:
            if filenames.endswith('.zip') or filenames.endswith('.Zip'):
                print('zipfile {} found in: {}'.format(filenames, root))
                currentdir = unziponce(root, filenames)
                walk(currentdir)
            elif filenames.endswith('rar'):
                currentdir = unziponce(root, filenames)
                walk(currentdir)

def unziponce(currentdir, zipfilename):
    global count
    copytofoldername = zipfilename[:-4].rstrip()
    if zipfilename.endswith('.rar'):
        if copytofoldername in os.listdir(currentdir):
            copytofoldername+='torar'
            print(colored('a folder with same name already exist take note: ' + currentdir + "/" + zipfilename, 'red'))
        os.mkdir(currentdir + '/' + copytofoldername)
        patoolib.extract_archive(currentdir + '/' + zipfilename, outdir=currentdir + '/' + copytofoldername)
        print(colored('unzipped: {} in {}\n'.format(zipfilename, currentdir), 'green'))
        count += 1
        return currentdir + "/" + copytofoldername

    with ZipFile(currentdir + '/' + zipfilename) as zipObject:
        if copytofoldername in os.listdir(currentdir):
            print(colored('a folder with same name already exist take note: ' + currentdir + "/" + zipfilename, 'red'))
            with open('note.txt', 'a') as f:
                f.write(currentdir + " " + zipfilename + "\n")
            copytofoldername += 'fromzip'
        if zipfilename.endswith('.zip') or zipfilename.endswith('.Zip'):
            print('unziping: {} in {}'.format(zipfilename, currentdir))
            zipObject.extractall(currentdir + '/' + copytofoldername)
            print(colored('unzipped: {} in {}\n'.format(zipfilename, currentdir),'green'))
        count += 1
        return currentdir + "/" + copytofoldername


with open('note.txt', 'w') as f:
    f.write('')
walk('D:/unzip')
with open('note.txt', 'a') as f:
    f.write('total zip file number: ' + str(count))
