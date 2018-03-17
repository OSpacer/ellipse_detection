# ellipse_detection
Ellipse Detection

## Anaconda 
    Install Anaconda(python 3.6 version): https://www.anaconda.com/download/
    Open `Anaconda Navigator`, create a new envs which I named 'OpenCV'
    Open terminal under the new envs to install some essential libraries
    
Install OpenCV:
```Bash
conda install opencv
```
Install Qt (PyQt5 and Qt Creator):
```Bash
conda install pip
pip install pyqt5
pip install pyqt5-tools
```

## PyCharm
Install PyCharm to edit python file(or you can still use python IDIE): https://www.jetbrains.com/pycharm/

Set the python environment to Anaconda new envs(OpenCV):

    1. open Pycharm
    2. File-Settins-Project-Project Interpreter
    3. select the PATH where you install python envs, such as`C:\Users\username\Anaconda3\envs\OpenCV\python.exe`
    
Configure PyQt5 in PyCharm:
    
    Reference: https://www.jianshu.com/p/094928ac0b73
    1. '配置QtDesigner'
    2. '配置PyUIC'
