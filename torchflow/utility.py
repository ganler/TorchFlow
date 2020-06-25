from pip_module_scanner.scanner import Scanner, ScannerException
import os

def setup_pip_env(path):
    try:
        scanner = Scanner(path)
        scanner.run()
        for lib in scanner.libraries_found:
            os.system(f'python3 -m pip install {lib.key}=={lib.version}')
    except ScannerException as e:
        print("Error: %s" % str(e))