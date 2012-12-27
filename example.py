#!/usr/bin/env python
# -*- coding: utf-8 -*-

class pressure:
	def __init__(self, tap, default=0, multiplier=1.25, max_=20):
		self._parent = tap
		self._pressure = default
		self._multiplier = multiplier
		self._max = max_

	def increase(self, multiplier=None):
		if multiplier is None:
			multiplier = self._multiplier
		self._pressure *= multiplier
		if self._pressure > self._max:
			self._parent.explode()

	def decrease(self, multiplier=None):
		if multiplier is None:
			multiplier = self._multiplier
		self._pressure /= multiplier
		if self._pressure == 0:
			self._parent.stop()

	def get(self):
		return self._pressure

	def set(self, new):
		self._pressure = new


class tap:
	def __init__(self, run=True):
		self.pressure = pressure(self)
		self.say("I'm a tap!")
		if run:
			self.run()

	def run(self):
		if self.pressure.get() != 0:
			self.say("I'm already running!")
			return
		self.pressure.set(4)
		self.say("Catch me if you can!")

	def stop(self):
		if self.pressure.get() == 0:
			self.say("I'm not running!")
			return
		self.pressure.set(0)
		self.say("I've stopped!")

	def explode(self):
		self.pressure.set(0)
		self.say('BANG!')

	def say(self, *what):
		print ' '.join(what)