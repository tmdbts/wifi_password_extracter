import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

wifi_list = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

for wifi in wifi_list:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', wifi, 'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if 'Key Content' in line]
    
    try:
        print(f'Name: {wifi}, Password: {results[0]}')
    except IndexError as identifier:
        print(f'Name: {wifi}, Password: Cannot be read.')