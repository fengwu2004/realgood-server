from cx_Freeze import setup, Executable
import sys

build_exe_options = {"packages": ["jwt", 'appdirs', 'packaging', 'tornado', 'openpyxl', 'pymongo'], 'path':sys.path + [sys.path[0] + '/analyse', sys.path[0] + '/webserver', sys.path[0] + '/data', sys.path[0] + '/stockmgr']}

print(build_exe_options['path'])

setup(
    name = 'pack',
    version = '0.1',
    options = {'build_exe': build_exe_options},
    executables = [Executable('main.py', base = None)]
)