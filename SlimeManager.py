
from __future__ import unicode_literals

import subprocess

from PyQt6 import QtWidgets, QtCore
from FQt import FairUI
from F import OS, RE, DICT
from F.CLASS import Thread
import os
# import youtube_dl
# from pytube import YouTube
from FW.Core.CoreDownloaders import MediaDownloaders

uiFile = OS.get_cwd() + "/SlimeManager.ui"

cw_DIRECTORY = OS.get_cwd()
downloaded_FILE = lambda fileName: f"{cw_DIRECTORY}/{fileName}"
completed_DIRECTORY = f"{cw_DIRECTORY}/completed"

def post_processor():
    for file in OS.get_files_in_directory(completed_DIRECTORY):
        if str(file).endswith(".mp4"):
            newFile = str(file)[:-4]
            newFile = f"{newFile}-rs"
            file = f"{completed_DIRECTORY}/{file}"
            post_process(file, newFile)
            os.remove(file)

def post_process(fileIn, fileOutName):
    fileNameOut = f"{OS.get_cwd()}/completed/{fileOutName}.mp3"
    output = subprocess.run(f"ffmpeg -i {fileIn} -b:a 192k {fileNameOut}", shell=True)
    return output

def YoutubeDownloader(url):
    from FW.Core.CoreDownloaders import MediaDownloaders
    return MediaDownloaders.YoutubeDownloader(url)

def GeneralDownloader(url):
    return MediaDownloaders.GeneralDownloader(url)

