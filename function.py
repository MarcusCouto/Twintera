# -*- coding: utf-8 -*-
import sys
import os
import datetime

def removeMarcacaoEncode(text):
	text.replace("&#", "|@|")
	return text
	
def trataCodigosHTML(text):  			
    text.replace("|@|160;", "&nbsp;")
    text.replace("|@|161;", "&iexcl;")
    text.replace("|@|162;", "&cent;")
    text.replace("|@|163;", "&pound;")
    text.replace("|@|164;", "&curren;")
    text.replace("|@|165;", "&yen;")
    text.replace("|@|166;", "&brvbar;")
    text.replace("|@|167;", "&sect;")
    text.replace("|@|168;", "&uml;")
    text.replace("|@|169;", "&copy;")
    text.replace("|@|170;", "&ordf;")
    text.replace("|@|171;", "&laquo;")
    text.replace("|@|172;", "&not;")
    text.replace("|@|173;", "&shy;")
    text.replace("|@|174;", "&reg;")
    text.replace("|@|175;", "&macr;")
    text.replace("|@|176;", "&deg;")
    text.replace("|@|177;", "&plusmn;")
    text.replace("|@|178;", "&sup2;")
    text.replace("|@|179;", "&sup3;")
    text.replace("|@|180;", "&acute;")
    text.replace("|@|181;", "&micro;")
    text.replace("|@|182;", "&para;")
    text.replace("|@|183;", "&middot;")
    text.replace("|@|184;", "&cedil;")
    text.replace("|@|185;", "&sup1;")
    text.replace("|@|186;", "&ordm;")
    text.replace("|@|187;", "&raquo;")
    text.replace("|@|188;", "&frac14;")
    text.replace("|@|189;", "&frac12;")
    text.replace("|@|190;", "&frac34;")
    text.replace("|@|191;", "&iquest;")
    text.replace("|@|192;", "&Agrave;")
    text.replace("|@|193;", "&Aacute;")
    text.replace("|@|194;", "&Acirc;")
    text.replace("|@|195;", "&Atilde;")
    text.replace("|@|196;", "&Auml;")
    text.replace("|@|197;", "&Aring;")
    text.replace("|@|198;", "&AElig;")
    text.replace("|@|199;", "&Ccedil;")
    text.replace("|@|200;", "&Egrave;")
    text.replace("|@|201;", "&Eacute;")
    text.replace("|@|202;", "&Ecirc;")
    text.replace("|@|203;", "&Euml;")
    text.replace("|@|204;", "&Igrave;")
    text.replace("|@|205;", "&Iacute;")
    text.replace("|@|206;", "&Icirc;")
    text.replace("|@|207;", "&Iuml;")
    text.replace("|@|208;", "&ETH;")
    text.replace("|@|209;", "&Ntilde;")
    text.replace("|@|210;", "&Ograve;")
    text.replace("|@|211;", "&Oacute;")
    text.replace("|@|212;", "&Ocirc;")
    text.replace("|@|213;", "&Otilde;")
    text.replace("|@|214;", "&Ouml;")
    text.replace("|@|215;", "&times;")
    text.replace("|@|216;", "&Oslash;")
    text.replace("|@|217;", "&Ugrave;")
    text.replace("|@|218;", "&Uacute;")
    text.replace("|@|219;", "&Ucirc;")
    text.replace("|@|220;", "&Uuml;")
    text.replace("|@|221;", "&Yacute;")
    text.replace("|@|222;", "&THORN;")
    text.replace("|@|223;", "&szlig;")
    text.replace("|@|224;", "&agrave;")
    text.replace("|@|225;", "&aacute;")
    text.replace("|@|226;", "&acirc;")
    text.replace("|@|227;", "&atilde;")
    text.replace("|@|228;", "&auml;")
    text.replace("|@|229;", "&aring;")
    text.replace("|@|230;", "&aelig;")
    text.replace("|@|231;", "&ccedil;")
    text.replace("|@|232;", "&egrave;")
    text.replace("|@|233;", "&eacute;")
    text.replace("|@|234;", "&ecirc;")
    text.replace("|@|235;", "&euml;")
    text.replace("|@|236;", "&igrave;")
    text.replace("|@|237;", "&iacute;")
    text.replace("|@|238;", "&icirc;")
    text.replace("|@|239;", "&iuml;")
    text.replace("|@|240;", "&eth;")
    text.replace("|@|241;", "&ntilde;")
    text.replace("|@|242;", "&ograve;")
    text.replace("|@|243;", "&oacute;")
    text.replace("|@|244;", "&ocirc;")
    text.replace("|@|245;", "&otilde;")
    text.replace("|@|246;", "&ouml;")
    text.replace("|@|247;", "&divide;")
    text.replace("|@|248;", "&oslash;")
    text.replace("|@|249;", "&ugrave;")
    text.replace("|@|250;", "&uacute;")
    text.replace("|@|251;", "&ucirc;")
    text.replace("|@|252;", "&uuml;")
    text.replace("|@|253;", "&yacute;")
    text.replace("|@|254;", "&thorn;")
    text.replace("|@|255;", "&yuml;")
    text.replace("|@|10084;", "")
    text.replace("|@|8221;", "")
    text.replace("|@|8211;", "-")
    text.replace("|@|9834;", "")
    text.replace("|@|9829;", "")
    text.replace("|@|9824;", "")
    text.replace("|@|9827;", "")
    text.replace("|@|9830;", "")
    text.replace("|@|8968;", "")
    text.replace("|@|8969;", "")
    text.replace("|@|8970;", "")
    text.replace("|@|8971;", "")
    text.replace("|@|9674;", "")
    text.replace("|@|10216;", "")
    text.replace("|@|10085;", "")
    text.replace("|@|350;", "")
    
    return text


