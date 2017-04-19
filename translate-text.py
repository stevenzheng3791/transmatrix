#!/usr/bin/python
import sys
from googletrans import Translator
translator = Translator()

print (translator.translate(sys.argv[1], src='it', dest='en')).text