class SlimeManager(FairUI):
    # SlimeManager
    editFinalDirectory = None
    editAddUrl: QtWidgets.QLineEdit = None
    listUrlInQueue: QtWidgets.QListWidget = None
    listFinalDirectory: QtWidgets.QListWidget = None
    listUrlDownloaded = None
    # Converter
    convertConfig = { "type": "", "fileIn": "", "fileOut": "" }
    listConvertExploreFiles: QtWidgets.QListWidget = None
    currentConvertDirectory = None
    fileToConvert = None
    btnConvertListBack = None
    btnConvert = None
    lblInputPath = None
    lblOutputPath = None
    toggleConvertMP3: QtWidgets.QCheckBox = None
    toggleConvertMP4: QtWidgets.QCheckBox = None
    # cache
    urls_cached = []
    urls_in_general = []
    finalDirectory = OS.get_cwd()


    def __init__(self):
        super(SlimeManager, self).__init__()
        self.bind_ui(uiFilePath=uiFile)
        self.do_refresh()
        self.refresh_convert_directory()
        self.show()

    def onClick_btnYoutubeDownloader(self, item):
        url = self.editAddUrl.text()
        self.urls_cached.append(url)
        Thread.runFuncInBackground(YoutubeDownloader, arguments=url, callback=self.CallbackYoutube)

    def onClick_btnGeneralDownloader(self, item):
        url = self.editAddUrl.text()
        self.urls_in_general.append(url)
        Thread.runFuncInBackground(GeneralDownloader, arguments=url, callback=self.CallbackGeneral)

    def onClick_btnAddUrlToQueue(self, item):
        url = self.editAddUrl.text()
        if RE.contains("youtube", url):
            self.urls_cached.append(url)
            Thread.runFuncInBackground(YoutubeDownloader, arguments=url, callback=self.CallbackYoutube)
        else:
            self.urls_in_general.append(url)
            Thread.runFuncInBackground(GeneralDownloader, arguments=url, callback=self.CallbackGeneral)
        self.listUrlInQueue.addItem(url)
        self.editAddUrl.setText("")

    def onClick_btnRunUrlQueue(self, item):
        url = self.editAddUrl.text()
        self.urls_in_general.append(url)
        Thread.runFuncInBackground(GeneralDownloader, arguments=url, callback=self.CallbackGeneral)
        self.listUrlInQueue.addItem(url)
        self.editAddUrl.setText("")
        print("running download queue")

    # def onClick_listConvertExploreFiles(self, item: QtCore.QModelIndex):
    #     print("Single Click", item.row())

    def onClick_btnConvert(self, item):
        from F import FFMPEG
        if self.convertConfig["type"] == ".mp3":
            np = self.fileToConvert[:-1] + "3"
            self.lblOutputPath.setText(np)
            print("Converting to mp3")
            FFMPEG.to_mp3(self.fileToConvert)
        elif self.convertConfig["type"] == ".mp4":
            np = self.fileToConvert[:-1] + "4"
            self.lblOutputPath.setText(np)
            print("Converting to mp4")
            FFMPEG.to_mp4(self.fileToConvert)

    def onClick_btnConvertListBack(self):
        if str(self.currentConvertDirectory) == "/":
            return
        parDir = OS.get_previous_directory(self.currentConvertDirectory)
        self.refresh_convert_directory(parDir)

    def onDoubleClick_listConvertExploreFiles(self, item: QtWidgets.QListWidgetItem):
        print("Double Click", item)
        selection = item.text()
        fullPath = f"{self.currentConvertDirectory}/{selection}"
        if OS.is_directory(fullPath):
            self.refresh_convert_directory(fullPath)
        else:
            if OS.is_media_file(fullPath):
                self.fileToConvert = fullPath
                self.lblInputPath.setText(OS.get_file_name(fullPath))
                self.convertConfig["fileIn"] = fullPath
        print(fullPath)

    def onToggled_toggleConvertMP3(self, item):
        self.toggleConvertMP3.setChecked(item)
        if self.toggleConvertMP3.isChecked():
            self.toggleConvertMP4.setChecked(False)
            self.convertConfig["type"] = ".mp3"
        else:
            self.convertConfig["type"] = ""

    def onToggled_toggleConvertMP4(self, item):
        self.toggleConvertMP4.setChecked(item)
        if self.toggleConvertMP4.isChecked():
            self.toggleConvertMP3.setChecked(False)
            self.convertConfig["type"] = ".mp4"
        else:
            self.convertConfig["type"] = ""

    def CallbackGeneral(self, result):
        downloadResult = self.get_arg("result", result)
        downloadSuccess = self.get_list(0, downloadResult)
        downloadedUrl = self.get_list(1, downloadResult)
        if type(downloadedUrl) in [list]:
            downloadedUrl = self.get_list(0, downloadedUrl)

        for file in OS.get_files_in_directory():
            if str(file).endswith(".mp3"):
                OS.move_file(f"{cw_DIRECTORY}/{file}", completed_DIRECTORY)
                self.urls_cached = DICT.remove_key_value(downloadedUrl, self.urls_cached)
        self.do_refresh()

    def CallbackYoutube(self, result):
        downloadResult = self.get_arg("result", result)
        downloadSuccess = self.get_list(0, downloadResult)
        downloadedUrl = self.get_list(1, downloadResult)
        if type(downloadedUrl) in [list]:
            downloadedUrl = self.get_list(0, downloadedUrl)

        if downloadSuccess:
            temp = []
            for url in self.urls_cached:
                if url == downloadedUrl:
                    continue
                temp.append(url)
            self.urls_cached = temp
            self.listUrlInQueue.clear()
            self.listUrlDownloaded.clear()

        self.do_refresh()

    def onClick_btnMoveToFinalDirectory(self):
        try:
            self._set_finalDirectory()
            for file in OS.get_files_in_directory(completed_DIRECTORY):
                if str(file).endswith(".mp3"):
                    try:
                        if not OS.move_file(f"{completed_DIRECTORY}/{file}", self.finalDirectory):
                            print("Need to move this file to a failed folder.")
                    except Exception as e:
                        print("Failed to move file", e)
            self.urls_in_general = []
            self.do_refresh()
        except:
            print("Failed to move files.")

    def onClick_btnRefreshFolders(self):
        self.do_refresh()

    def moveDownloadedToCompleted(self):
        try:
            files_to_move = []
            for file in OS.get_files_in_directory():
                if str(file).endswith(".mp3"):
                    files_to_move.append(file)
        except:
            print("Failed to move file.")

        # for url in self.urls_cached.keys():
        #     status = self.urls_cached[url]
        #     if status == "complete":
        #         self.listUrlDownloaded.addItem(url)
        #     if status == "queued" or status == "downloading":
        #         self.listUrlInQueue.addItem(url)
        #         Thread.runFuncInBackground(dl.GeneralDownloader, arguments=url, callback=self.CallbackGeneral)

    def _set_finalDirectory(self):
        self.finalDirectory = self.editFinalDirectory.text()

    def do_refresh(self):
        try:
            self._set_finalDirectory()
            self.refresh_completed_directory()
            self.refresh_final_directory()
        except:
            print("Failed to refresh directories!")
            self.finalDirectory = OS.get_cwd()
            self.refresh_completed_directory()
            self.refresh_final_directory()

    def refresh_final_directory(self):
        self.listFinalDirectory.clear()
        for file in OS.get_files_in_directory(self.finalDirectory):
            self.listFinalDirectory.addItem(file)

    def refresh_completed_directory(self):
        self.listUrlDownloaded.clear()
        for file in OS.get_files_in_directory(completed_DIRECTORY):
            self.listUrlDownloaded.addItem(file)

    def refresh_convert_directory(self, path=completed_DIRECTORY):
        self.listConvertExploreFiles.clear()
        self.currentConvertDirectory = path
        for file in OS.get_files_in_directory(path):
            self.listConvertExploreFiles.addItem(file)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SlimeManager()
    sys.exit(app.exec())
