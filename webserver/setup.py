from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["jwt", 'appdirs', 'packaging', 'tornado']}

setup(
    name = 'pack',
    version = '0.1',
    options = {'build_exe': build_exe_options},
    executables = [Executable('main.py', base = None)]
)