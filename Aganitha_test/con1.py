import re

def con1(para):
  result=re.sub('(\d)( dollars)',r'$\1',para)
  return result
def con2(para):
  result=re.sub('[C,P] M','CM',para)
  return result
def con3(para):
  result=re.sub('(triple) (\w)',r'\2\2\2',para)
  return result

def converter1(para):
  para=con1(para)
  para=con2(para)
  para=con3(para)
  return para
