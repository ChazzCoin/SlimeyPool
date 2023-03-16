from PyQt6 import QtWidgets

from F import OS, DICT

from FQt.FQtBaseApp import FQtBaseApp
from UI.Variables import SlimeyPoolVariables
from completed import completed_DIRECTORY

cw_DIRECTORY = OS.get_cwd()
cwd = OS.get_cwd()
uiFile = cwd + "/SlimeManager.ui"

class SlimeyBase(FQtBaseApp, SlimeyPoolVariables):

    def __init__(self):
        super(SlimeyBase, self).__init__(uiFile=uiFile)

    def CallbackYoutube(self, result):
        downloadResult = self.get_arg("result", result)
        downloadSuccess = self.get_list(0, downloadResult)
        downloadedUrl = self.get_list(1, downloadResult)
        if type(downloadedUrl) in [list]:
            downloadedUrl = self.get_list(0, downloadedUrl)
        self.urls_cached.remove(downloadedUrl)
        self.do_refresh()

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

    def _set_finalDirectory(self):
        self.finalDirectory = self.editFinalDirectory.text()

    def refresh_final_directory(self):
        self.listFinalDirectory.clear()
        for file in OS.get_files_in_directory(self.finalDirectory):
            self.listFinalDirectory.addItem(file)

    def refresh_completed_directory(self):
        self.listUrlDownloaded.clear()
        for file in OS.get_files_in_directory(completed_DIRECTORY):
            self.listUrlDownloaded.addItem(file)

    def refresh_convert_directory(self, path=completed_DIRECTORY):
        pass
        # self.listConvertExploreFiles.clear()
        # self.currentConvertDirectory = path
        # for file in OS.get_files_in_directory(path):
        #     self.listConvertExploreFiles.addItem(file)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SlimeyBase()
    sys.exit(app.exec())