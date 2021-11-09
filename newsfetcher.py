#need to import requests package
import requests

def NewsFromAPI():

    #source, sortBy and apiKey
    query_params = {
        "source": "NewsAPI",
        "sortBy": "top",
        "apiKey": "71043e61097a4919bfa8fc68c5c9dea8"
    }
    main_url = "https://newsapi.org/v1/articles"

    #fetching data in json format
    res = requests.get(main_url, params= query_params)
    open_NewsApi_page = res.json()

    #getting all articles in a sting article
    article = open_NewsApi_page["articles"]

    #empty list which will contain all trending news
    results= []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):

        #printing all trending news
        print(i + 1, results[i])

    #to read the news out loud for us
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)

    if __name__ == '__main__':
        NewsFromAPI()