import json

from PyQt6 import QtWidgets

from F import RE
from F.CLASS import Thread
from UI.SlimeyOnClicks import SlimeyOnClicks
from SlimeyTools import Downloaders as dl
from SlimeyTools import YoutubeSearch

class SlimeyDownloading(SlimeyOnClicks):

    """ Search YouTube """
    def onClick_btnSearchYoutube(self, item):
        self.listSearchResults.clear()
        searchTerm = self.editSearchYoutube.text()
        results = YoutubeSearch.search_youtube(searchTerm)
        for item in results:
            self.listSearchResults.addItem(str(item))

    def onDoubleClick_listSearchResults(self, item):
        selection_dict = self.parse_string_to_dict(item.text())
        print(selection_dict)
        url = selection_dict['link']
        Thread.runFuncInBackground(dl.YoutubeDownloader, arguments=url, callback=self.CallbackYoutube)
        self.listSearchResults.clear()

    def parse_string_to_dict(self, input_str):
        import ast
        try:
            parsed_dict = ast.literal_eval(input_str)
            return parsed_dict
        except (SyntaxError, ValueError):
            print("Error: Unable to parse the given string.")
            return None

    """ Downloader """
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