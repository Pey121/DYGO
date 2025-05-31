# 水印程序

这是一个使用 PyQt5 开发的水印程序，可以在 Windows 系统上运行。

## 功能

- 显示固定文字水印
- 显示实时时间
- 窗口置顶
- 鼠标穿透

## 构建

本项目使用 GitHub Actions 自动构建 Windows 可执行文件。每次推送到 main 分支时，都会自动触发构建流程。

构建完成后，可以在 Actions 页面下载生成的 exe 文件。

## 本地运行

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行程序：
```bash
python test11.py
``` 