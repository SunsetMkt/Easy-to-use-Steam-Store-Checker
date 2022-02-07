import zipfile

with zipfile.ZipFile("pak.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write("curl.exe")
    zf.write("tcping.exe")
    zf.write("curl.bat")
    zf.write("tcping.bat")