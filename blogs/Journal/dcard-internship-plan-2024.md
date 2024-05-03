# Dcard 實習計畫 2024
## 機緣
這次去 SITCON 玩大地遊戲的時候，剛好在 Dcard 攤位看到正在招募 2024 暑期實習計畫的實習生，於是我就過去了跟他們聊了一下，沒想到他們竟然說高中生只要有時間也可以來報名看看，身為自學生的我怎麼能錯過這樣的機會呢！

## 作業
按照實習計畫的說明，在投遞履歷的同時，還需要附上「作業」，而這次的作業內容大概就是要建立一個可登入、發文然後串 Github API 的 blog 網頁。

![alt text](https://github.com/dada878/blog/blob/master/assets/dimage-10.png?raw=true)

我在開始製作這個作業時，其實對於 React 的了解其實幾乎趨近於零，沒有抱持的太大的期待就開始做下去了，想說就透過這個作業邊寫邊學 React 和 Next.js。

過程中其實遇到不少困難，起初就是 `useEffect` 用得太差，導致出現一堆問題，網路上查了許多資料都沒辦法完美的解決我遇到的困難，直到發現了 [A Complete Guide to useEffect](https://overreacted.io/a-complete-guide-to-useeffect/) 這篇文章，對英文不是很好的我來說，這超長的文章大概也花了我兩天的時間才讀完。幸運的是，這篇文章寫得非常詳細而且解決了我遇到的問題，感覺我就是基礎很不扎實吧。

![alt text](https://github.com/dada878/blog/blob/master/assets/dimage-2.png?raw=true)

除了 `useEffect` 以外，還遇到另外一個更棘手的就是 Next.js 的快取問題，每當我發布 blog 文章之後，無論怎麼重新載入我的文章都不會顯示出來。翻了 Next.js 的文件才發現快取系統怎麼這麼複雜，總之後來又花了一些時間把 Next.js 的文件都好好讀一一讀，最終稍微解決了這個問題，但解法似乎不是非常優雅。

繳交期限最後一週，我參考了之前 [某個被錄取的實習生的作業](https://github.com/5j54d93/Dcard-2022-Web-Frontend-Intern-Homework) 寫好了 `README.md` 文件就交上去了。如果有興趣的話，你可以在 [這裏](https://github.com/dada878/dcard-homework) 看到我當時的作業，總共 320 個 commits，我花了整整一個月的時間在上面。

## 面試準備

作業繳交上去幾天後，很順利的收到了面試通知，那時候看到這個超開心！

![alt text](https://github.com/dada878/blog/blob/master/assets/dimage.png?raw=true)

距離面試時間，還有兩週多，首先我上網查了一些資訊，看看之前的 Dcard 面試到底都做了什麼。因為某篇文章說建議去讀 React 底層的東西，於是我就找了 [React 技術揭密](https://react.iamkasong.com/) 這本電子書來讀，裡面真的提到了非常多很底層的東西，像是什麼 fiber node 之類的，不過最後還是看不太懂qwq，因此放棄了這本書。

或許對我來說 React 底層太難了，但我至少可以繼續增進我對 React 的了解，根據前面 Next.js 的學習經驗，我決定要把 React 的文件全部讀過一遍！

還在 Obsidian 整理了蠻多的筆記，感覺有機會可以公開出來。

![alt text](https://github.com/dada878/blog/blob/master/assets/dimage-4.png?raw=true)

大約一週的時間，我把 React 讀得差不多了，過程中其實發現了不少作業中可以優化的地方也改上去了。然後又再回去看一下之前面試的考古題，發現我對 Javascript 的了解似乎也不夠深，尤其時原型練之類的東西。最後根據 [某 Javascript 大師](https://YuRen-tw.github.io) 的推薦，讀了 [這個系列](https://openhome.cc/zh-tw/javascript/basics/) 的文章，真的挺優質的，很多其他地方看不到的內容裡面都有。這部分我比較多的時間可能都還是在研究原型鏈。

![alt text](https://github.com/dada878/blog/blob/master/assets/dimage-6.png?raw=true)

接下來也花了一些時間學 git 更進階的指令，[這個網站](https://learngitbranching.js.org/) 真的挺有意思的，到後面感覺很像在玩解謎遊戲。

![alt text](https://github.com/dada878/blog/blob/master/assets/dimage-7.png?raw=true)

git 的部分也整理了一些筆記，不過沒 React 那麼多就是了。

![alt text](https://github.com/dada878/blog/blob/master/assets/dimage-9.png?raw=true)

面試前兩三天，繼續查了一下考古題，看看 HR 面試的關卡會做什麼，但好像也沒查到什麼太有用的資訊。結果反而有點不知道要做什麼，於是就去處理了一些雜事，把之前 side project 想加的東西加上去、把還沒發佈的 chrome extension 給 publish 上去有的沒的。

## 面試當天

大概提前兩個多小時左右就先到了現場，看一下面試地點大概在什麼地方，然後去吃個午餐休息一下，本來想再複習一下結果好像來不及了。進公司之後，他們先跟我介紹了一下 Dcard 的歷史，然後參觀一下工作環境（看起來真的很舒服）。接著迎來的第一關就是 HR 面試。

其實氛圍還算滿輕鬆的，不過我還是有點緊張。剛開始有跟他們聊了一下關於我現在自學生的身份和接下來的升學打算，後來還有提到問我是如何學習一項新的技術、以及程式學習的歷程，然後問我短中長期規劃之類的。因為我個人網站上面寫了很多比賽的經歷，他們也根據這個詢問了我一些相關問題，比如為什麼想參加這些比賽、跟隊友賽中的策略怎麼樣等等，在小組合作過程當中的協作模式、有沒有遇過衝突及如何化解有的沒的。

這邊其實我覺得很多問題我都沒有回答得很好，或者是思考停頓了太久。

![alt text](https://github.com/dada878/blog/blob/master/assets/dimage-3.png?raw=true)

下一個階段是 Frontend Team 的面試，他們問了很多關於 React 的問題，包含 `useMemo`、`useCallback`、SSR、CSR、await async 跟 promise 差在哪、SSG、server component 跟 client component 的差別等等。

比較令我印象深刻的是有一題他們問 server component 跟 server side rendering (SSR) 差在哪裡，第一瞬間幾乎沒什麼靈感，想說不就是 server component 才會 server rendering 這樣嗎，思考一小段時間之後突然有一點想法回想起來之前在看 Next build 結果的時候就連 client component 也被標示成 SSR，於是我就有點免強的回答說：「client component 也會用到 SSR... 對吧？」，似乎應該是正確答案，不過感覺回答的很不完整。


另外一個也讓我思考了蠻久的問題就是「`<Suspense>` 在 server component 的運作原理是什麼？它是如何做到載入好後把 fallback 替換成取得到的資料的？」，這題我就真的幾乎完全沒頭緒了，雖然大概給了一點零散地回答剛好提到了 streaming 這個詞，他們就說算是有擦到一點邊，對於這個沒回答出來的問題他們也好心的跟我解釋了 `Suspense` 到底是怎麼是怎麼運作的。

![alt text](https://github.com/dada878/blog/blob/master/assets/dimage-12.png?raw=true)

剩下一些沒有回答的很好的問題還有，「有沒有自調整過 webpack 的 config」，我回答沒有，大多數情況下都是用 framework 的 default config。「web vitals 的評分項目」，雖然用過，但我幾乎忘光了。

作業的部分他們也提到了我的 blog 頁面的 error handling 沒有做得很好，某個 `promise` 的 `.catch` 後面沒判斷就直接接了 `notFound()`。然後 blog 頁面的 cache miss 掉以及我用 `Map` 實作了奇怪的小 cache 也被抓到，快取的部分真的被問得挺慘的ww

還有因為之前的專案都是 Vue 寫的，所以他們也稍微問了一些關於 Vue 的問題，比如說你覺得 Vue 跟 React 差在哪、更喜歡哪個之類的，
但其實我現在對 Vue 的了解度應該比 React 還低，這部分也挺慘的。

面試最後我問他們我還有什麼地方是可以加強的，他們第一句話就是說我非常優秀，三年能學到這樣已經比很多 Junior 強了（這真的讓我很感動），鼓勵的部分結束後，他們給我的建議是應該再多了解 React、Next 的底層在做什麼，可以常常觀察 Devtools 裡面的 Network Tab 到底傳了什麼東西過來。


## 審核結果

面試結束後的下一週，他們就寄了審核結果的資訊到我的信箱。

![alt text](https://github.com/dada878/blog/blob/master/assets/dimage-11.png?raw=true)

打開來看到我沒有錄取，其實當初還蠻失望的，不過仔細這樣回過頭來看看這段時間發生的事，沒有錄取好像也挺合情合理的。至少在這個過程當中我真的學習到了非常多東西，了解到自己許多不足的地方，認識了所謂的「面試」到底是什麼，甚至還讓我從 0 學會了 React 跟 Next XD，再次感謝 Dcard 願意給我這次嘗試的機會 ><

如果沒有 Dcard，我很難想像我可以在兩個月之內成長這麼多！

## 2025 Dcard 實習備戰計畫

統整一下這段時間發生的事情，首先我認為最明顯的缺點應該就是我對 React 和 Next 技術及經驗還不夠充足，尤其是關於偏底層的部分。再來就是技術面試以外的部分我幾乎不知道怎麼準備，感覺 HR 那關我幾乎都是在亂答，像是他們問說有沒有在合作過程當中遇到衝突然後怎麼處理，我回答幾乎沒有，可能藉由這個答案被判斷成我沒什麼合作經驗（雖然這確實），還有短中長期計畫那題也是想了蠻久的。

無論如何，接下來這一年我希望可以：

- 寫更多前端技術文章
- 更深入了解 React / Next 底層技術
- 學習 webpack
- 學習 redux
- 累積更多合作開發的經驗

希望明年就可以錄取 Dcard！！！