#!/usr/bin/env python3.6
import pyperclip
from user import User
from crredentials import credentials
def create_user(fname,lname,password):
	'''
	Function to create a new user account
	'''
    new_user = User(fname,lname,password)
	return new_user
