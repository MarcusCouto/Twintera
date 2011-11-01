# -*- coding: utf-8 -*-
import sys
import os, glob, re
import subprocess
import random

semente = random.random()*35


print semente
file = open("./"+str(semente)+".txt",'w')  
file.write("teste" +str(semente))
file.close()

	
	





