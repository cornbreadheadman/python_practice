#!/usr/bin/env python

# Python Scripting by Cornbread
# In The Begining

# Import various librarys
#import CHIP_IO.GPIO as GPIO
#import CHIP_IO.PWM as PWM
#import CHIP_IO.SOFTPWM as SOFTPWM
import time
import datetime
import random
import pyperclip

# Global Variables
author = 'Cornbread'
now = datetime.datetime.now()

# Defines
def cb():
	clipboard = pyperclip.paste()
	return clipboard

def lotto(min, max):
	number = random.randint(min, max)
	return number

# Introduction
print('Hello Cruel World!')
time.sleep( 1 )

# Gather the current time
print('The current date and time is', now.strftime("%B %d, %Y %I:%M %p"))

time.sleep( 1 )

# Gather name
name = input('What is your name?\n')
print('Hello', name)
time.sleep( 1 )

# Grab a lucky number
number = lotto(100, 999)
print('Your lucky number is', number)
if number == 420:
    print('Wow! Thats a great number.')
time.sleep( 1 )

# Print the clipboard
clipboard = cb()
print('The following stuff is in your clipboard:')
print('<------------Begining-------------->')
print(clipboard)
print('<-------------Ending--------------->')

time.sleep( 2 )

print('This scripts was written by:', author)
