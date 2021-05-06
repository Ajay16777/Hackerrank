def fun(s):
	try:
		username, other = s.split('@')
		websitename,exetanson = other.split('.')
	except ValueError:
		return False

	if username.replace('_','').replace('-','').isalnum() is False:
		return False
	elif websitename.isalnum() is False:
		return False
	elif len(exetanson) > 3:
		return False
	else:
		return True