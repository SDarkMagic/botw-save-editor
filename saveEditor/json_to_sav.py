import argparse
import pathlib
import json
from saveEditor import util
import os
from saveEditor import save

def main():
    print('Converting JSON files to .sav files for BotW!')
    desc = 'Program for converting .sav files to .json data that can then be editted'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("fileToOpen", help='The path to the file to convert, or directory where the files to be converted are located.')
    parser.add_argument('-be', '--bigendian', action='store_true', dest='be', help='Whether or not to write the file for WiiU (Big endian) or switch (little Endian). Defaults to little endian; add this flag to write big endian.', required=False, default=False)
    args = parser.parse_args()
    genFileList = util.genDirList(args.fileToOpen)
    fileList = genFileList.listOut
    for fileObj in fileList:
#        print(fileObj)
        if str(fileObj).split('.')[-1] == 'json' and str(fileObj).split('.')[-2] == 'sav':
            fileOpen = open(pathlib.Path(str(f'{fileObj}')), 'rt')
            jsonData = json.loads(fileOpen.read())
            fileOpen.close()
            if args.be:
                writeData = save.writeSaveFile_be(jsonData, pathlib.Path(str(fileObj).rstrip('json')))
            else:
                writeData = save.writeSaveFile_le(jsonData, pathlib.Path(str(fileObj).rstrip('json')))
            if writeData != None:
                writeFile = open(pathlib.Path(str(fileObj).rstrip('.json')), 'wb')
                writeFile.write(bytes(writeData))
                writeFile.close()
                os.remove(pathlib.Path(fileObj))
        else:
#            print('Invalid file. Please make sure you are trying to convert a .json file.')
            continue

if __name__ == "__main__":
    main()