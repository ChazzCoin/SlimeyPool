from setuptools import setup
import sys

# from cx_Freeze import setup, Executable

# executables = [Executable('App.py')]
# base = None
# if sys.platform == "win32":
#     base = "Win32GUI"
#
# executables = [Executable("App.py", base=base)]
#
# setup(
#     name = "MyApp",
#     version = "0.1",
#     description = "My PyQt6 GUI application",
#     executables = executables
# )
# hdiutil create -volname "App" -srcfolder "App.app" -ov -format UDZO "App.dmg"
APP = ['run.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True,}

from setuptools import setup, find_packages
import os

current = os.getcwd()

setup(
    name='SlimeyPool',
    version='0.0.1',
    description='pyQt6 plus Qt Designer Support Framework',
    url='https://github.com/chazzcoin/FairQt',
    author='ChazzCoin',
    author_email='chazzcoin@gmail.com',
    license='BSD 2-clause',
    options={'py2app':OPTIONS},
    packages=find_packages(),
    package_dir={'res': 'FQt'},
    package_data={
        'FQt': ['FTemplates/*.ui']
    },
    install_requires=['py2app', 'faircore', 'fairqt', 'pytube', 'youtube-dl', 'youtube-search-python', 'fairweb',
                      'pyqt6', 'pyqt6-sip', 'pyqt6-qt6'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)