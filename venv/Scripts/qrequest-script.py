#!D:\PyCharmDev\currency-names\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'qrequest==0.1.12','console_scripts','qrequest'
__requires__ = 'qrequest==0.1.12'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('qrequest==0.1.12', 'console_scripts', 'qrequest')()
    )
