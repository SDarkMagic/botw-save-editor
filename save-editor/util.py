import pathlib

class genDirList:
    def __init__(self, pathIn):
        self.listOut = self.checkIsDir(pathIn)

    def checkIsDir(self, pathIn):
        fileList = []
        pathIn = pathlib.Path(pathIn)
        if pathIn.is_file():
            subDir = pathIn
            fileList.append(subDir)
        else:
            for subDir in pathIn.iterdir():
                if subDir.is_dir():
                    fileList.extend(self.checkIsDir(subDir))
                else:
                    fileList.append(subDir)
        return(fileList)