from flask import Flask
import requests

#app = Flask(__name__)

# TODO
# 1. прием сообщения
# 2. отсылка

URL = 'https://api.telegram.org/bot589971495:AAEq6WKJ1A97zg3ympZ6fGbTL03JMn15_cg'


def main():
	r = requests.get(URL = 'getMe')
	print(r.json())
	

if __name__ == '__main__':
	main()