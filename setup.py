from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy
import os
import imp

VERSION = imp.load_source('version', os.path.join('.', 'darkflow', 'version.py'))
VERSION = VERSION.__version__

if os.name == 'nt':
    ext_modules = [
        Extension("darkflow.cython_utils.nms",
                  sources=["darkflow/cython_utils/nms.pyx"],
                  include_dirs=[numpy.get_include()]
        ),
        Extension("darkflow.cython_utils.cy_yolo2_findboxes",
                  sources=["darkflow/cython_utils/cy_yolo2_findboxes.pyx"],
                  include_dirs=[numpy.get_include()]
        ),
        Extension("darkflow.cython_utils.cy_yolo_findboxes",
                  sources=["darkflow/cython_utils/cy_yolo_findboxes.pyx"],
                  include_dirs=[numpy.get_include()]
        )
    ]

# ... (rest of the os.name conditions remain unchanged)

setup(
    version=VERSION,
    name='darkflow',
    description='Darkflow',
    license='GPLv3',
    url='https://github.com/thtrieu/darkflow',
    packages=find_packages(),
    scripts=['flow'],
    ext_modules=cythonize(ext_modules, include_path=['darkflow/cython_utils'])
)