@echo off

set ip=%1
set port=%2
set basetitle=tcping - %ip%:%port%

title %basetitle%

echo tcping %ip%������%port%�˿�TCPЭ��ɴ��Բ���
echo �ڱ������У����ǻ᲻�ϲ���%ip%:%port%�Ƿ�ɴ�����ɴ�����ʾ��No Response����
echo ����ϸ�۲��·������Ϣ��

.\tcping.exe -t %ip% %port%

pause