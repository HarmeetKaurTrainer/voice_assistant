import pyttsx3  # Voice for the assistant
import speech_recognition as sr # recognizes the voice input and converts it to be understandable by the program
import smtplib, ssl # smtplib sends mail and ssl provides a secure connection to do so
import subprocess, os # subproccess opens a pseudo shell, OS passes commands to the shell
import time # allows the program to sleep(stop temporarily)
from selenium import webdriver # controls the browser
# driver = webdriver.Chrome()
Options = webdriver.ChromeOptions()
Options.add_experimental_option("detach", True)

#opening chrome with os, subprocess
# os.chdir("C:\Program Files\Google\Chrome\Application")
# subprocess.Popen("chrome.exe")

#Email array that is used by the program to send emails

email = input("Your email Address: ")
passwd = input("your email password(this is needed for sending mails with the assistant): ")
#####Email Table#####
print('Initializing the array of emails, you can add upto 3 emails...\n\n')
email1 = input("email 1: ")

keyword1 = input("keyword to identify the above email address: ")

email2 = input("email 2: ")

keyword2 = input("keyword to identify the above email address: ")

email3 = input("email 3: ")

keyword3 = input("keyword to identify the above email address: ")

emails = [email1, email2, email3]

def voice(text):
	engine = pyttsx3.init('sapi5')
	engine.setProperty('rate', 140)
	engine.say(text)
	engine.runAndWait()

# with webdriver.Chrome() as driver:
# 	WebDriverWait(driver, 3)
# 	driver.get("https://www.google.com/search?q={}".format("hi")) 

r = sr.Recognizer() # initializes a recognizer used for the recognition of voices
mic = sr.Microphone(device_index=1)

# Sending Mail with SMTP
######TEST EMAIL######
# smtpOBJ = smtplib.SMTP(host="smtp.gmail.com", port=25)
# smtpOBJ.ehlo() # not necessary
# smtpOBJ.starttls()
# smtpOBJ.ehlo() # not necessary
# smtpOBJ.login("email", "passwd")
# smtpOBJ.sendmail("email", "testEmail", "See if this works")

# Send Mail with SMTP with voice
try:
	with mic as source: # with statement necessary for voice input
		# voice("Hi, I am an artificial Intelligence inspired by Kalkin Raheja")
		voice("these are some of the commands that I can help you with: Sending mail, searching google and youtube")
		voice("what do you want me to do?")
		r.adjust_for_ambient_noise(source)
		Input = r.listen(source)
		t = r.recognize_google(Input)
		print(t)
		if "mail" in t:
			if keyword1 in t:
				voice("what is the message?")
				t3 = r.listen(source)
				t2 = r.recognize_google(t3)
				server = smtplib.SMTP(host="smtp.gmail.com", port=25)
				server.ehlo()
				server.starttls()
				server.ehlo()
				server.login(email, passwd)
				server.sendmail(email, emails[0], t2)

			if keyword2 in t:
				voice("what is the message?")
				t4 = r.listen(source)
				t5 = r.recognize_google(t4)
				server = smtplib.SMTP(host="smtp.gmail.com", port=25)
				server.ehlo()
				server.starttls()
				server.ehlo()
				server.login(email, passwd)
				server.sendmail(email, emails[1], t5)

			if keyword3 in t:
				voice("what is the message?")
				t6 = r.listen(source)
				t7 = r.recognize_google(t6)
				server = smtplib.SMTP(host="smtp.gmail.com", port=25)
				server.ehlo()
				server.starttls()
				server.ehlo()
				server.login(email, passwd)
				server.sendmail(email, emails[2], t7)

		if "search" in t:
			# os.chdir("C:\Program Files\Google\Chrome\Application")
			# subprocess.Popen("chrome.exe")
			# time.sleep(3)
			voice("What do you want to search?")
			r.adjust_for_ambient_noise(source)
			t8 = r.listen(source)
			t9 = r.recognize_google(t8)
			with webdriver.Chrome(options=Options) as driver:
				driver.get("https://www.google.com/search?q={}".format(t9))
				while True:
					time.sleep(0.1)

		if "YouTube" in t:
			voice("What do you want to search on youtube?")
			r.adjust_for_ambient_noise(source)
			t10 = r.listen(source)
			t11 = r.recognize_google(t10)
			with webdriver.Chrome(options=Options) as driver:
				# os.chdir("C:\Program Files\Google\Chrome\Application")
				# subprocess.Popen("chrome.exe")
				# time.sleep(1.5)
				print(t11)
				driver.get("https://www.youtube.com/results?search_query={}".format(t11))
				while True:
					time.sleep(0.1)

		if "thank you" in t:
			voice("happy to help")
			exit()
except KeyboardInterrupt:
	voice('Good-bye')
	print("exiting.....")
except:
	print("an unexpected error occured, exiting....")
	voice("an unexpected error occured, exiting....")
