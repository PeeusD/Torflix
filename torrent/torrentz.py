import requests
from bs4 import BeautifulSoup  


def torrent_api():

    torrent_results = input('Enter here to search: ')
    print(f"Searching {torrent_results} Please Wait....")
    torrent_results.replace(' ', '+')
    response = requests.get(f'https://torrentz2.pics/data.php?q={torrent_results}')
    # print(r.status_code)
    try:
            soup = BeautifulSoup(response.text,'html.parser')
            contents = soup.find('table', class_ = 'table')
            res = {}
            
            for content in contents.find_all('tbody'):
                rows = content.find_all('tr')
                # print(rows[5])
                i=0
                for row in rows:
                    udt = []
                    res_lst = []
                    movie_name = row.find('span').text  #movie name
                    leeches = row.find('td', attrs={ 'data-title':'Leeches'}).text # no. of leeches
                    for seed in row.findAll('td', attrs={ 'data-title':'Last Updated'}):  #no. of seeders and last updt
                        udt.append(seed)
                    last_updt = (str(udt[0])).strip('<td class="age-data" data-title="Last Updated"></td>')  #last updated
                    seeds = (str(udt[1])).strip('<td data-title="Last Updated"></td>') #seeds
                    file_size = row.find('td', attrs={ 'data-title':'Size'}).text  #file size
                    magnets = row.find('a').get('href') #magnet links
                    i=i+1
                    
                    res_lst.extend([movie_name, leeches, seeds, file_size, last_updt, magnets])  #appending multiple values into res_lst...
                    res[i] = res_lst
            print(res)
            return res
    except Exception as e:
        #print('Result not found, Error: ',e)     
        return e


# torrent_api()  # DEBUGGING