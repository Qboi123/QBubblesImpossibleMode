from qbubbles.__main__ import Main

import sys
import os


if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath("impossiblemode"))
    sys.argv.append(f"gameDir=/Users/{os.getlogin()}/Documents/qlaunch")
    from impossiblemode import __init__
    main = Main()
    main.mainloop()
