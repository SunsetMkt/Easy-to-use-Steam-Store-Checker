# Easy-to-use-Steam-Store-Checker

易于使用的Steam商店443端口干扰验证工具

[lwd-temp/steam-store-checker](https://github.com/lwd-temp/steam-store-checker) 测试脚本打包优化版

## 功能

* 常规访问store.steampowered.com
* 访问store.steampowered.com，但将其IP解析为百度日本服务器
* 访问fuck.steampowered.com，但将其IP解析为Steam商店服务器

## 获取应用程序

### 从源码构建

下载此代码库，在Windows下安装Python 3版本及pyinstaller，确保pyinstaller可执行位置在%PATH%内。

运行build.bat，打包后的程序在src\dist\内。

尽可能不要修改spec文件，这个文件是定制化的。

（适配架构取决于操作系统，代码库中附带的工具可执行文件是x86）

### 下载Release构建

在页面中占到Releases，点击标记Latest的最近一次发布，在Assets中找到steam-store-checker.exe，点击下载。

（这里提供的是x64版本）

### 下载GitHub Action构建（需要登录GitHub账号）

点击上方Actions，寻找最靠近上方的有绿色√标记的构建，点击进入，在Artifacts下找到steam-store-checker，点击下载。

（这里提供的是x64版本）

### 直接从源码运行

**不建议**，下载代码库后运行一次build.bat便会自动生成运行所需的资源文件，这时便可从源码直接运行steam-store-checker.py。亦可参考本项目的定制化构建流程自行补全缺失的资源文件。

（代码库中附带的工具可执行文件是x86）

## 采用的工具

* [curl.exe](https://curl.se/windows/)
* [tcping.exe](https://elifulkerson.com/projects/tcping.php)

它们的开源许可详见LICENSE

## 开源许可

使用GNU General Public License v3.0协议开源发布

不包括二进制文件

## 本项目的定制化构建流程

详见steam-store-checker.spec。

* 将\src\res\src下的两个UTF-8编码的批处理文件源码转换为在\src\res下的GBK编码、CRLF换行批处理文件（解决中文Windows下UTF-8批处理乱码及Git提交时会自动将CRLF转换成LF导致批处理解析错误的问题）
* 将\src\res下的两个bat和两个exe文件打包成\src\res\pak.zip，只有此压缩文件会被PyInstaller打包。

## 更新日志

v0.1.1 更新curl二进制版本

v0.1.0 发布

v0.0.6-beta 补充注释，整理代码

v0.0.5-alpha 修复错误的自动处理路径 自动提交Release

v0.0.4-alpha 当在代码库中直接运行时显示警告

v0.0.3-alpha 优化构建流程

v0.0.2-alpha 无明显更新

v0.0.1-alpha 基本完成，自动化构建

## TODO

* 把目前用批处理实现的部分用Python重写
* 想办法让pyinstaller打包后的exe能打开多个Python命令行
* ~~打包类似traceroute~~不建议，tracetcp/tcproute需要WinPcap驱动支持，Windows提供的tracert不支持TCP协议测试
