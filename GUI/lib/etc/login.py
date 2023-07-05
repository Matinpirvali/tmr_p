import requests

ul = 'https://raw.githubusercontent.com/BDadmehr0/tmr_p_SQL/main/permum.json?token=GHSAT0AAAAAACC5JLWXK66MPKEN624VBOMAZFFTA6Q'
res = requests.get(ul)
print(res.text)
