:: curl.bat
:: 用于调用curl.exe
:: https://github.com/lwd-temp/Easy-to-use-Steam-Store-Checker
:: 参数： [域名] [IP] [端口]
:: 参数不全会报错
:: 协议会根据端口80或443自动选择，如果两个都不是则默认为http://
:: %errorlevel% 表示上一个命令的返回值
@echo off
chcp 936 > nul
:: 设置编码为GBK，避免在非中文Windows下的中文乱码

set domain=%1
set ip=%2
set port=%3
set protocol=http://
if %3 == 80 (set protocol=http://)
if %3 == 443 (set protocol=https://)
set url=%protocol%%domain%
set basetitle=curl - %domain%解析为%ip%

title %basetitle%

echo curl %ip%网站访问测试
echo 在本测试中，我们会以访问%domain%的名义尝试访问服务器%ip%。URL为%url%，其中%domain%被解析为%ip%。
echo 请按下任意键测试一次
pause > nul

:curl
title %basetitle% - 请求中

.\curl.exe -I -k -v --resolve %domain%:%port%:%ip% %url%
set lastreturn=%errorlevel%

title %basetitle% - 请求结束

if %lastreturn% == 0 (echo 请求成功) else (echo 请求失败)

echo 请按下任意键再测试一次
pause > nul

goto curl
