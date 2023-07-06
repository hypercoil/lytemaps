import os
from setuptools import setup
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import versioneer

if __name__ == "__main__":
    setup(name='minnmaps',
          version=versioneer.get_version(),
          cmdclass=versioneer.get_cmdclass())
