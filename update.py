import requests
import os

# Replace with your Cloudflare API token
API_TOKEN = 'your_api_token_here'
# Replace with your Cloudflare account email
EMAIL = 'your_email@example.com'
# Replace with your domain name
DOMAIN = 'yourdomain.com'
# Replace with your record ID
RECORD_ID = 'your_record_id_here'

def get_public_ip():
    response = requests.get('https://api.ipify.org')
    return response.text

def update_dns(ip):
    url = f'https://api.cloudflare.com/client/v4/zones/{DOMAIN}/dns_records/{RECORD_ID}'
    headers = {
        'X-Auth-Email': EMAIL,
        'X-Auth-Key': API_TOKEN,
        'Content-Type': 'application/json'
    }
    data = {
        'type': 'A',
        'name': '@',
        'content': ip,
        'ttl': 1,
        'proxied': False
    }
    response = requests.put(url, headers=headers, json=data)
    return response.status_code

if __name__ == '__main__':
    new_ip = get_public_ip()
    status = update_dns(new_ip)
    if status == 200:
        print(f'DNS record updated to {new_ip}')
    else:
        print('Failed to update DNS record')
