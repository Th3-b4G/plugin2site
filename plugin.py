import requests
import re
import base64
import os

#<-----clear start----->
def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][(os.name == 'nt')])
#<-----clear done----->

#<------HEAD&BANNER-------------->
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
banner = "ICAgIDogICAgICAgICAgICAgIDogICAgICAgICAgICAgICAgOgogICAgOiAgICAgICAgICAgICAgOiAgICAgICAgICAgICAgICA6CiAgLyBfIFwgICAgICAgICAgICA6ICAgICAgICAgICAgICAgIDoKXF9cKF8pL18vICAgICAgICAgIDogICAgICAgICAgICAgICAgOgogXy8vIlxcXyAgICAgICAgICAgOiAgICAgICAgICAgICAgICA6CiAgLyAgIFwgICAgICAgICAgLyBfIFwgICAgICAgICAgICAgIDoKICAgICAgICAgICAgICAgXF9cKF8pL18vICAgICAgICAgICAgOgogICAgICAgICAgICAgICAgXy8vIlxcXyAgICAgICAgICAgICA6IAogICAgICAgICAgICAgICAgIC8gICBcICAgICAgICAgICAgLyBfIFwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBcX1woXykvXy8KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXy8vIlxcXyAKICAgICAgICAgIC0nJy0tLiAgICAgICAgICAgICAgICAgIC8gICBcCiAgICAgICBfYD4gICBgXC4tJzwKICAgIF8uJyAgICAgXyAgICAgJy5fCiAgLicgICBfLj0nICAgJz0uXyAgICcuTjM2QSBQUklWOCBHUkFCQkVSIAogID5fICAgLyAvX1wgL19cIFwgICBfPCAgICAgICAgICAgICAgdjEKICAgIC8gKCAgXG8vXFxvLyAgKSBcCiAgICA+Ll9cIC4tLF8pLS4gL18uPApwb2MgICAgIC9fXy8gXF9fXCAKICAgICAgICAgICctLS0nICAgICAgICAgU01MQVNIIFRIRSBXRUIKICAgICAgICAgICAgICAgICAgICAgICAgLi4uLi4uLi4uLi4uLi4JCSAgCgkJCQkJCQkJICA="
#<------HEAD&BANNER-------------->

#<----------TOOL 1 --------------->
def plugin4life():
	clear()
	print("""
		----------------------
		SEARCH WORDPRESS SITE BY PLUGIN -------
		----------------------""")
	pluglist = raw_input("GIVE ME YUOUR PLUGIN LIST? :")
	pluglist = open(pluglist, 'r').read().splitlines()
	for plugin in pluglist:
		countx = 1
		while  countx < 20000 :
			payloadx = requests.get("http://pluginu.com/"+plugin+"/"+str(countx), headers=headers, timeout=10).text
			list = re.findall('<p style="margin-bottom: 20px">(.*?)</p></a>', payloadx)
			for x in list:
				print("[+]"+plugin +" :"+" page :"+str(countx)+"  >>"+ x)
				open("plugin.txt", "a").write(x + "\n")
			countx = countx+1
#<----------TOOL 1 --------------->

#<----------TOOL 2 --------------->

def pesta4life():
	clear()
	print("""
		----------------------
		SEARCH PESTASITE BY PLUGIN -------
		----------------------""")
	pluglist = raw_input("GIVE ME YUOUR PLUGIN LIST? :")
	pluglist = open(pluglist, 'r').read().splitlines()
	for plugin in pluglist:
		countx = 1
		while  countx < 20000 :
			payloadx = requests.get("http://prestasites.com/theme/"+plugin+"/"+str(countx), headers=headers, timeout=10).text
			list = re.findall('<h3 style="margin-bottom: 20px">(.*?)</h3></a>', payloadx)
			for x in list:
				print("[+]"+plugin +" :"+" page :"+str(countx)+"  >>"+ x)
				open("pesta-plugin.txt", "a").write(x + "\n")
			countx = countx+1
#<----------TOOL 2 --------------->

#<----------HELP --------------->
def help():
	clear()
	print(banner.decode('base64'))
	
	print("""

    	 USE PLUGIN LIST LIKE:
    	 --------------------
    	 Default-bootstrap
    	 Default
    	 Prestashop
    	 ------------
    	 Any ques pm @Th3b4G""")

	
#<----------HELP --------------->


print(banner.decode('base64'))
print('''
	[+] 0 [+] SEARCH BY PLUGIN(WP)
	[+] 1 [+] SEARCH BY PLUGIN(PESTA)
	[+] 3 [+] HELP ''')

doIT = raw_input("[+] WHAT YOU WANA DO  :")
if doIT == '0':
    plugin4life()

elif doIT == '1':
    pesta4life()

elif doIT == '3':
	help()
    
   
