from PyQt6 import QtWidgets
from F import OS
from UI.SlimeyBase import SlimeyBase
from completed import completed_DIRECTORY
from failed import failed_DIRECTORY

cw_DIRECTORY = OS.get_cwd()
# downloaded_FILE = lambda fileName: f"{cw_DIRECTORY}/{fileName}"
# completed_DIRECTORY = f"{cw_DIRECTORY}/completed"
# failed_DIRECTORY = f"{cw_DIRECTORY}/failed"

class SlimeyOnClicks(SlimeyBase):

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

    def onClick_btnMoveToFinalDirectory(self):
        try:
            self._set_finalDirectory()
            for file in OS.get_files_in_directory(completed_DIRECTORY):
                if str(file).endswith(".mp3") or str(file).endswith(".mp4"):
                    try:
                        if not OS.move_file(f"{completed_DIRECTORY}/{file}", self.finalDirectory):
                            print("Need to move this file to a failed folder.")
                            OS.move_file(f"{completed_DIRECTORY}/{file}", failed_DIRECTORY)
                    except Exception as e:
                        print("Failed to move file", e)
            self.urls_in_general = []
            self.do_refresh()
        except:
            print("Failed to move files.")

    def onClick_btnRefreshFolders(self):
        self.do_refresh()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SlimeyOnClicks()
    sys.exit(app.exec())