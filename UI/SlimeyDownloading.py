from PyQt6 import QtWidgets

from F import RE
from F.CLASS import Thread
from UI.SlimeyOnClicks import SlimeyOnClicks
from SlimeyTools import Downloaders as dl

class SlimeyDownloading(SlimeyOnClicks):

    def onClick_btnYoutubeDownloader(self, item):
        url = self.editAddUrl.text()
        self.urls_cached.append(url)
        Thread.runFuncInBackground(dl.YoutubeDownloader, arguments=url, callback=self.CallbackYoutube)

    def onClick_btnGeneralDownloader(self, item):
        url = self.editAddUrl.text()
        self.urls_in_general.append(url)
        Thread.runFuncInBackground(dl.GeneralDownloader, arguments=url, callback=self.CallbackGeneral)

    def onClick_btnAddUrlToQueue(self, item):
        url = self.editAddUrl.text()
        if RE.contains("youtube", url):
            self.urls_cached.append(url)
            Thread.runFuncInBackground(dl.YoutubeDownloader, arguments=url, callback=self.CallbackYoutube)
        else:
            self.urls_in_general.append(url)
            Thread.runFuncInBackground(dl.GeneralDownloader, arguments=url, callback=self.CallbackGeneral)
        self.listUrlInQueue.addItem(url)
        self.editAddUrl.setText("")

    def onClick_btnRunUrlQueue(self, item):
        url = self.editAddUrl.text()
        self.urls_in_general.append(url)
        Thread.runFuncInBackground(dl.GeneralDownloader, arguments=url, callback=self.CallbackGeneral)
        self.listUrlInQueue.addItem(url)
        self.editAddUrl.setText("")
        print("running download queue")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SlimeyDownloading()
    sys.exit(app.exec())