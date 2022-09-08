import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
import os
import json
# importing the required libraries
import pprint
import json
import warnings
import jsonify
warnings.filterwarnings('ignore')
import pandas as pd

def checkpwd(email,texto):
	df = pd.read_csv('static/data/users.csv',encoding='utf-8-sig')
	print(df)
	for i in range(len(df)):
		user = 'no'
		pawd = 'no'
		numero = 0
		print ("si "+email+" es igual a "+df.loc[i][1])
		if str(df.loc[i][1]) == email:
			user = 'ok'
			numero = i
			print ("si "+texto+" es igual a "+df.loc[i][2])
			if df.loc[numero][2] == texto:
				pawd = 'ok'
				break

	if user == 'ok' and pawd == 'ok':
		return (df.loc[numero][0],df.loc[numero][3])
	else:
		return('Error','Error')
