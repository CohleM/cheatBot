from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.set_window_position(0, 0)
driver.set_window_size(1300, 768)


def GoogleSearch(query):
	page = 1
	url = "http://www.google.com/search?q=" + query + "&start=" +      str((page - 1) * 10) 
	driver.get(url)
	driver.get_screenshot_as_file("screenshot.png")
	print('executed')

def returnLinks(query):
	n_pages = 2
	links = []
	for page in range(1,n_pages):		
		url = "http://www.google.com/search?q=" + query + "&start=" +      str((page - 1) * 10) 
		driver.get(url)
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		search = soup.find_all('div',class_ = "yuRUbf")
		for h in search:
			links.append(h.a.get('href'))
			
	return links

def getfullscreenshot(query, num):
	links = returnLinks(query)
	url = links[num - 1]
	driver.get(url)
	S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)	
	driver.set_window_size(S('Width'),S('Height'))
	driver.find_element_by_tag_name('body').screenshot('full_screenshot.png')
	print('executed  yoo ')















	


GoogleSearch('How to make a new boyfriend')
