import re

def div(n1, n2, minstr = "-", decstr = ".", rstr1 = "[", rstr2 = "]"):
	(n1, n2) = (str(n1), str(n2))

	if len(n1)==0 or len(n2)==0 or re.match("^\\d*$", minstr) or re.match("^\\d*$", decstr) or re.match("^\\d*$", rstr1) or re.match("^\\d+$", rstr2):
		return None

	nre = "^("+re.escape(minstr)+")?\\d*("+re.escape(decstr)+"\\d*("+re.escape(rstr1)+"\\d*"+re.escape(rstr2)+")?)?$"

	if not re.match(nre, n1) or not re.match(nre, n2):
		return None

	neg = False
	if n1.startswith(minstr):
		n1 = n1[len(minstr):]
		neg = True
	if n2.startswith(minstr):
		n2 = n2[len(minstr):]
		neg = not neg

	sign = minstr if neg else ""

	n1 = n1.replace(decstr, ".", 1)
	n2 = n2.replace(decstr, ".", 1)

	if n1[0]==".":
		n1 = "0"+n1

	if n2[0]==".":
		n2 = "0"+n2

	r1 = re.search(re.escape(rstr1)+"(.+)"+re.escape(rstr2), n1[:n1.index(".") + 1]) if rstr1 in n1 else None
	r1 = "0" if r1 is None else r1.group(1)
	if r1!="0":
		n1 = n1[:n1.index(".") + n1[n1.index(".") + 1:].index(rstr1) + 1]
	r2 = re.search(re.escape(rstr1)+"(.+)"+re.escape(rstr2), n2[:n1.index(".") + 1]) if rstr1 in n2 else None
	r2 = "0" if r2 is None else r2.group(1)
	if r2!="0":
		n2 = n2[:n2.index(".") + n2[n2.index(".") + 1:].index(rstr1) + 1]


	if n2=="0" and re.match("^[0\\.]+$", r2):
		return None
	if n1=="0" and re.match("^[0\\.]+$", r1):
		return "0"

	if r2!="0":
		n1m = n1.replace(".", "", 1)
		n2m = n2.replace(".", "", 1)

		n1mc = int(n1m+str(r1)) - int(n1m)
		n2mc = int(n2m+str(r2)) - int(n2m)

		if "." in n1:
			m1 = 10 ** (len(n1) - n1.index(".") - 1 + len(str(r1))) - 10 ** (len(n1) - n1.index(".") - 1)
		else:
			m1 = 10 ** len(str(r1)) - 1

		if "." in n2:
			m2 = 10 ** (len(n2) - n2.index(".") - 1 + len(str(r2))) - 10 ** (len(n2) - n2.index(".") - 1)
		else:
			m2 = 10 ** len(str(r2)) - 1

		return sign+div(n1mc * m2, m1 * n2mc, minstr, decstr, rstr1, rstr2)

	def times10(nstring):
		if nstring.endswith(".0"):
			nstring = nstring[:-2]
		if(nstring=="0"):
			return "0"
		if "." in nstring and nstring.find(".")==len(nstring) - 2:
			return nstring.replace(".", "")
		if "." in nstring:
			return nstring.split(".")[0]+nstring.split(".")[1][0]+"."+nstring.split(".")[1][1:]
		return nstring + "0"

	while "." in n2:
		if "." not in n1:
			n1+= str(r1)[0]
			if len(str(r1)) > 1:
				r1 = int(str(r1)[1:]+str(r1)[0])
		else:
			n1= times10(n1)
		n2= times10(n2)
	n2i = int(n2)
	res = ""
	n1s = list(n1)
	n1s1 = list(n1.split(".")[0])
	carry = 0
	newcarry = 0
	over = False
	x = 0
	for v in n1s1:
		res+= str((int(times10(str(carry))) + int(v)) // n2i)
		carry = (int(times10(str(carry))) + int(v)) % n2i
		x+= 1
	if res=="":
		res = "0"
		x+= 1
	res+= "."
	carries = []
	x+= 1
	rcount = -1
	if "." not in n1s:
		n1s.append(".")
	while True:
		if(x >= len(n1s)):
			rcount+= 1
			over = True
			n1s.append(int(list(str(r1))[rcount % len(str(r1))]))
		newcarry = (int(times10(str(carry))) + int(n1s[x])) % n2i
		if over:
			if newcarry==0 and r1=="0":
				res+= str((int(times10(str(carry))) + int(n1s[x])) // n2i)
				return sign+re.sub("^$", "0", re.sub("^\\.", "0.", res.strip("0").rstrip("."))).replace(".", decstr, 1)
			y = 0
			while y < len(carries):
				if carries[y]==newcarry and (y % len(str(r1)))==((rcount + 1) % len(str(r1))):
					res+= str((int(times10(str(carry))) + int(n1s[x])) // n2i)
					result = sign+re.sub("^$", "0", re.sub("^\\.", "0.", re.sub("^0+", "", res[:x - rcount + y]+"["+res[x - rcount + y:]+"]")))
					if result[result.index("[") - 1]==result[result.index("]") - 1]:
						result = result[:result.index("[") - 1]+"["+result[result.index("[") - 1]+result[result.index("[")+1:result.index("]") - 1]+"]"
					if result.index("]")==result.index("[") + 3 and result[result.index("[") + 1]==result[result.index("[") + 2]:
						result = result[:result.index("[") + 2]+"]"
					return result.replace(".", decstr, 1).replace("[", rstr1, 1).replace("]", rstr2, 1)
				y+= 1
		res+= str((int(times10(str(carry))) + int(n1s[x])) // n2i)
		if over:
			carries.append(carry)
		carry = newcarry
		x+= 1

if __name__=="__main__":
	import sys

	match len(sys.argv):
		case 7:
			print(div(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]) or "Error")
		case 6:
			print(div(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], "") or "Error")
		case 5:
			print(div(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "[", "]") or "Error")
		case 4:
			print(div(sys.argv[1], sys.argv[2], sys.argv[3], ".", "[", "]") or "Error")
		case 3:
			print(div(sys.argv[1], sys.argv[2], "-", ".", "[", "]") or "Error")
		case _:
			print("Usage: python3 "+sys.argv[0]+" n1 n2 [minch [decch [rch1 [rch2]]]]")
