import urllib.request
import os



#读取url,返回一个html对象
def url_open(url):
	rq = urlib.request.Request(url)
	rq.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0')
	
	proxies = ['39.84.60.47:8118', '117.64.50.166:8118', '171.39.43.183:8123']
    proxy = random.choice(proxies)

    proxy_support = urllib.request.ProxyHandler({'http':proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
	
	response = urllib.request.urlopen(url)
	html = response.read()
	print(html)
	return html

#保存图片
def save_imgs(folder,img_addrs):
	for each in img_addrs:
		file_name = each.split('/')[-1]
		img = url_open(each)
		with open(file_name,'wb') as f:
			f.write(img)


#得到图片主页面的所有img的地址，返回一个list
def find_imgs(url):

	html = url_open(url)
	html = html.decode('utf-8')
	
	img_addrs = []
	a = html.find('img src=')
	
	while a != -1:
		b = html.find('.jpg',a,a + 255)
		if b != -1:
			img_addrs.append(html[a + 9:b + 4])
		else:
			b = a + 9
		a = html.find('img src=',b)
		
	return img_addrs
	
	
#得到图片的主页面，返回一个页码的字符串	
def imgPage(url):
	html = url_open(url)
	html = html.decode('utf-8')
	a = html.find('current-comment-page') + 23
	b = html.find(']', a)
	return html[a:b]

#主函数

def download_mm(folder = 'xxoo',pages = 2):
	os.mkdir(folder)
	os.chdir(folder)
	url = "http://jandan.net/ooxx/"
	img_page = imgPage(url)
	img_page = int(img_page)
	for i in range(pages):
		print(i)
		img_page -= i
		page_url = url + 'page-' + str(img_page) + '#comments'
		img_addrs = find_imgs(page_url)
		save_imgs(folder, img_addrs)
		
	
		
if __name__ == '__main__':
	download_mm()
	