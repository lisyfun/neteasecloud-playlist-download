# neteasecloud-playlist-download

网页云歌单下载

代码结构如下
```
├── README.md
└── src
    ├── main.py
    └── music
```
1. 选中自己想要下载的歌单 -> 分享 -> 复制链接 
<img width="1002" alt="图片" src="https://user-images.githubusercontent.com/76048823/124612598-0af91c00-dea5-11eb-904a-fe24efa715d8.png">

2. 在main.py中87行,将url替换成从第一步复制到的歌单链接
<img width="946" alt="图片" src="https://user-images.githubusercontent.com/76048823/124614520-e605a880-dea6-11eb-90da-08c1db772248.png">

3. 从第一步复制到的歌单链接复制到谷歌浏览器中,使用手机网易云扫码登陆(如果不登陆默认只能下载前10首歌)

未登陆:
<img width="1250" alt="图片" src="https://user-images.githubusercontent.com/76048823/124612442-e8670300-dea4-11eb-9f7a-0d78479d300a.png">
已登陆:
<img width="1226" alt="图片" src="https://user-images.githubusercontent.com/76048823/124613078-74792a80-dea5-11eb-9199-1c9d2f8f56a6.png">


4. F12进入控制台,刷新一下页面
<img width="1431" alt="图片" src="https://user-images.githubusercontent.com/76048823/124614220-9b842c00-dea6-11eb-85b6-3a7345251a80.png">

5. 修改代码中13行的cookie值,为第三步中复制到的cookie
<img width="948" alt="图片" src="https://user-images.githubusercontent.com/76048823/124614656-0d5c7580-dea7-11eb-82c8-b063df7f3291.png">

6. 执行代码,`python neteasecloud-playlist-download/src/main.py`, 
 等待控制台输出`Download complete` 即可看到 `neteasecloud-playlist-download/src/muisc` 目录下生成的mp3文件;
 (如果文件格式有问题,不是正确的mp3文件,是由于该歌曲版权问题导致的)
