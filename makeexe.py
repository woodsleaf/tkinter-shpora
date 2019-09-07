# coding: utf-8
'''python makeexe.py build'''
from cx_Freeze import setup, Executable

buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [Executable('example.py',
                          targetName='hello_wx.exe',
                          base=base,
                          icon='example.ico')]

excludes = ['logging', 'unittest', 'email', 'html', 'http', 'urllib', 'xml',
            'bz2', 'select']

zip_include_packages = ['collections', 'encodings', 'importlib', 'wx']

# options = dict(build_exe = buildOptions),
options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
    }
}

setup(name='hello_world',
      version='0.0.13',
      description='My Hello World App!',
      executables=executables,
      options=options)
