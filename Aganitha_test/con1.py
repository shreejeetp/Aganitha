import re

def con1(para):
  result=re.match('(\d)( dollars)',para)
  para=para.replace(result.string,'$'+result.group(1))
  return para
def con2(para):
  result=re.match('C M',para)
  if(result!=None):
    para=para.replace(result.string,'CM')
  return para
def con3(para):
  result=re.match('(triple) (/w)',para)
  if(result!=None):
    para=para.replace(result.string,result.group(2)*3)
  return para
def converter1(para):
  para=con1(para)
  para=con2(para)
  para=con3(para)
  return para
