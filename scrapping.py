import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager(retries = False)
check_word_list = ['hundar','dogs','dog','koerad','koirat','hunde','hunder','cães','собака','psy','honden','Σκύλοι']
r = open('/home/radiohead/websites777.txt', 'r', encoding='utf-8')
website_list = r.read().split()
for url in website_list:
    try:
        response = http.request('GET',url)
        soup = BeautifulSoup(response.data,'lxml')
        content = soup.get_text().split()
        for check_word in check_word_list:
            if check_word in content:
                print(url)
    except:
        pass