def escreveLog(text):
	today_date = datetime.datetime.now()
	file = open("/var/www/log/log.txt",'a')  
	file.write(str(today_date) + " " + text +"\n")
	file.close()


def trataPalavra(text):
	word = text.lower()
	if '.' in word:
		word = word.replace('.','')
	if ')' in word:
		word = word.replace(')','')
	if '(' in word:
		word = word.replace('(','')
	if '=' in word:
		word = word.replace('=','')
	if '-' in word:
		word = word.replace('-','')
	if '~' in word:
		word = word.replace('~','')
	if ',' in word:
		word = word.replace(',','')
	if ';' in word:
		word = word.replace(';','')
	if ':' in word:
		word = word.replace(':','')
	if '?' in word:
		word = word.replace('?','')
	if '!' in word:
		word = word.replace('!','')
	if ' ' in word:
		word = word.replace(' ','')
	if '"' in word:
		word = word.replace('"','')
	if "'" in word:
		word = word.replace("'","")	
		
	return word 
	
def corrigeData(text):
	
	tokens = text.split()
		
	
	if tokens[1] == "Jan":
		tokens[1] = str("01")	
			
	elif tokens[1] == "Feb":
		tokens[1] = str("02")		
		
	elif tokens[1] == "Mar":
		tokens[1] = str("03")		
		
	elif tokens[1] == "Apr":
		tokens[1] = str("04")		
		
	elif tokens[1] == "May":
		tokens[1] = str("05")		
		
	elif tokens[1] == "Jun":
		tokens[1] = str("06")		
		
	elif tokens[1] == "Jul":
		tokens[1] = str("07")		
		
	elif tokens[1] == "Aug":
		tokens[1] = str("08")		
		
	elif tokens[1] == "Sep":
		tokens[1] = str("09")		
		
	elif tokens[1] == "Oct":
		tokens[1] = str("10")		
		
	elif tokens[1] == "Nov":
		tokens[1] = str("11")		
		
	elif tokens[1] == "Dec":
		tokens[1] = str("12")	

	texto =  tokens[5] + "-" + tokens[1] + "-" + tokens[2] + " " + tokens[3]
	
	return texto

def corrigeDataPost(text):
	
	tokens = text.split()
	
	
	
	
	if tokens[2] == "Jan":
		tokens[2] = str("01")	
			
	elif tokens[2] == "Feb":
		tokens[2] = str("02")		
		
	elif tokens[2] == "Mar":
		tokens[2] = str("03")		
		
	elif tokens[2] == "Apr":
		tokens[2] = str("04")		
		
	elif tokens[2] == "May":
		tokens[2] = str("05")		
		
	elif tokens[2] == "Jun":
		tokens[2] = str("06")		
		
	elif tokens[2] == "Jul":
		tokens[2] = str("07")		
		
	elif tokens[2] == "Aug":
		tokens[2] = str("08")		
		
	elif tokens[2] == "Sep":
		tokens[2] = str("09")		
		
	elif tokens[2] == "Oct":
		tokens[2] = str("10")		
		
	elif tokens[2] == "Nov":
		tokens[2] = str("11")		
		
	elif tokens[1] == "Dec":
		tokens[1] = str("12")	

	texto =  tokens[3] + "-" + tokens[2] + "-" + tokens[1] + " " + tokens[4]
	
	return texto
