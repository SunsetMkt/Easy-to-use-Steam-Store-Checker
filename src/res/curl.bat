@echo off

set domain=%1
set ip=%2
set port=%3
if %3 == 80 (set protocol=http://)
if %3 == 443 (set protocol=https://)
set url=%protocol%%domain%
set basetitle=curl - %domain%����Ϊ%ip%

title %basetitle%

echo curl %ip%��վ���ʲ���
echo �ڱ������У����ǻ��Է���%domain%�����峢�Է��ʷ�����%ip%��URLΪ%url%������%domain%������Ϊ%ip%��
echo �밴�����������һ��
pause

:curl
title %basetitle% - ������

.\curl.exe -I -k -v --resolve %domain%:%port%:%ip% %url%
set lastreturn=%errorlevel%

title %basetitle% - �������

if %lastreturn% == 0 (echo ����ɹ�) else (echo ����ʧ��)

echo �밴��������ٲ���һ��
pause

goto curl
