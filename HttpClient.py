import http.cookiejar, urllib, urllib.request, urllib.error, socket,time


class HttpClient:
    __cookie = http.cookiejar.LWPCookieJar('cookie/cookie.data')
    # replace line 9 with line 7 and 8 will enable the request report of urllib
    # logprint=urllib.request.HTTPHandler(debuglevel=1)
    # __req = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(__cookie),logprint)
    __req = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(__cookie))
    __req.addheaders = [
        ('Accept', 'application/javascript, */*;q=0.8'),
        ('User-Agent',
         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"),
        ('Referer', 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1')
    ]
    urllib.request.install_opener(__req)

    def __init__(self):
        try:
            self.__cookie.load(ignore_discard=True,ignore_expires=True)
        except Exception:
            self.__cookie.save(ignore_discard=True,ignore_expires=True)

    def getTimeStamp(self):
        return str(int(time.time()*1000))

    def Get(self, url, refer=None):
        try:
            # print("requesting " + str(url) + " with cookies:")
            # print(self.__cookie)
            req = urllib.request.Request(url)
            # if not (refer is None):
            #     req.add_header('Referer', refer)
            req.add_header('Referer', 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1')
            # print(req.headers)
            tmp_req = urllib.request.urlopen(req)
            self.__cookie.save('cookie/cookie.data',ignore_discard=True,ignore_expires=True)
            return tmp_req.read().decode('UTF-8')
        except urllib.error.HTTPError as e:
            return e.read()

    def GetDownload(self, url, refer=None, path=""):
        try:
            # print("requesting " + str(url) + " with cookies:")
            # print(self.__cookie)
            req = urllib.request.Request(url)
            if not (refer is None):
                req.add_header('Referer', refer)
            # req.add_header('Referer', 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1')
            # print(req.headers)
            tmp_req = urllib.request.urlopen(req)
            print("start download")
            pic = tmp_req.read()
            try:
                File = open(path, 'wb')
                File.write(pic)
                File.close()
            except:
                print("download failed")
                return
            self.__cookie.save('cookie/cookie.data',ignore_discard=True,ignore_expires=True)
            return tmp_req.read().decode('UTF-8')
        except urllib.error.HTTPError as e:
            return e.read()

    def Post(self, url, data, refer=None):
        try:
            # print("requesting " + str(url) + " with data:")
            # print(data)
            # print("Cookies: ")
            # print(self.__cookie)
            req = urllib.request.Request(url, urllib.parse.urlencode(data).encode('UTF-8'))
            if not (refer is None):
                req.add_header('Referer', refer)
            req.add_header('Referer', 'http://d1.web2.qq.com/proxy.html?v=20151105001&callback=1&id=2')
            # print("Headers: ")
            # print(req.headers)
            tmp_req = urllib.request.urlopen(req, timeout=180)
            self.__cookie.save('cookie/cookie.data',ignore_discard=True,ignore_expires=True)
            return tmp_req.read().decode('UTF-8')
        except urllib.error.HTTPError as e:
            return e.read()

    def Download(self, url, file):
        output = open(file, 'wb')
        output.write(urllib.request.urlopen(url).read())
        output.close()

    #  def urlencode(self, data):
    #    return urllib.quote(data)

    def dumpCookie(self):
        for c in self.__cookie:
            print(c.name,'=',c.value)

    def getCookie(self, key):
        for c in self.__cookie:
            if c.name == key:
                return c.value
        return ''

    def setCookie(self, key, val, domain):
        ck = http.cookiejar.Cookie(version=0, name=key, value=val, port=None, port_specified=False, domain=domain,
                              domain_specified=False, domain_initial_dot=False, path='/', path_specified=True,
                              secure=False, expires=None, discard=True, comment=None, comment_url=None,
                              rest={'HttpOnly': None}, rfc2109=False)
        self.__cookie.set_cookie(ck)
        self.__cookie.save(ignore_discard=True,ignore_expires=True)
        # self.__cookie.clear() clean cookie
        # vim : tabstop=2 shiftwidth=2 softtabstop=2 expandtab
