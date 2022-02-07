cd src\res
python pack.py
cd ..
pyinstaller -F steam-store-checker.py --add-data ".\\res\\*;.\\"