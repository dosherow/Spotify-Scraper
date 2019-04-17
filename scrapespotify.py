# creating spotify charts scraper
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
from time import time
from time import sleep
from random import randint
import pandas as pd


base_url = 'https://spotifycharts.com/regional/global/daily/'
start = date(2017, 1, 1)
end = date.today()
skip = {date(2017, 2, 23), date(2017, 5, 30), date(2017, 5, 31), date(2017, 6, 2),
        date(2017, 7, 20), date(2017, 7, 21), date(2017, 7, 22), date(2017, 7, 23),
        date(2017, 11, 9), date(2017, 11, 10), date(2017, 11, 11), date(2017, 11, 12),
        date(2017, 11, 13), date(2017, 11, 14), date(2017, 12, 1), date(2019, 4, 5)}
iter = timedelta(days=1)

start_time = time()
serve = 0

mydate = start

while mydate < end:

    while mydate in skip:
        mydate += iter

    if(mydate > end):
        break

    r = requests.get(base_url + mydate.strftime('%Y-%m-%d'))
    mydate += iter

    #pause the loop
    sleep(randint(1,3))

    # monitor requests
    serve += 1
    elapsed_time = time() - start_time









# pulling website url request and setting variable

# r = requests.get("https://spotifycharts.com/regional")

# using bs4 to create variable to clean up site content

    soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

#getting data by looking for each row
#establishing table variable 'chart' by finding element from html

    # chart = soup.find('table', {'class': 'chart-table'})
# print(chart)

# establishing where data we are interested starts and ends
#     tbody = chart.find('tbody')
# print(tbody)

# get ranks for daily

    chart = soup.find('table', {'class': 'chart-table'})

    tbody = chart.find('tbody')

    all_rows = []

    for tr in tbody.find_all('tr'):

        rank_text = tr.find('td', {'class': 'chart-table-position'}).text
    # print(rank_text)

    # for tr in tbody.find_all('tr'):

# rank_text = []
# rank_text_elem = soup.find_all('td', {'class': 'chart-table-position'})

    # print(rank_text_elem)

        # for item in rank_text_elem:
        #     rank_text.append(item.text)
            # print(rank_text)

        artist_text = tr.find('td', {'class': 'chart-table-track'}).find('span').text
        artist_text = artist_text.replace('by ','').strip()
        # print(artist_text)

    # for item in artist_text_elem:
    #     artist_text.append(item.text.replace('by ','').strip())
    #     print(artist_text)

        title_text = tr.find('td', {'class': 'chart-table-track'}).find('strong').text


        # print(title_text)

        streams_text = tr.find('td', {'class': 'chart-table-streams'}).text

        date = (mydate - iter)

        all_rows.append( [rank_text, artist_text, title_text, streams_text, date.strftime('%Y-%m-%d')] )
        # print(streams_text)

    # create dataframe array to store all data


    df = pd.DataFrame(all_rows, columns =['Rank','Artist','Title','Streams', 'Date'])
    print(df)

    with open('200chart.csv', 'a') as f:
        df.to_csv(f, header=False, index=False)

    # with open("spotify_data.csv", "a") as f:
    #     f.write(df)
    # dff = pd.read_csv('spotify.csv')
# artist_text = []
# artist_text_elem = soup.find_all('td', {'class': 'chart-table-track'}).find_all('span')
# print(artist_text_elem)
        #
        # for item in artist_text_elem:
        #     artist_text.append(item.text.replace('by ','').strip())
        #     print(artist_text)
        #
        # title_text = []
        # title_text_elem = tr.find(class_='chart-table-track').find_all('strong')
        #
        # for item in title_text_elem:
        #     title_text.append(item.text)
    #
    #     rank_text = []
    #     rank_text_elem = tr.find('td', {'class': 'chart-table-position'})
    #
    #     for item in rank_text_elem:
    #         rank_text.append(item)
    #
    #
    #
    #     artist_text = []
    #     artist_text_elem = tr.find('td', {'class': 'chart-table-track'}).find_all('span')
    #
    #     for item in artist_text_elem:
    #         artist_text.append(item.text.replace('by ','').strip())
    #
    #
    #
    #     title_text = []
    #     title_text_elem = tr.find('td', {'class': 'chart-table-track'}).find_all('strong')
    #
    #     for item in title_text_elem:
    #         title_text.append(item.text)
    #
    #     streams_text = []
    #     streams_text_elem = tr.find('td', {'class': 'chart-table-streams'})
    #
    #     for item in streams_text_elem:
    #         streams_text.append(item)
    #
    # # create dataframe to store table
    #
    #     final_array = []
    #
    #     for rank, artist, title, streams in zip(rank_text,artist_text,title_text,streams_text):
    #         final_array.append({'Rank':rank,'Artist':artist,'Title':title,'Streams':streams})
    #
    #     df = pd.DataFrame(final_array)
    #     print(df)
    #
    #     df.to_csv('spotify.csv', sep=',', encoding='utf-8', index=False)
    #     dff = pd.read_csv('spotify.csv')



# finding and setting variables for each element in our list we want to scrape
#     for tr in tbody.find_all('tr'):
#         rank = tr.find_all('td', {'class': 'chart-table-position'})[0].text.strip()
#         artist = tr.find_all('td', {'class': 'chart-table-track'})[0].find_all('span')[0].text.replace('by ','').strip()
#         title = tr.find_all('td', {'class': 'chart-table-track'})[0].find_all('strong')[0].text.strip()
#         streams = tr.find_all('td', {'class': 'chart-table-streams'})[0].text.strip()
        # print(rank, artist, title, streams










