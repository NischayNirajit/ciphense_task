from bs4 import BeautifulSoup
import requests
from tkinter import *
import sys
def place_values1():
	search_query(entry_value1.get())
def place_values2():
	search_query(entry_value2.get())
def place_values3():
	search_query(entry_value3.get())
def place_values4():
	search_query(entry_value4.get())
def place_values5():
	search_query(entry_value5.get())
def place_values6():
	search_query(entry_value6.get())
def place_values7():
	search_query(entry_value7.get())
def place_values8():
	search_query(entry_value8.get())

def search_query(sentence):
	if len(sentence) > 300:
		sentence = sentence[1:298]
	query = 'https://en.wikipedia.org/w/index.php?search=+'+sentence
	response = requests.get(query)
	soup = BeautifulSoup(response.text, 'html.parser')
	for div in soup.findAll('div', attrs={'class':'mw-search-result-heading'}):
		link = div.find('a')['href']
		address.append(link)

def check_link_frequency():
	m = 0;
	get_link = None
	for i in address:
		c = address.count(i)
		if c>m :
			m = c
	if m>1:
		get_link = max(address, key = address.count)
	else:
		get_link = address[0]
	get_link = 'https://en.wikipedia.org'+get_link
	final_url = Label(root, text = "final wiki link: ")
	final_url.grid(row = 10, column = 0)

	label1 = Label(root)
	label1["text"] = get_link
	label1.grid(row = 10, column= 1)


root = Tk()

root.title("User input area")
url_label1 = Label(root, text = "Enter the query: ")
entry_value1 = Entry(root, width = 50)
click_button1 = Button(root, text = "search", command =  place_values1)

url_label2 = Label(root, text = "Enter the query: ")
entry_value2 = Entry(root, width = 50)
click_button2 = Button(root, text = "search", command =  place_values2)

url_label3 = Label(root, text = "Enter the query: ")
entry_value3 = Entry(root, width = 50)
click_button3 = Button(root, text = "search", command =  place_values3)

url_label4 = Label(root, text = "Enter the query: ")
entry_value4 = Entry(root, width = 50)
click_button4 = Button(root, text = "search", command =  place_values4)

url_label5 = Label(root, text = "Enter the query: ")
entry_value5 = Entry(root, width = 50)
click_button5 = Button(root, text = "search", command =  place_values5)

url_label6 = Label(root, text = "Enter the query: ")
entry_value6 = Entry(root, width = 50)
click_button6 = Button(root, text = "search", command =  place_values6)

url_label7 = Label(root, text = "Enter the query: ")
entry_value7 = Entry(root, width = 50)
click_button7 = Button(root, text = "search", command =  place_values7)

url_label8 = Label(root, text = "Enter the query: ")
entry_value8 = Entry(root, width = 50)
click_button8 = Button(root, text = "search", command =  place_values8)

address = []
click_button = Button(root, text = "search", command =  check_link_frequency)



url_label1.grid(row = 0, column = 0)
entry_value1.grid(row = 0, column= 1)
click_button1.grid(row = 0, column= 2)

url_label2.grid(row = 1, column = 0)
entry_value2.grid(row = 1, column= 1)
click_button2.grid(row = 1, column= 2)

url_label3.grid(row = 2, column = 0)
entry_value3.grid(row = 2, column= 1)
click_button3.grid(row = 2, column= 2)

url_label4.grid(row = 3, column = 0)
entry_value4.grid(row = 3, column= 1)
click_button4.grid(row = 3, column= 2)

url_label5.grid(row = 4, column = 0)
entry_value5.grid(row = 4, column= 1)
click_button5.grid(row = 4, column= 2)

url_label6.grid(row = 5, column = 0)
entry_value6.grid(row = 5, column= 1)
click_button6.grid(row = 5, column= 2)

url_label7.grid(row = 6, column = 0)
entry_value7.grid(row = 6, column= 1)
click_button7.grid(row = 6, column= 2)

url_label8.grid(row = 7, column = 0)
entry_value8.grid(row = 7, column= 1)
click_button8.grid(row = 7, column= 2)
click_button.grid(row = 9, column= 0)


root.mainloop()
