#coding=utf-8
#!/usr/bin/python
import os

def open_app(app_dir):
    os.startfile(app_dir)

if __name__ == '__main__':
    app_dir = r'E:\软件安装\Sublime Text 3 中文优化版\Sublime Text 3 中文优化版\sublime_text.exe'
    open_app(app_dir)