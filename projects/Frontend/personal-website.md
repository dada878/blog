# 個人網站
## 簡介
就是你現在看到ㄉ這個很酷的網站 \
大概是從 2022 開始搞的 \
雖然中間斷了很長一段時間的更新 \
主要是方便放我寫的文章還有把我的作品整理起來 \
放一些經歷之類的順便還可以當備審或履歷之類的(?)
## 技術
- Nuxt
- Vue
- Typescript
- SCSS
## 歷程
### 創立
剛開始只是覺得我需要一個很酷的個人網站 \
然後用 Vue 簡單建立了一個網站
### SSR 優化
這個網站被冷凍了好幾個月之後 \
2023 的暑假繼續回到了這個專案更新 \
因為想讓 Google 搜尋搜到的關係 \
決定來優化一下 SEO \
Vue 的 CSR 對 SEO 非常差 \
所以改成使用 Nuxt 的 SSR 實現
### SSG 部落格
雖然這個網站一直都有部落格頁面 \
但實際上那個頁面什麼文章都沒有 \
甚至連文章的系統都沒有

最初想使用 hackmd 的文章 \
然後透過 API 之類的方式同步過來 \
結果發現它的 API 沒辦法顯示整個文章

後來決定使用 Github 來存放文章 \
然後因為 CSRF 和效能問題 \
最後在 CI/CD 寫了一個腳本抓取文章 SSG 生成資訊
### SEO 再次優化
當然 \
現在 Google 還是搜尋不到我的網站 \
所以我打算來做更多的 SEO 優化 \
把 meta tag、sitemap 等等該設定的都設定了 \
也設定讓 nuxt 在 build 時把部落格頁面都先 prerendering 過
### 圖片載入優化
原本的圖片都是直接連結 Github repository 裡面的圖片連結 \
但這樣載入速度非常的慢 \
經過測試大概需要花 1 ~ 1.5 秒才能完成圖片載入 \
所以後來連圖片也都先預先下載 \
再把所有原文的連結替換成目前網站上的連結 \
成功把載入速度優化到 20 ~ 50 毫秒
## 心得
好麻煩喔我之後再寫