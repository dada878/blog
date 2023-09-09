# 調和級數
## 簡介
一個在因倍數相關題目可以用到的小技巧 \
程式碼大概像這樣 \
可以得到 $O(n \log n)$ 的時間複雜度
```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j += i) {
        // to something
    }
}
```
## 公式
$\log n \approx \sum_{k=1}^n \frac 1 k =  1 + \frac 1 2 + \frac 1 3 + \frac 1 4 + \cdots + \frac 1 n$ \
$\quad$
![](https://github.com/dada878/blog/blob/master/assets/Snipaste_2023-09-09_20-53-54.png?raw=true)
## 例題
https://codeforces.com/contest/1850/problem/F \
https://cses.fi/problemset/task/1081/