import glob
import requests
import pathlib
import regex as re
import os
import logging as log
import urllib
import hashlib
#https://render.githubusercontent.com/render/math?math=
def ddl_svg(formula, folder):
  err = False
  pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
  to_hash = str("/latex-svg/"+str(formula).replace("\b", "b").replace("&","&amp;").replace("\\", "")[0:]+".svg").encode('utf-8')
  f = folder+"/"+hashlib.md5(to_hash).hexdigest() + ".svg"
  with open(f, 'wb') as handle:
    response = requests.get("https://latex.codecogs.com/svg.latex?"+str(formula)[0:].replace("%5C%7B", "\\{").replace("%5C%7D", "\\}"), stream=True)
    if not response.ok:
      log.error(str(response.status_code) + " : " + formula)
      log.error("https://latex.codecogs.com/svg.latex?"+urllib.parse.quote(str(formula))[0:].replace("%5C%7B", "\\{"))
      err = True
    else : 
      for block in response.iter_content(1024):
        if not block:
          break
        handle.write(block)
  if (err):
    if os.path.exists(f):
        os.remove(f)
    cont = input("Voulez-vous réessayez ?")
    if (cont == "y"):
      ddl_svg(formula, folder)

def parser(f): 
  with open(f, 'r') as file:
    data = file.read().replace('\n', '')
    tab_i = re.findall(r"\$(.*?)\$", data)
    tab = re.findall(r"\$\$(.*?)\$\$", data)
    tab_i = [x for x in tab_i if x != '']
  return tab + tab_i


def test_exist(formula, folder):
  f2 = str("/latex-svg/"+str(formula).replace("\b", "b").replace("\i", "i").replace("&","&amp;").replace("\\", "")[0:]+".svg").encode('utf-8')
  f = folder + "/"+ hashlib.md5(str("/latex-svg/"+str(formula).replace("\b", "b").replace("\i", "i").replace("&","&amp;").replace("\\", "")[0:]+".svg").encode('utf-8')).hexdigest() + ".svg"
  if (not os.path.isfile(f)):
    print("Formula : " + formula + " Downloaded")
    print(f)
    ddl_svg(formula, folder)
  else: 
    print("Formula : "+ formula + " (Skipt : Already Exist in folder)")
    print(f)
    print(f2)
    
def get_all_file():
  return glob.glob("content/**/*.md", recursive=True)

def execute(folder="./themes/amperage/static/latex-svg"):
  l_file = []
  for f in get_all_file() :
    l_file += parser(f)
  for x in l_file: 
    test_exist(x,folder)

execute()