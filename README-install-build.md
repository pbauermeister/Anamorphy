# INSTALLING AND BUILDING ON OSX

Macport or Homebrew? Macport. Here is why:
- homebrew: issues compiling wxpython. Cannot be solved easily.
- macports: issue with py2app. Can be solved by installing macports from source in alternate prefix.


## A. Installing Macport from sources

Why from source? Reason: issue with py2app:
http://stackoverflow.com/questions/13131024/py2app-error-for-opencv-macports-app-how-to-compile-opencv-with-headerpad-max-i

1. Download macport source from https://distfiles.macports.org/MacPorts/
2. expand archive, and do:

   ``./configure --prefix=/opt/localdepth/localdepth/localdepth/localdepth/local && make && sudo make install``
3. Adjust your PATH to contain \<prefix\>/bin, \<prefix\>/sbin, and MANPATH to contain \<prefix\>/share/man.


## B. Installing Python 2.7

```
sudo port install python27
sudo port select --set python python27
```

## C. Installing needed stuff using Macport

```
sudo port install py27-wxpython-3.0 py27-numpy py27-pil py27-reportlab py27-simplejson
```

## D. Building the app using py2app

```
sudo port install py27-py2app
./build_osx.sh
```


# INSTALLING AND BUILDING ON DEBIAN

## A. Dependencies

- Python
- Numpy
- wxPython
- ReportLab
- SimpleJSON

```
sudo apt-get install python-numpy python-stdeb pep8 python-wxgtk2.8 python-all build-essential
./build_debian.sh
```


# BUILDING FOR WINDOWS

Install:
- Python 2.7
- InnoSetup
- py2exe
- wxPython

- GCC https://github.com/develersrl/gccwinbinaries
- easy_install https://pypi.python.org/pypi/setuptools#windows-simplified
- c:\Python27\Scripts\easy_install.exe reportlab

- Get http://www.dll-files.com/dllindex/dll-files.shtml?msvcr71
  and copy into c:\win

- numpy: copy msvcr71.dll into numpy dir, and build numpy
- ``c:\Python27\Scripts\pip.exe install "numpy-1.9.2rc1+mkl-cp34-none-win32.whl"``
