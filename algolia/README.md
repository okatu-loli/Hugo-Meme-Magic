# 简体中文版本：

## 脚本介绍

本目录下的脚本基于 `Python` 编写，用于自动化生成和上传 `algolia.json` 至 `Algolia` 平台。虽然脚本基于 `Meme` 主题定制，但大多数代码可通用于其他 `Hugo` 主题或其他使用场景。根据需要，可以酌情修改代码。

## 环境要求

- 操作系统: Windows、MacOS 或 Linux
- Python环境：Python 3.6 或以上版本，包含 pip 包管理器
- 已建立的博客系统，并可以访问其根目录
- 具备基本的命令行操作技能，包括文件的移动、重命名以及在命令行中执行命令等
- 对于 config.ini 文件中的参数设置，你需要具备一定的配置知识，能够根据你的实际情况进行适当的调整

## 操作步骤

1. 将本目录下的main.py文件、config.ini.example文件和py文件夹移动至博客根目录
2. 重命名config.ini.example为config.ini，并填写相关参数
3. 在博客根目录打开终端，安装相关依赖
    ```python
    $ pip install algoliasearch
    ```
4. 执行以下命令
    ```python
    $ python main.py
    ```
5. 根据控制台日志判断是否执行成功

# English version

## Script Introduction
The script in this directory is written in `Python` and is used to automate the generation and upload of `algolia.json` to the `Algolia` platform. Although the script is customized for the `Meme` theme, most of the code can be used in other `Hugo` themes or different scenarios. You can modify the code as needed.

## System Requirements

- Operating System: Windows, MacOS, or Linux
- Python Environment: Python 3.6 or above, including the pip package manager
- Established blog system accessible in its root directory
- Basic command line operation skills, including moving and renaming files, and executing commands in the command line
- Some configuration knowledge to adjust the parameters in the config.ini file according to your specific circumstances

## Steps

1. Move the `main.py` file, `config.ini.example` file, and `py` folder from this directory to the root directory of your blog.
2. Rename `config.ini.example` to `config.ini` and fill in the relevant parameters.
3. Open a terminal in the root directory of your blog and install the required dependencies by running the following command:
    ```shell
    $ pip install algoliasearch
    ```
4. Execute the following command:
    ```python
    $ python main.py
    ```
5. Check the console logs to determine if the execution was successful.