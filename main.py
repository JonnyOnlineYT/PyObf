import random
import re
import base64
fil = open("in.py")
out = fil.read()
version = 5
commentstring = " #$$$$OBFUSCATED WITH PYOBF$$$$ - "
varname = "PYOBF_" * 100
def removeComments(modify):
	reer = re.findall(r"#.*?\n", modify)
	temp = out
	commentsremoved = 0
	for goofyahh in reer:
		temp = temp.replace(goofyahh, "", -1)
		commentsremoved += 1
	
	print("Removed", commentsremoved, "comment(s)!")
	return temp

def commentSpam(modify):
	modify = modify.replace("\n", "\n" + commentstring + str(int(random.randint(1000, 99999))*random.randint(10000,999999)) + "\n", -1)
	for i in range(len(out)):
		modify = commentstring + str(random.randint(10000,999999)) + str(random.randint(10000,999999)) + str(random.randint(10000,999999)) + str(random.randint(10000,999999)) + str(random.randint(10000,999999)) + str(random.randint(10000,999999)) + "\n" + modify
		modify = modify + commentstring + str(random.randint(10000,999999)) + str(random.randint(10000,999999)) + str(random.randint(10000,999999)) + str(random.randint(10000,999999)) + str(random.randint(10000,999999)) + str(random.randint(10000,999999)) + "\n"
	
	print("Spammed comments!")
	return modify

def enterSpam(modify):
	modify = modify.replace("\n", "\n" * random.randint(3, 10), -1)
	modify = modify.replace("(", "(" + ("\n" * random.randint(10, 15)), -1)
	modify = modify.replace(")", ("\n" * random.randint(10, 20)) + ")", -1)
	print("Spammed enter!")
	return modify
    

def changeFuncs(modify):
	lul = re.findall("def.*?\(", modify)
	randnum = ""
	paste = ""
	nameschanged = 0
	for goofyahh in lul:
		if goofyahh.replace("def ", "", -1)[0] != "_":
			randnum = str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999))
			paste = "def a" + randnum + "("
			modify = modify.replace(goofyahh.replace("def ", "", -1), paste.replace("def ", "", -1), -1).replace("strf" + paste.replace("def ", "", -1).replace("(", "", -1), "strftime", -1)
			modify = modify.replace(goofyahh.replace("def ", "", -1).replace("(", "", -1) + ")", paste.replace("def ", "", -1).replace("(", "", -1) + ")", -1)
			nameschanged += 1
	
	print("Changed", nameschanged, "function name(s)!")
	return modify

def doStringObf(modify):
	stringsencrypted = 0
	strings = re.findall("\".*?\"", modify)
	for nonobf in strings:
		stringsencrypted += 1
		modify = modify.replace(nonobf,"do_the_fortnite(b\"" + base64.b64encode(nonobf.replace("\"", "").encode("ascii")).decode("utf-8") + "\")", -1)
	modify = "import base64\ndef do_the_fortnite(inarg):\n  return base64.b64decode(inarg).decode(\"utf-8\")\n\n" + modify

	print("Obfuscated", stringsencrypted, "string(s)!")
	return modify

def goofyAhhStringObf(modify):
	stringsencrypted = 0
	strings = re.findall("\".*?\"", modify)
	for nonobf in strings:
		nonobf = nonobf.replace("\"", "", -1)
		newString = ""
		for cha in nonobf:
			newString = newString = newString + str(hex(ord(cha))).replace("0x", "\\x", -1)
		stringsencrypted += 1
		modify = modify.replace(nonobf, newString, -1)

	print("Hexxed", stringsencrypted, "string(s)!")
	return modify

def execObf(modify):
	modify = modify.replace("\\", "\\\\", -1).replace("\n", "\\n", -1).replace("\"", "\\\"", -1)
	vasrsr = modify.split("i")
	last = vasrsr[-1]
	modify = varname + " = \"\""
	for punjabi in vasrsr:
		if(punjabi != last):
			punjabi = punjabi + "i"
		modify = modify + "\n" + varname + " = " + varname + " + " + "\"" + punjabi + "\""
	
	modify = modify + "\nexec(" + varname + ")"
	return modify

def doNumberObf(modify):
	numbersencrypted = 0
	nums = re.findall("\d+?\)", modify)
	for nonobf in nums:
		print(nonobf)
		rand1 = str(random.randint(-100, 100))
		rand2 = str(random.randint(-100, 100))
		rand3 = str(random.randint(-100, 100))
		rand4 = str(random.randint(-100, 100))
		nonobf = nonobf.replace(")", "", -1)
		numbersencrypted += 1
		acchyually = int(nonobf) + int(rand1) - int(rand2) - int(rand3) + int(rand4)
		susi = str(int(nonobf) + int(rand1)) + "-" + rand2 + "-" + rand3 + "+" + rand4 + "-" + str(acchyually - int(nonobf))
		modify = modify.replace(nonobf, susi, -1)
	
	print("Obfuscated", numbersencrypted, "number(s)!")
	return modify

def intrnlObf(modify):
	obfed = 0
	randnum = ""
	if "random." in modify:
		obfed += 1
		randnum = str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999)) + str(random.randint(1, 99999))
		modify = modify.replace("random.", "a" + randnum + "().", -1)
		modify = "def a" + randnum + "():\n  return random\n\n" + modify
	
	if "print(" in modify:
		obfed += 1
		randnum = str(random.randint(1, 99999))
		modify = modify.replace("print(", "a" + randnum + "(", -1)
		modify = "def a" + randnum + "(inarg):\n  print(inarg)\n\n" + modify
	
	if "open(" in modify:
		obfed += 1
		randnum = str(random.randint(1, 99999))
		modify = modify.replace("open(", "a" + randnum + "(", -1)
		modify = "def a" + randnum + "(inarg):\n return open(inarg)\n\n" + modify
	
	print("Randomized", obfed, "internal func(s)!")
	return modify

def writeToFile(inp):
	outfile = open("out.py", "w")
	outfile.write(inp)

def doTitle():
	print("###..........###..#.....###")
	print("#..#.#...#..#...#.#....#...")
	print("###...#.#...#...#.###..###.")
	print("#......#....#...#.#..#.#...")
	print("#.....#......###..###..#.v" + str(version))

# veri beautiful startup screen
doTitle()
# removing comments to not confuse other modules
#out = removeComments(out)
# number obfuscation
#out = doNumberObf(out)
# string obf2 bozo
#out = doStringObf(out)
# string obf1 bozo
#out = goofyAhhStringObf(out)
# internal command obf
#out = intrnlObf(out)
# change names of defined functions
#out = changeFuncs(out)
# Spamming enter to confuse humans
#out = enterSpam(out)
# execobf
out = execObf(out)
# spam comments les go
#out = commentSpam(out)
# write file
writeToFile(out)
