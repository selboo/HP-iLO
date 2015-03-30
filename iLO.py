#!/usr/bin/env python
#coding=utf8
# AUTHOR written by Selboo 2014/11/11

import os, sys, re
import json
import httplib2
import urllib

class iLO():

	def __init__(self, ip, timeout=5):
		if not ip:
			print 'IP is null'
			exit()
		self.Url        = "https://"+ip+"/json/"
		self.timeout    = timeout
		self.headers    = {
			'Accept'          : 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
			'User-Agent'      : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0',
			'Accept-Encoding' : 'gzip, deflate',
			'Cache-Control'   : 'no-cache',
			'Accept-Language' : 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
			'Content-Type'    : 'application/x-www-form-urlencoded; charset=UTF-8'
		}
	

	def iLO_Conn(self, Disable_SSL):
		if Disable_SSL:
			self.http = httplib2.Http(disable_ssl_certificate_validation=True, timeout=self.timeout)
		else:
			self.http = httplib2.Http(disable_ssl_certificate_validation=False, timeout=self.timeout)

	def iLO_Login(self, Type, User, Pass):
		self.login       = {"method":"login", "user_login":User ,"password":Pass}
		self.body        = json.dumps(self.login)
		try:
			response,content = self.http.request(self.Url+"login_session", Type, headers=self.headers, body=self.body)
		except Exception, e:
			print 'Connection False'
			exit()
		if response['status'] != '200':
			print 'UserName or Password Error'
			exit()
		self.session_key = eval(content)['session_key']
		self.headers     = {'Cookie' : 'sessionKey=%s' %(self.session_key)}

	def Get_Info(self, Type, url):
		response,content = self.http.request(self.Url+url, Type, headers=self.headers)
		
		if response['status'] == '200':
			#return eval(content)
			return json.dumps(eval(content), indent=1)
		else:
			return 'Get Info False'

	def iLO_Logout(self):
		self.logout      = {"method":"logout", "session_key":self.session_key}
		self.outbody     = json.dumps(self.logout)
		response,content = self.http.request(self.Url+"login_session", 'POST', headers=self.headers, body=self.outbody)
		if response['status'] == '200':
			return 'Logout True'
		else:
			return 'Logout False'
		
	def iLO_Test(self):
		pass

# 服务器管理IP
ip                  = '192.168.1.100'
# 用户名
UserName            = 'Administrator'
# 密码
PassWord            = '123456'

# 系统简介状态
health_summary      = 'health_summary'
# 硬件详细状态
health_drives       = 'health_drives'

health_power_supply = 'health_power_supply'
power_supplies      = 'power_supplies'
power_readings      = 'power_readings'

health_fans         = 'health_fans'

health_temperature  = 'health_temperature'

mem_info            = 'mem_info'
nic_info            = 'nic_info'
"""
更多信息和字段，请跟踪 http HEAD 头 进行查看
"""

ilo = iLO(ip)
ilo.iLO_Conn(Disable_SSL=True)
ilo.iLO_Login('POST', UserName, PassWord)


Info = ilo.Get_Info('GET', 'health_drives')
print Info

ilo.iLO_Logout()


