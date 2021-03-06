import os
from python import moe_utils
import shutil

# recompile files
os.system('npm install --no-save --no-audit')
os.system('npm update --no-save')
os.system('npm run build')
moe_utils.compile_pyc()
# os.system('python setup.py build')
# print('### fix scipy ####')
# os.rename('./build/exe.win-amd64-3.7/lib/scipy/spatial/cKDTree.cp37-win_amd64.pyd','./build/exe.win-amd64-3.7/lib/scipy/spatial/ckdtree.cp37-win_amd64.pyd')

# delete deprecated files

moe_utils.delete_files('../build/model')
moe_utils.delete_files('../build/pyc')
moe_utils.delete_files('../build/site-packages')
moe_utils.delete_files('../build/ffmpeg')
moe_utils.delete_files('../build/static')
moe_utils.delete_files('../build/templates')
moe_utils.delete_files('../build/manifest.json')
moe_utils.delete_files('../build/update_log.txt')
moe_utils.delete_files('../build/download')
moe_utils.delete_files('../build/.user')
# copy files
shutil.copytree(src='./model',dst='../build/model')
shutil.copytree(src='./pyc',dst='../build/pyc')
shutil.copytree(src='./site-packages',dst='../build/site-packages')
shutil.copytree(src='./ffmpeg',dst='../build/ffmpeg')
shutil.copytree(src='./static',dst='../build/static')
shutil.copytree(src='./templates',dst='../build/templates')
shutil.copy(src='./manifest.json',dst='../build/manifest.json')
shutil.copy(src='./update_log.txt',dst='../build/update_log.txt')