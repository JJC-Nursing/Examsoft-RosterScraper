"""
This is a setup_test.py script generated by py2applet

Usage:
    python3 setup_test.py py2app
"""
import setuptools
from setuptools import setup

# import sys
# for path in sys.path:
#     print(path)

APP = ['rosterscraper_frontend.py']
DATA_FILES = [("fonts", ['fonts/BeVietnam-ExtraBold.ttf',
                         'fonts/BeVietnam-Regular.ttf',
                         'fonts/BeVietnam-SemiBold.ttf']),
              ("assets", ['assets/search_icon.png',
                          'assets/offlineRS_icon.icns'])]

PACKAGES = ['bs4', 'PyQt6']
MODULES = ['rosterscraper_backend']


OPTIONS = {'iconfile':
           'assets/offlineRS_icon.icns'
           ,
           'packages': PACKAGES,
           'includes': MODULES
           }


setup(
    name="Examsoft RosterScraper",
    version="2.0.02",
    app=APP,
    packages=setuptools.find_packages(),
    include_package_data=True,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app', "bs4", "PyQt6"],
)
