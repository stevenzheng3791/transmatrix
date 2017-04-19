# generate augmented english word embeddings based on POS tags

import subprocess
with open("data/IT.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05.txt",'r') as f:
	lines = f.readlines()

en_tag = {
	'CC' : 0,
	'CD' : 1,
	'DT' : 2,
	'EX' : 3,
	'FW' : 4,
	'IN' : 5,
	'JJ' : 6,
	'JJR' : 7,
	'JJS' : 8,
	'LS' : 9,
	'MD' : 10,
	'NN' : 11,
	'NNS' : 12,
	'NP' : 13,
	'NPS' : 14,
	'PDT' : 15,
	'POS' : 16,
	'PP' : 17,
	'PP$' : 18,
	'RB' : 19,
	'RBR' : 20,
	'RBS' : 21,
	'RP' : 22,
	'SYM' : 23,
	'TO' : 24,
	'UH' : 25,
	'VB' : 26,
	'VBD' : 27,
	'VBG' : 28,
	'VBN' : 29,
	'VBP' : 30,
	'VBZ' : 31,
	'WDT' : 32,
	'WP' : 33,
	'WP$' : 34,
	'WRB' : 35,	
}

import sys
from googletrans import Translator
translator = Translator()

with open("data/IT.200K.cbow1_wind5_hs0_neg10_size300_smpl1e-05_POS.txt",'w') as f:
	m = 0
	z = ""
	buf = []
	#f.write(lines[0])
	f.write("200000 336\n")
	lines = lines[1:]
	for x in lines:
		print m
		if (m % 20000) == 0:
			#print z
			proc = subprocess.Popen(["./english_pos_tag.sh",z], stdout=subprocess.PIPE)
			tags = proc.stdout.read().split('\n')
			for i in range(len(buf)):
				line = buf[i]
				tag = tags[i].split()[1]
				f.write(line)
				for j in range(36):
					if (tag in en_tag) and (j == en_tag[tag]):
						f.write(' 1')
					else:
						f.write(' 0')
				f.write('\n')
				f.flush()
			buf = []
			z = ""
		#z += (x.split()[0] + " ")
		value = x.split()[0]
		#print value
		w = ""
		try:
			w = (translator.translate(sys.argv[1], src='it', dest='en')).text.split()[0]
		except:
			w = "x"

		#print w
		z += (w + " ")

		buf.append(x.strip('\n'))
		m += 1

	
	proc = subprocess.Popen(["./english_pos_tag.sh",z], stdout=subprocess.PIPE)
	tags = proc.stdout.read().split('\n')
	for i in range(len(buf)):
		line = buf[i]
		tag = tags[i].split()[1]
		f.write(line)
		for j in range(36):
			if (tag in en_tag) and (j == en_tag[tag]):
				f.write(' 1')
			else:
				f.write(' 0')
		f.write('\n')
		f.flush()
	


