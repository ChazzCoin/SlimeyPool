from F import OS
from PyQt6 import QtWidgets
from F.TYPE.List import fist


class SlimeyPoolVariables:
    # SlimeManager
    editFinalDirectory = None
    editAddUrl: QtWidgets.QLineEdit = None
    listUrlInQueue: QtWidgets.QListWidget = None
    listFinalDirectory: QtWidgets.QListWidget = None
    listUrlDownloaded = None
    # Converter
    convertConfig = {"type": "", "fileIn": "", "fileOut": ""}
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
    urls_cached = fist()
    urls_in_general = []
    finalDirectory = OS.get_cwd()