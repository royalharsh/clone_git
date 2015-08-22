from github import Github
from configparser import ConfigParser

def g_pass():
 config = ConfigParser()
 config.read('config.ini')
 usr,pwd = config['github']['user'],config['github']['pass']
 return usr,pwd

def connect():
 usr,pwd = g_pass()
 return Github(usr,pwd)
