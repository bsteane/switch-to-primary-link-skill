# switch to primary link
import paramiko 
import time 
import getpass 
import os 

from mycroft import MycroftSkill, intent_file_handler

__author__ = "bsteane" 

class SwitchToPrimaryLink(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('link.primary.to.switch.intent')
    def handle_link_primary_to_switch(self, message):
        ip = "192.168.0.200" 
        twrssh = paramiko.SSHClient() 
        twrssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        twrssh.connect(ip, port=22, username="cisco", password="cisco") 
        remote = twrssh.invoke_shell() 
        remote.send('term len 0\n')
        remote.send('en\n') 
        remote.send('cisco\n')
        remote.send('conf t\n')
        remote.send('int g0/1\n') 
        remote.send('no shut\n') 
        remote.send('int g0/24\n') 
        remote.send('shut\n') 
        time.sleep(1) 
        twrssh.close()
        self.speak_dialog('link.primary.to.switch')


def create_skill():
    return SwitchToPrimaryLink()

