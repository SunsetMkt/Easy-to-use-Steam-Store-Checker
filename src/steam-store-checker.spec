# -*- mode: python ; coding: utf-8 -*-

# UTF-8 LF转GBK CRLF
def UTF8LF2GBKCRLF(infile, outfile):
    with open(infile, 'r',encoding="utf-8") as open_file:
        content = open_file.readlines()
    with open(outfile, 'w',encoding="gbk",newline="\r\n") as open_file:
        open_file.writelines(content)

UTF8LF2GBKCRLF(os.path.join("res", "src", "curl.bat"), os.path.join("res", "curl.bat"))
UTF8LF2GBKCRLF(os.path.join("res", "src", "tcping.bat"), os.path.join("res", "tcping.bat"))

# 打包资源文件到pak.zip
# 需要注意这样压缩后，压缩文件内的文件结构是res/，不是散装
import os
import zipfile
with zipfile.ZipFile(os.path.join("res", "pak.zip"), "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write(os.path.join("res", "curl.exe"))
    zf.write(os.path.join("res", "tcping.exe"))
    zf.write(os.path.join("res", "curl.bat"))
    zf.write(os.path.join("res", "tcping.bat"))


block_cipher = None


a = Analysis(['steam-store-checker.py'],
             pathex=['C:\\path-to\\Easy-to-use-Steam-Store-Checker\\src'],
             binaries=[],
             datas=[('.\\\\res\\\\pak.zip', '.\\')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='steam-store-checker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
