import json
import os
import requests

os.mkdir('data')

def download(link):
    filename = link.split('/')[-1]
    r = requests.get(link, allow_redirects=True)
    open(filename, 'wb').write(r.content)

os.system('pip install discord.py')
os.system('pip install subprocess.run')

lvl = open('data/lvl.json', 'w')
lvl.write("{}")
lvl.close

balance = open('data/Money.json', 'w')
balance.write("{}")
balance.close

bm = open('data/bm.json', 'w')
bm.write("{}")
bm.close
link1 = 'https://www.dropbox.com/s/rbzbl09nwr98wkc/token.txt?dl=0'
link2 = 'https://www.dropbox.com/s/dofef1erej06bo3/%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F.txt?dl=0'
link3 = 'https://www.dropbox.com/s/2sn93fb34vbgzcc/neko.bat?dl=0'
link4 = 'https://www.dropbox.com/s/j28fx4cnm2wfbyn/lvlneko.py?dl=0'
link5 = 'https://www.dropbox.com/s/7i3i6nn7nxbc2iu/neko.py?dl=0'
link6 = 'https://www.dropbox.com/s/drofzagg9zvydrh/prstart.bat?dl=0'

download(link1)
download(link2)
download(link3)
download(link4)
download(link5)
download(link6)