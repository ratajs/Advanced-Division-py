import re
def div(n1, n2, r = 0, rstr1 = "[", rstr2 = "]"):
  if float(n2)==float(0):
    return False
  sign = "-" if ((int(n2) >= 0) if (int(n1) < 0) else (int(n2) < 0)) else ""
  n1 = abs(float(n1))
  n2 = abs(float(n2))
  r = abs(int(r))
  def times10(nstring):
    if nstring.endswith(".0"):
      nstring = nstring[:-2]
    if(nstring=="0"):
      return "0"
    if "." in nstring and nstring.find(".")==len(nstring) - 2:
      return nstring.replace(".", "")
    if "." in nstring:
      return nstring.split(".")[0] + nstring.split(".")[1][0] + "." + nstring.split(".")[1][1:]
    return nstring + "0"
  n1string = str(n1)[:-2] if str(n1).endswith(".0") else str(n1)
  n2string = str(n2)[:-2] if str(n2).endswith(".0") else str(n2)
  while "." in n1string or "." in n2string:
    if not "." in n1string:
      n1string+= str(r)[0]
      if len(str(r)) > 1:
        r = int(str(r)[1:] + str(r)[0])
    elif "." in times10(n1string):
      n1string = times10(n1string)+str(r)[0]
      if len(str(r)) > 1:
        r = int(str(r)[1:] + str(r)[0])
    else:
      n1string = times10(n1string)
    n2string = times10(n2string)
  n1 = int(n1string)
  n2 = int(n2string)
  res = ""
  n1s = list(n1string)
  n1s1 = list(n1string.split(".")[0])
  carry = 0
  newcarry = 0
  over = False
  i = 0
  for v in n1s1:
    res+= str((int(times10(str(carry))) + int(v)) // n2)
    carry = (int(times10(str(carry))) + int(v)) % n2
    i+= 1
  if res=="":
    res = "0"
    i+= 1
  doti = i
  res+= "."
  carries = [carry]
  i+= 1
  n1s.append("")
  while True:
    if(i >= len(n1s)):
      if "rcount" in vars():
        rcount+= 1
      else:
        rcount = 0
      over = True
      n1s.append(int(list(str(r))[rcount % len(str(r))]))
    newcarry = (int(times10(str(carry))) + int(n1s[i])) % n2
    if newcarry==0 and r==0:
      res+= str((int(times10(str(carry))) + int(n1s[i])) // n2)
      return sign + re.sub("^$", "0", re.sub("^\.", "0.", res.strip("0").rstrip(".")))
    x = 0
    while x < len(carries):
      if carries[x]==newcarry and (x % len(str(r)))==((i - doti) % len(str(r))):
        res+= str((int(times10(str(carry))) + int(n1s[i])) // n2)
        return sign + re.sub("^$", "0", re.sub("^\.", "0.", re.sub("^0+", "", "".join([res[:doti + carries.index(newcarry) + 1], rstr1, res[doti + carries.index(newcarry) + 1:], rstr2]))))
      x+= 1
    res+= str((int(times10(str(carry))) + int(n1s[i])) // n2)
    carry = newcarry
    if over:
      carries.append(carry)
    i+= 1
if __name__ == "__main__":
  import sys
  if len(sys.argv) > 2:
    print(div(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 0, sys.argv[4] if len(sys.argv) > 4 else "[", sys.argv[5] if len(sys.argv) > 5 else "]"))