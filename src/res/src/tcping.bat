:: tcping.bat
:: 用于调用tcping.exe
:: https://github.com/lwd-temp/Easy-to-use-Steam-Store-Checker
:: 参数： [IP] [端口]
:: 参数不全会报错
@echo off
chcp 936 > nul
:: 设置编码为GBK，避免在非中文Windows下的中文乱码

set ip=%1
set port=%2
set basetitle=tcping - %ip%:%port%

title %basetitle%

echo tcping %ip%服务器%port%端口TCP协议可达性测试
echo 在本测试中，我们会不断测试%ip%:%port%是否可达。若不可达，则会提示“No Response”。
echo 请仔细观察下方输出信息。

.\tcping.exe -t %ip% %port%

pause > nul