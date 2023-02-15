import retrieve as re 

def get_data(page = 1):
	store = {}
	page = str(page)
	url = "https://www.vinabook.com?q=&page=" + page
	print("\n----------------------- Page " + page + " -----------------------\n")
	soups = re.get_resource(url)
	store["data"] = re.save_data(soups)
	store["url"] = url
	re.data_to_csv(store, page)

def main():
	page = int(input("Pages to crawl: "))
	for i in range(page):
		get_data(i+411)

if __name__ == '__main__':
	main()
	print('done')