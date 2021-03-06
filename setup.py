from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="paxes",
    version="0.1.0",
    license="MIT/X11",
    author="Yuhang (Steven) Wang",
    author_email="stevenyhw.project@gmail.com",
    packages=[
        "atomicblock",
        "atomicblock.io",
        "atomicblock.io.read",
    ],
    ext_modules=cythonize("**/*.pyx"),
    install_requires=[
        "ProDy",
    ],
)
