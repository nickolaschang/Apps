import os

from woocommerce import API


def setup_api(filename):
	filepath = os.getcwd()
	filename = filename
	set_timeout = None

	if filename in os.listdir(filepath):
		print('File Found, Credentials Ready...')
		with open(filename, mode='r') as file:
			credentials = file.read().split(',')
			url = credentials[0]
			consumer_key = credentials[1]
			consumer_secret = credentials[2]
			while True:
				print(f"""
				Current URL: {url}
				Current Consumer Key: {consumer_key}
				Current Consumer Secret: {consumer_secret}
				Timeout set to {set_timeout}. If None is selected it will be defaulted to 240 seconds.
				Please check if the information is correct before proceeding.						
				""")
				information_is_correct = input('Would you like to proceed? (yes/no): ')
				if information_is_correct.lower() == 'yes':
					print('Product API ready to use.')
					break
				elif information_is_correct.lower() == 'no':
					with open(filename, mode='w') as file:
						url = input("Enter the API URL from Woocommerce: ")
						consumer_key = input("Enter the API consumer key from Woocommerce: ")
						consumer_secret = input("Enter the API consumer secret from Woocommerce: ")
						file.write(f"{url},{consumer_key},{consumer_secret}")
						print('Credentials Fixed Successfully.')
						break
				else:
					print('Invalid Option. Please try again.')
	elif filename not in os.listdir(filepath):
		print('File not found, creating...')
		with open(filename, mode='w') as file:
			url = input("Enter the API URL from Woocommerce: ")
			consumer_key = input("Enter the API consumer key from Woocommerce: ")
			consumer_secret = input("Enter the API consumer secret from Woocommerce: ")
			timeout_option = input('Set Timeout? yes/no: ')
			if timeout_option.lower() == 'yes':
				set_timeout = input('Enter the timeout value (in seconds): ')
				file.write(f"{url},{consumer_key},{consumer_secret},{set_timeout}")
			else:
				set_timeout = None
				file.write(f"{url},{consumer_key},{consumer_secret}")

	wcapi = API(
		url=url,
		consumer_key=consumer_key,
		consumer_secret=consumer_secret,
		version='wc/v3',
		timeout=int(set_timeout) if set_timeout else 240
	)

	return wcapi


credentials_file_check = input('Before Continuing the program will check if the credentials file'
                               ' is present in the current working directory.\n'
                               'Please enter the file name: ').lower() + '.csv'
wcapi = setup_api(credentials_file_check)

while True:
	menu_option = input('The API validation has completed, select an option to continue:\n'
	                    '--> 1. Products Menu \n'
	                    '--> 2. Orders Menu\n'
	                    '--> 3. Check Credentials File Again\n'
	                    '--> 4. Exit\n'
	                    '--> Selected Option: ')
	if menu_option == '1':
		pass
	elif menu_option == '2':
		pass
	elif menu_option == '3':
		pass
	elif menu_option == '4':
		break
	else:
		print('Invalid option.')
