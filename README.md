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

### 下载Release构建

在页面中占到Releases，点击标记Latest的最近一次发布，在Assets中找到steam-store-checker.exe，点击下载。

### 下载GitHub Action构建（需要登录GitHub账号）

点击上方Actions，寻找最靠近上方的有绿色√标记的构建，点击进入，在Artifacts下找到steam-store-checker，点击下载。

## 采用的工具

* curl
* tcping

## 开源许可

使用GNU General Public License v3.0协议开源发布

## 更新日志

v0.0.3-alpha 优化构建流程

v0.0.2-alpha 无明显更新

v0.0.1-alpha 基本完成，自动化构建

## TODO

* 把目前用批处理实现的部分用Python重写
* 想办法让pyinstaller打包后的exe能打开多个Python命令行
