import base64
import datetime
import requests
import re
import execjs

helper=execjs.compile(open("iobbhelper.js",'r').read())

def encode(x):
	v=str(hex(len(x)))[2:]
	return "0"*(4-len(v))+v+x
def generateiobb(url,prox):
	sess=requests.session()
	token=re.search("\"(.*?)\"",sess.get("https://mpsnare.iesnare.com/script/logo.js",headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36","Referer":url},proxies={"https":prox}).text).group(1)
	script=sess.get("https://mpsnare.iesnare.com/snare.js",headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36","Referer":url},proxies={"https":prox}).text
	sess.close()
	jssrc=base64.b64decode(re.search("\"JSSRC\",.*?\"(.*?)\"",script).group(1))
	jstime=datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S")
	svrtime=re.search("\"SVRTIME\",.*?\"(.*?)\"",script).group(1)
	iggy=re.search("\"IGGY\",.*?\"(.*?)\"",script).group(1)
	jsver=re.search("\"JSVER\",.*?\"(.*?)\"",script).group(1)
	return helper.call("getblackbox","00190006INTLOC"+encode(url)+"0004JINT0008function0005JENBL000110005JSSRC"+encode(jssrc)+"0004UAGT0072Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.360007JSTOKEN"+encode(token)+"0007HACCLNG000een-US,en;q=0.90005JSVER"+encode(jsver)+"0004TZON"+encode("300")+"0006JSTIME"+encode(jstime)+"0007SVRTIME"+encode(svrtime)+"0005JBRNM0006Chrome0005JBRVR000c67.0.3396.990005JBROS000fWindows NT 10.00005APVER006a5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.360005APNAM0008Netscape0005NPLAT0005Win320005JBRCM001dWin64; x64; KHTML, like Gecko0005JLANG0005en-US0004IGGY"+encode(iggy)+"0004JRES0008864x15360006JPLGNS004ainternal-pdf-viewer;mhjfbmdgcfjbbpaeojofohoefgiehjai;internal-nacl-plugin;0007LSTOKEN"+encode(token)+"0006CTOKEN"+encode(token)+"0008WDBTOKEN"+encode(token))