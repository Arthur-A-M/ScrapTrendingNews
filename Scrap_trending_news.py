from GoogleNews import GoogleNews
import pandas as pd
whatNews = str(input('De qual país deseja ter noticias? '))
news = GoogleNews(period='1d')
news.search(whatNews)
result = news.result()
data = pd.DataFrame.from_dict(result)
data = data.drop(columns=["img"])
data.head()
print(data)
for i in result:
    print("Title : ", i["title"])
    print("News : ", i["desc"])
    print("Read/watch full news : ", i["link"])
