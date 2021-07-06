#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import threading
import os
import re
from bs4 import BeautifulSoup


class NeteaseCloud(threading.Thread):
    musicData = []
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    cookie = "JSESSIONID-WYYY=mcVQ073zhJq6IPhq48%5CoFSWJeui6tKFkNEynFzw%2F1C%2BnpQhnWWYfsn%2B%2F%2F7G0fa%5CaYJNTP1jzC27aZcaHp1%2FKSsdHozmvfwqcZ6ZKEiWQCKqUZF80FNjgPXlezifIn3a%5CPjfN0Zuqw4ZcFDhCnOpYR4rYZ9%2BtpiS%2FpgoFD%2B%5CptzZcCpQ2%3A1625578746632; _iuqxldmzr_=32; _ntes_nnid=3e0e4d398c420ed792241f283e33be47,1625576946644; _ntes_nuid=3e0e4d398c420ed792241f283e33be47; NMTID=00O-irM2lNPrLd9rE0ItDYX0R_tlEwAAAF6e-_BLA; WEVNSM=1.0.0; WNMCID=eznlap.1625576951098.01.0; WM_NI=uSxeYvDG7A1LJLkIeRen8WZuml7liRn5A2OkcVEwtnXde3Cj3GitISdMcv%2BWBJJW7lNTs%2F%2B7%2FaUWOvkeB1ARkX%2F%2FPDRwtql1jEhHabNyqZZXt54CBQLl%2BQrAWrrHNjqxRHk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee87ae3eb8988b84ae39aeb08fa3c15e979a8faff13a81afa093e121f587e5d6c12af0fea7c3b92ab78db886dc7e8899f9a2b4488a94a5aae85aa7b2f8b8d97fafb4f98dec5aaeeb8fd3ce61a18a8b98f7669cbcabd4c262f199a795cc59a893ad97aa5d829686b8b6688e8cbdd0aa3dedbf9bb8ce7ea9bb8ed2c45aa988e1d0d35092a9bc92ef3baa9ba8a9e46a8ea7bfbbd954b8ebfca4c15b90b4e5b2f14b95aebea9cd62b3a89ea9ea37e2a3; WM_TID=QIhnYd%2Ft519BURFQVUM6zG6avfr%2Bdu4B; __csrf=f3eff20d356d268b34727ecca175d60c; MUSIC_U=70ccb447cc6d97432c66b87de6f0eee6b7c37e654428ade7725b74e9ce09c7e19cb4377b2d7ba249; ntes_kaola_ad=1"

    def __init__(self, threadID, name, counter, url_text):

        self.url_text = url_text
        # 多线程
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

        if not os.path.exists("./music"):
            os.mkdir('./music')

    def __del__(self):
        pass

    def run(self):
        self.musicData = []
        self.musicData = self.getMusicData(
            self.url_text.replace("#/", ""))
        print(u"歌曲获取成功,任务线程开启///")
        self.get(self.musicData)

    def get(self, values):
        downNum = 0
        rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
        for x in values:
            x['name'] = re.sub(rstr, "_", x['name'])
            if not os.path.exists("./music/" + x['name'] + '.mp3'):
                print(
                    '***** ' + x['name'] + '.mp3 ***** Downloading...')

                url = 'http://music.163.com/song/media/outer/url?id=' + \
                      x['id'] + '.mp3'
                try:
                    # urllib.request.urlretrieve(url,'d:/music/' + x['name'] + '.mp3')
                    self.saveFile(url, './music/' + x['name'] + '.mp3')
                    downNum = downNum + 1
                except:
                    x = x - 1
                    print(u'Download wrong~')
        print(
            'Download complete ' + str(downNum) + ' files !')
        pass

    def getMusicData(self, url):

        headers = {'User-Agent': self.user_agent,
                   "Cookie": self.cookie}

        webData = requests.get(url, headers=headers).text
        soup = BeautifulSoup(webData, 'lxml')
        find_list = soup.find('ul', class_="f-hide").find_all('a')

        tempArr = []
        for a in find_list:
            music_id = a['href'].replace('/song?id=', '')
            music_name = a.text
            tempArr.append({'id': music_id, 'name': music_name})
        return tempArr

    def saveFile(self, url, path):
        headers = {'User-Agent': self.user_agent,
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   "Cookie": self.cookie,
                   'Upgrade-Insecure-Requests': '1'}
        response = requests.get(url, headers=headers)
        with open(path, 'wb') as f:
            f.write(response.content)
            f.flush()


def main():
    n = NeteaseCloud(1, "Thread-1", 1, "https://music.163.com/playlist?id=6845925374&userid=121988863")
    n.run()
    n.start()


if __name__ == '__main__':
    main()
