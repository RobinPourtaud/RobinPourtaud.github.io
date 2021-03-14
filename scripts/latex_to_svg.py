import glob
import requests
import pathlib
import regex as re
import time
import os
import logging as log
import urllib
def ddl_svg(formula, folder):
  err = False
  pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
  f = folder+"/"+urllib.parse.quote(str(formula).replace("\\", ""))[0:] + ".svg"
  with open(f, 'wb') as handle:
    response = requests.get("https://latex.codecogs.com/svg.latex?"+urllib.parse.quote(str(formula))[0:], stream=True)
    if not response.ok:
      log.error(str(response.status_code) + " : " + formula)
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
    if (not os.path.isfile(folder + "/"+ urllib.parse.quote(str(formula).replace("\\", ""))[0:] + ".svg")):
      log.info("Formula : " + formula + " Downloaded")
      ddl_svg(formula, folder)
    else: 
      log.info("Formula : "+ formula + "Skipt (Already Exist in folder)")
    
def get_all_file():
  return glob.glob("*.md")

def execute(folder="latex-svg"):
  l_file = []
  for f in get_all_file() :
    l_file += parser(f)
  for x in l_file: 
    test_exist(x,folder)


execute()