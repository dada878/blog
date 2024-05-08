# CSS 動畫如何從中途開始播放
## 前言
事情是這樣的，前陣子在開發的網頁背景有個星空，於是就想說不如來加點星空的閃爍特效吧！

於是就先寫了這樣的 CSS：

![alt text](https://github.com/dada878/blog/blob/master/assets/dddimage-3.png?raw=true)

不過這樣當然是不夠的，每個星星同時閃爍太不自然了，於是我加了一點隨機的 delay：

![alt text](https://github.com/dada878/blog/blob/master/assets/dddimage-2.png?raw=true)

看起來是會隨機閃爍了，但在頁面剛載入進去的時候因為很多星星都還在 delay 中，畫面特別的空虛。這時候我就想了，有沒有可能讓 CSS 動畫從中途開始播放？

上網一查，原來還真的可以！

只要把 `animation-delay` 的值改成負數就行了！比如說 `animation-delay: -3s` 就是指從 3 秒開始的動畫。於是最後我把程式碼改成了這樣：

![alt text](https://github.com/dada878/blog/blob/master/assets/dddimage.png?raw=true)

~~GIF 錄起來品質好像不是很好，但還是放一下好了~~

![](https://github.com/dada878/blog/blob/master/assets/daydream_demo.gif?raw=true)