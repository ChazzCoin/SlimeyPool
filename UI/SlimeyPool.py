from PyQt6 import QtWidgets
from F import OS
from UI.SlimeyDownloading import SlimeyDownloading


class SlimeyPool(SlimeyDownloading):

    def init(self):
        self.refresh_convert_directory()

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

    def moveDownloadedToCompleted(self):
        try:
            files_to_move = []
            for file in OS.get_files_in_directory():
                if str(file).endswith(".mp3"):
                    files_to_move.append(file)
        except:
            print("Failed to move file.")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SlimeyPool()
    sys.exit(app.exec())

