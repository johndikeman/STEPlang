#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import sys, copy, os, glob, time

reserved_methods = ['pause','output', 'input', 'finput', 'sto', 'dupe' ,'+', '-', '/', '*', '%', '?', 'goto', 'end', 'rand', '>', '<', '==', "!="]

parser = ArgumentParser()
parser.add_argument('file',help='the path to the step file')

class StepSyntaxError(Exception):
	def __init__(self,message):
		super(Exception,self).__init__(message + ' ¯\_(ツ)_/¯')

class Interpreter:
	def __init__(self, li):
		self.global_index = 0L
		self.li = li
		self.computering = True
		self.memory = []
		self.parseStrings()

	def parseStrings(self):
		comprehending = False
		startind = 0
		endind = 0
		choplist = []
		for a in range(0,len(self.li)):
			if '\'' in self.li[a] and not comprehending:
				self.li[a] = self.li[a][self.li[a].index('\'')+1:]+self.li[a][:self.li[a].index('\'')]
				comprehending = True
				startind = a
			elif comprehending:
				if not '\'' in self.li[a]:
					self.li[startind] += (" %s" % self.li[a])
				else:
					self.li[a] = self.li[a][self.li[a].index('\'')+1:]+self.li[a][:self.li[a].index('\'')]
					self.li[startind] += (" %s" % self.li[a])
					comprehending = False
					self.li = self.li[:startind+1] + self.li[a+1:]
					# print self.li
					return self.parseStrings()
		return '¯\_(ツ)_/¯ bush did 9/11 ¯\_(ツ)_/¯'


	def interpret(self):
		computering = True
		while(self.computering):
			# print self.computering
			try:
				self.li.index(str(self.global_index)+'.')
				try:
					self.li.index('.'+str(self.global_index))
					self.execute(self.li.index(str(self.global_index)+'.'),self.li.index('.'+str(self.global_index)))
				except ValueError as e:
					raise StepSyntaxError('you forgot to close operation %d!!' % self.global_index)
			except ValueError as e:
				pass
			self.global_index += 1

	def execute(self, begin, end):
		for index in range(begin+1,end):
			if '?' in self.li[index]:
				if self.memory.pop() != 'yea':
					self.li[index] = 'nu uh'
				else:
					ind = self.li[index].index('?')
					self.li[index] = self.li[index][:ind] + self.li[index][ind+1:]
			if self.li[index] not in reserved_methods and self.li[index] != 'nu uh' and '.' not in self.li[index]:
				self.memory.append(self.li[index])
				# print 'SOMETHING STORED'
			elif self.li[index] == 'output':
				sys.stdout.write(str(self.memory.pop())+'\n')
				# print 'OUTPUT CALLED'
			elif self.li[index] == 'goto':
				test = self.memory.pop()
				try:
					test = int(test)
				except ValueError:
					raise StepSyntaxError("whoa! that goto value is not a number!")
				self.global_index = test
				# print 'GOTO'
			elif self.li[index] == 'end':
				# print 'ENDED'
				self.computering = False
			elif self.li[index] == '+':
				self.memory.append(self.memory.pop() + self.memory.pop())
			elif self.li[index] == '*':
				self.memory.append(self.memory.pop() * self.memory.pop())
			elif self.li[index] == '/':
				self.memory.append(self.memory.pop() / self.memory.pop())
			elif self.li[index] == '-':
				self.memory.append(self.memory.pop() - self.memory.pop())
			elif self.li[index] == '%':
				self.memory.append(self.memory.pop() % self.memory.pop())
			elif self.li[index] == '<':
				if self.memory.pop() < self.memory.pop():
					self.memory.append('yea')
				else:
					self.memory.append('nope')
			elif self.li[index] == '>':
				if self.memory.pop() > self.memory.pop():
					self.memory.append('yea')
				else:
					self.memory.append('nope')
			elif self.li[index] == '==':
				if self.memory.pop() == self.memory.pop():
					self.memory.append('yea')
				else:
					self.memory.append('nope')
			elif self.li[index] == '!=':
				if self.memory.pop() != self.memory.pop():
					self.memory.append('yea')
				else:
					self.memory.append('nope')
			elif self.li[index] == 'input':
				self.memory.append(raw_input())
			elif self.li[index] == 'finput':
				try:
					self.memory.append(int(raw_input()))
				except ValueError:
					raise StepSyntaxError('finput requires you to input a number!!')
			elif self.li[index] == 'dupe':
				self.memory.append(self.memory[len(self.memory)-1])
			elif self.li[index] == 'pause':
				test = self.memory.pop()
				try:
					test = float(test)
				except ValueError as e:
					raise StepSyntaxError('whoops! you need a number for that \"pause\"')

				time.sleep(test)
			# print self.memory

if __name__ == '__main__':
	res = parser.parse_args()
	with open(res.file,'r+') as x:
		m = Interpreter(x.read().replace('\n',' ').replace('\t',' ').split(' '))
		m.interpret()
