import os
from zipapp import create_archive


class QCompiler(object):
    def __init__(self, mod_path, name, compressed=True, main_class="Main"):
        mod_path = mod_path.replace('\\', '/')
        while mod_path.endswith("/"):
            mod_path = mod_path[:-1]
        if not os.path.exists("build/"):
            os.makedirs("build/")
        create_archive(source=mod_path, target=f"build/{name}", compressed=compressed)
