#!/usr/bin/python
import unittest
import requests

class Server_API_TestCase(unittest.TestCase):
	def test_00_update_correct(self):
		"Testing if correct cell update returns true"
		r = requests.post('http://localhost:8080/update', data = {'id':'a1', 'value' : 4})
		response = r.json()
		if response['correct'] == True:
			return
		self.fail("Update true value returned false")
		
	def test_01_update_incorrect(self):
		"Testing if incorrect cell update returns false"
		r = requests.post('http://localhost:8080/update', data = {'id':'a1', 'value' : 5})
		response = r.json()
		if response['correct'] == False:
			return
		self.fail("Update false value returned true")
		
if __name__ == "__main__":
	unittest.main(verbosity = 2)