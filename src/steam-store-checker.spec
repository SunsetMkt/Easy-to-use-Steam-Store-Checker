# -*- mode: python ; coding: utf-8 -*-

# GBK & LF2CRLF
def LF2CRLF(file_path):
    WINDOWS_LINE_ENDING = b'\r\n'
    UNIX_LINE_ENDING = b'\n'
    with open(file_path, 'rb') as open_file:
        content = open_file.read()
    content = content.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)
    with open(file_path, 'wb') as open_file:
        open_file.write(content)

def altLF2CRLF(infile, outfile):
    with open(infile, 'r',encoding="utf-8") as open_file:
        content = open_file.readlines()
    with open(outfile, 'w',encoding="gbk",newline="\r\n") as open_file:
        open_file.writelines(content)

# LF2CRLF(os.path.join("res", "curl.bat"))
# LF2CRLF(os.path.join("res", "tcping.bat"))
altLF2CRLF(os.path.join("res", "src", "curl.bat"), os.path.join("res", "curl.bat"))
altLF2CRLF(os.path.join("res", "src", "tcping.bat"), os.path.join("res", "tcping.bat"))

# Pack Res Files
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
