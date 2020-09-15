import argparse
import pathlib
import json
from saveEditor import util
from saveEditor import save

def main():
    print('Converting .sav files to JSON data!')
    desc = 'Program for converting .sav files to .json data that can then be editted'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("fileToOpen", help='The path to the file to convert, or directory where the files to be converted are located.')
    args = parser.parse_args()
    genFileList = util.genDirList(args.fileToOpen)
    fileList = genFileList.listOut
    for fileObj in fileList:
#        print(fileObj)
        if str(fileObj).split('.')[-1] == 'sav':
            dataOut = save.parseSaveFile(fileObj, skip_bools=False)
            if dataOut != None:
                fileOpen = open(pathlib.Path(str(f'{fileObj}.json')), 'wt')
                fileOpen.write(json.dumps(dataOut, indent=2))
                fileOpen.close()
            else:
                continue
        else:
#            print('Invalid file. Please make sure you are trying to convert a .sav file.')
            continue

if __name__ == "__main__":
    main()