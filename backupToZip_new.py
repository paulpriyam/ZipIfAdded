# backupToZip.py - Copies entire folder and its content into a zip file

import zipfile,os,send2trash,shelve

filesize=0
def backupToZip(folder):
    folder=os.path.abspath(folder) # absolute path of the folder
    os.chdir(folder)
    os.chdir('../')
    number=1
    if os.path.exists(folder):
        os.chdir('C:\\Users\\Abc\\pythonScripts')
        shelveFile=shelve.open('backup')
        if shelveFile['size']== os.path.getsize('E:\\pics'):
            print('new files added.')
            os.chdir(folder)
            os.chdir('../')
            while True:
                zipFileName=os.path.basename(folder)+'_'+str(number)+'.zip' #name of the zip file
                if not os.path.exists(zipFileName):
                    break
                number=number+1

            print('Creating %s'%(zipFileName))
            backupZip=zipfile.ZipFile(zipFileName,'w')

            #walk through entire folder and compress files
            for folderName,subFolders,fileNames in os.walk(folder):
                print('Adding files in %s'%(folderName))
                backupZip.write(folderName)
                #Add all the files
                for files in fileNames:
                    if files.startswith(os.path.basename(folder) +'_') and files.endswith('.zip'):
                        continue
                    backupZip.write(os.path.join(folderName,files))

            backupZip.close()
            print('DONE')
            # delete the folder
            send2trash.send2trash(folder)
            if not os.path.exists(folder):
                print('FOLDER SUCCESSFULLY DELETED.')
        else:
            print('NO CHANGES were made to the file')

    else:
        print('FILE ALREADY DELETED.FILE %s NOT FOUND'%(folder))
if os.path.exists('E:\\pics'):
    shelveFileSize=shelve.open('backup')
    filesize=os.path.getsize('E:\\pics')
    shelveFileSize['size']=filesize
    print(shelveFileSize['size'])
    shelveFileSize.close()
    print(str(filesize))
    backupToZip('E:\\pics')
else:
    print('FILE DOES NOT EXISTS OR ALREADY ZIP')
