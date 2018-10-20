from urllib import request,parse
import json

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' % (k,v))
#     print('Data:',data.decode('utf-8'))

# print('Login to weibo.com')
# email = input('Email:')
# passwd = input('Password:')
# login_data = parse.urlencode([
#     ('username',email),
#     ('password',passwd),
#     ('entry','nweibo'),
#      ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin','https://passport.weibo.cn')
# req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer','https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
# with request.urlopen(req,data=login_data.encode('utf-8')) as f:
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' % (k,v))
#     print("Data:",f.read().decode('utf-8'))

# proxy_handler = request.ProxyHandler({'http':'http://www.example.com:3128/'})
# proxy_auth_handler = request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm','host','username','password')
# opener = request.build_opener(proxy_handler,proxy_auth_handler)
# with opener.open('http://www.example.com/login.html') as f:
#     data = f.read()
#     print(data)


def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
        rdata = json.loads(data)
        # print("Data:",data)
        print("Json Data:",rdata)

    return rdata
# 测试   
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'