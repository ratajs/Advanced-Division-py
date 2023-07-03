import re

def div(n1, n2, r1 = 0, rstr1 = "[", rstr2 = "]"):
	if float(n2)==float(0):
		return False
	sign = "-" if ((float(n2) >= 0) if (float(n1) < 0) else (float(n2) < 0)) else ""
	n1 = abs(float(n1))
	n2 = abs(float(n2))
	r1 = abs(int(r1))

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
	while "." in n2string:
		if "." not in n1string:
			n1string+= str(r1)[0]
			if len(str(r1)) > 1:
				r1 = int(str(r1)[1:] + str(r1)[0])
		else:
			n1string = times10(n1string)
		n2string = times10(n2string)
	n1 = float(n1string)
	n2 = int(n2string)
	res = ""
	n1s = list(n1string)
	n1s1 = list(n1string.split(".")[0])
	carry = 0
	newcarry = 0
	over = False
	x = 0
	for v in n1s1:
		res+= str((int(times10(str(carry))) + int(v)) // n2)
		carry = (int(times10(str(carry))) + int(v)) % n2
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
		newcarry = (int(times10(str(carry))) + int(n1s[x])) % n2
		if over:
			if newcarry==0 and r1==0:
				res+= str((int(times10(str(carry))) + int(n1s[x])) // n2)
				return sign + re.sub("^$", "0", re.sub("^\\.", "0.", res.strip("0").rstrip(".")))
			y = 0
			while y < len(carries):
				if carries[y]==newcarry and (y % len(str(r1)))==((rcount + 1) % len(str(r1))):
					res+= str((int(times10(str(carry))) + int(n1s[x])) // n2)
					result = sign + re.sub("^$", "0", re.sub("^\\.", "0.", re.sub("^0+", "", res[:x - rcount + y] + "[" + res[x - rcount + y:] + "]")))
					if result[result.index("[") - 1]==result[result.index("]") - 1]:
						result = result[:result.index("[") - 1] + "[" + result[result.index("[") - 1] + result[result.index("[") + 1:result.index("]") - 1] + "]"
					if result.index("]")==result.index("[") + 3 and result[result.index("[") + 1]==result[result.index("[") + 2]:
						result = result[:result.index("[") + 2] + "]"
					return result.replace("[", rstr1).replace("]", rstr2)
				y+= 1
		res+= str((int(times10(str(carry))) + int(n1s[x])) // n2)
		if over:
			carries.append(carry)
		carry = newcarry
		x+= 1

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 2:
		print(div(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 0, sys.argv[4] if len(sys.argv) > 4 else "[", sys.argv[5] if len(sys.argv) > 5 else "]"))
