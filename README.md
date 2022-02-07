# Easy-to-use-Steam-Store-Checker

易于使用的Steam 商店 store.steampowered.com 疑似 443 端口被干扰验证工具

[lwd-temp/steam-store-checker](https://github.com/lwd-temp/steam-store-checker) 测试脚本打包优化版


## 获取应用程序
### 从源码构建

下载此代码库，在Windows下安装Python 3版本及pyinstaller，确保pyinstaller可执行位置在%PATH%内。

运行build.bat，打包后的程序在src\dist\内。

### 下载GitHub Action的构建

点击上方Actions，寻找最靠近上方的有绿色√标记的构建，点击进入，在Artifacts下找到steam-store-checker，点击下载。

## TODO

* 把目前用批处理实现的部分用Python重写
* 想办法让pyinstaller打包后的exe能打开多个Python命令行
* ~~解决在GBK编码的Windows命令行环境下使用UTF8编码批处理中文乱码~~
* ~~因为在wine环境下打包，就算用GBK编码保存bat，Action提供的还是乱码~~
* 找到了个hack，想办法在不用hack的情况下解决问题