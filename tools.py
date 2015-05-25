__author__ = 'Johnny'
#coding=utf-8
import time
import urllib
import re

read = open('url.txt')
try:
    all_text = read.readlines()
    for line in all_text:
        print(line)
finally:
    read.close()
