import requests
from bs4 import BeautifulSoup


# roll_no='24930'
# level='0502'
# exam_year='1446'

# roll_no='18037'
# level='0601'
# exam_year='1447'

roll_no='33929'
level='0502'
exam_year='1447'

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
})

# Get form page
form_url = 'https://www.wifaqulmadaris.org/Results/Infradi'
resp = session.get(form_url)

# Extract token
soup = BeautifulSoup(resp.text, 'html.parser')
token = soup.find('input', {'name': '__RequestVerificationToken'}).get('value')

# Submit form
post_url = 'https://www.wifaqulmadaris.org/Results/RptInfradi'
data = {
    '__RequestVerificationToken': token,
    'Gender': 'M',
    'Examtype': 'A',
    'ExamYear': exam_year,
    'DarjaID': level,
    'Rolno': roll_no,
    'Submit': ''
}

response = session.post(post_url, data=data, headers={'Referer': form_url})

# Save result
filename = f'result_{roll_no}.html'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(response.text)

print("Result saved to result.html")