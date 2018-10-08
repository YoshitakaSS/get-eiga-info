import urllib.request, urllib.error
import requests
import re # 正規表現用のライブラリ
import datetime # 日時用のライブラリ
import pandas as pd # csv用のライブラリ
from bs4 import BeautifulSoup

# アクセスするURL
url = "https://eiga.com/now/";

# rootのURL
# 取得したURLの前に「/」が付いているため、rootでは外す
rootUrl = "https://eiga.com";

# 次ページの取得するためのURL
# nextUrl = 

# アクセスしたURLのHTML要素を取得
res = requests.get(url);

# 公開している日付の取得
now = datetime.date.today();

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(res.text, "html.parser");

# 映画コンテンツを取得する
contents = soup.find_all(class_="m_unit");

# 次ページのコンテンツを取得する
pagination = soup.find(class_="pagination");

def getNextContent(pagination):
	# 次ページにリンクを取得する
	for paginations in pagination:
		nextLinkParts = paginations.get('href');
		if nextLinkParts is None:
			continue;
		# 次ページの画面URL
		nextLink = rootUrl + nextLinkParts;

		# 次のページの画面URLにアクセスする
		res = requests.get(nextLink);

		soup = BeautifulSoup(res.text, "html.parser");

		contents = soup.find_all(class_="m_unit");

		for content in contents:

			title = content.find('h3');
			link = content.find('a');
			print('Title:' + str(title.string) + ' Link:' + rootUrl + str(link.get('href')));
			print("###############################");

		print(rootUrl + nextLink + "の情報を取得");
		print("###############################");


getNextContent(pagination);


columns = ["Date", "Title", "Link"];
df = pd.DataFrame(columns=columns);


# for eigaContents in contents:
# 	title = eigaContents.find('h3');
# 	link = eigaContents.find('a');

# 	# 映画詳細のURLを取得する
# 	detailLink = rootUrl + link.get('href');

# 	# 映画のタイトルとURLを出力する
# 	print(now);
# 	print('Title:' + str(title.string) + ' Link:' + detailLink);
# 	print("###############################");

# 	# CSVの方式に加工
# 	csv = pd.Series([now, str(title.string), detailLink], columns);
# 	df = df.append(csv, columns);

	
# if contents:
# 	print(url + "からコンテンツを取得");
# 	df.to_csv("eiga.csv", encoding="shift_jis");

# else:
# 	print("コンテンツを取得できませんでした");

# # except requests.HTTPError as e:
# # 	print(url + "において " +str(e.code));




