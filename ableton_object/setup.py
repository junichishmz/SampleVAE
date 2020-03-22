"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""
import sys
sys.setrecursionlimit(5000)

from setuptools import setup

APP = ['main.py']
DATA_FILES = []

OPTIONS = {'argv_emulation':True,
'plist':{
'PyRuntimeLocations':[
'@executable_path/../Frameworks/libpython3.6m.dylib',
'/Users/junichishimizu/anaconda3/lib/libpython3.6m.dylib'
]
}}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
