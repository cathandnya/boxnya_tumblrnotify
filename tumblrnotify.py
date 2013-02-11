# -*- coding: utf-8 -*-
import atexit
import os
import sys
import signal
import time

import re
import time
import urllib, urllib2
import cookielib

from BeautifulSoup import BeautifulSoup
from lib.core import Input

class TumblrNotify(Input):
	def init(self):
		print "tumblr notify init"
		self.sended_messages = []
		self.isInitial = True

	def fetch(self):
		print "tumblr notify fetch"
		# アクセスするWebサイトのURLを設定
		url = 'https://www.tumblr.com/login'  
		  
		# Cookie
		cookie = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  
		web = opener.open(url)  
		dom = BeautifulSoup(web)  
		hidden = dom.find(attrs = {'class' : "form_row_hidden"})
		# print hidden
		postdata = {}
		for param in hidden.findAll('input'):
			# print param
			postdata[dict(param.attrs)["name"]] = dict(param.attrs)["value"]
		postdata["redirect_to"] = "/dashboard"
		postdata["user[email]"] = self.email
		postdata["user[password]"] = self.password
		postdata = urllib.urlencode(postdata);
		# print postdata
		
		# login
		web = opener.open(url, postdata)
		# print web
		
		# load
		web = opener.open("http://www.tumblr.com/blog/" + self.blog)
		dom = BeautifulSoup(web)  
		sentences = dom.findAll(attrs = {'class' : "notification_sentence"})
		for sentence in sentences:
			msg = re.compile(r'<.*?>').sub('', sentence.renderContents())
			if self.isInitial:
				self.sended_messages.append(msg)
			elif not msg in self.sended_messages:
				print "tumblr_notify: %s" % msg
				self.send(msg)
				self.sended_messages.append(msg)
				if len(self.sended_messages) > 50:
					self.sended_messages.pop(0)

		self.isInitial = False;
		time.sleep(self.period)
