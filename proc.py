import queue as Queue, multiprocessing, os
import shutil

fileQueue = Queue.Queue()
destPath = './dest'

class MultiProcessedCopy:
    totalFiles = 0
    copyCount = 0
    lock = multiprocessing.Lock()

    def __init__(self):
        with open("filelist.txt", "r") as txt: #txt with a file per line
            fileList = txt.read().splitlines()

        if not os.path.exists(destPath):
            os.mkdir(destPath)

        self.totalFiles = len(fileList)

        print(str(self.totalFiles) + " files to copy.")
        self.processWorkerCopy(fileList)


    def CopyWorker(self, fileName):
        shutil.copy(fileName, destPath)
        self.lock.acquire()
        self.copyCount += 1
        percent = (self.copyCount * 100) / self.totalFiles
        self.lock.release()

    def processWorkerCopy(self, fileNameList):
        pool = multiprocessing.Pool(6)
        pool.map(self.CopyWorker, fileNameList)
        pool.close()
        pool.join()

MultiProcessedCopy()