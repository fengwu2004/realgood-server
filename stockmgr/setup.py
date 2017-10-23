from cx_Freeze import setup, Executable

build_exe_options = {}

setup(
    name = 'pack',
    version = '0.1',
    options = {'build_exe': build_exe_options},
    executables = [Executable('stockstoremgr.py', base = None)]
)