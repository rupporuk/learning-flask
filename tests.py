#!/usr/bin/env python
import requests
import os
import unittest

endpoint = os.getenv("CHATTYBOT_ENDPOINT")


class BaseEndpoint(unittest.TestCase):
    def test(self):
        r = requests.get(endpoint + '/')
        self.assertEqual(r.status_code, 200)


class HealthEndpoint(unittest.TestCase):
    def test(self):
        r = requests.get(endpoint + '/health')
        self.assertEqual(r.status_code, 200)


class SpeakEndpoint(unittest.TestCase):
    def test(self):
        r = requests.get(endpoint + '/input/test')
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
