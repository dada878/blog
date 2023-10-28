# APCS 2023 10 月題解
## 前言
這次 APCS 跟 ISSC 撞期 \
然後我就放掉 APCS 跑去打 ISSC : D \
下一次要慢三天才能報了 qwq
## [一、機械鼠](https://zerojudge.tw/ShowProblem?problemid=m370)
### 題意
數線上有一隻老鼠 \
且有 $n$ 個食物散落在數線上 \
老鼠可以選擇一直往左或一直往右 \
求最多可以吃到幾個食物及最後吃食物的位置
### 想法
把問題轉換一下 \
就變成是在問老鼠左邊還是右邊食物比較多、最左邊或最右邊的食物在哪裡 \
於是只要簡單維護一下就可以幾個變數就可以解出來了
### 考點
基本語法
### 程式碼
```cpp
#include <bits/stdc++.h>

using namespace std;

signed main() {
    int x, n, tmp;
    cin >> x >> n;
    int cntl = 0, cntr = 0; // 左邊與右邊食物數量
    int maxv = -1e5, minv = 1e5; // 用最大與最小值維護最後停在的食物位置
    while (n--) {
        cin >> tmp;
        if (tmp >= x) cntr++; // 如果食物在左邊
        if (tmp <= x) cntl++; // 如果食物在右邊
        maxv = max(maxv, tmp);
        minv = min(minv, tmp);
    }
    if (cntl > cntr) cout << cntl << " " << minv << endl; // 往做邊走解更優
    else cout << cntr << " " << maxv << endl; // 否則決定往右邊走
}

```
## [二、卡牌遊戲](https://zerojudge.tw/ShowProblem?problemid=m371)
### 題意
在一個 $n \times m$ 大小的表格上每格裡都有一張牌 \
你可以水平或垂直消除數值為 $x$ 的兩張牌並獲得 $x$ 分，但中間不能有其他牌 \
求最多能獲得多少分
### 想法
枚舉每張牌，嘗試上或左匹配是否存在相同的牌即可 \
使用 $-1$ 紀錄已經匹配掉的牌

至於為什麼只要匹配左上不用考慮右下 \
是因為左跟右、還有上跟下是相對關係

我比較在意的地方是 \
本來以為這個動作需要重複多次才能匹配所有牌 \
結果竟然一次就過了，不知道是不是 ZeroJudge 測資太弱 :thinking: \
或者其實有辦法證明這個作法最多只需要一次
### 考點
二維陣列、模擬
### 程式碼
```cpp
#include <bits/stdc++.h>

using namespace std;

int tb[50][50]; // 表格

signed main() {
    int n, m;
    cin >> n >> m;
    // 輸入資料
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> tb[i][j];
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (tb[i][j] == -1) continue;
            // 嘗試往上配對
            if (i > 0) {
                int k = i-1;
                while (k >= 0 && tb[k][j] == -1) k--;
                if (tb[i][j] == tb[k][j]) {
                    // 配對成功
                    ans += tb[i][j]; // 增加分數
                    tb[i][j] = b[k][j] = -1; // 將兩張牌紀錄乘已匹配
                    continue; // 匹配成功後即可忽略這張牌
                }
            }
            // 嘗試往左配對
            if (j > 0) {
                int k = j-1;
                while (k >= 0 && tb[i][k] == -1) k--;
                if (tb[i][j] == tb[i][k]) {
                    // 配對成功
                    ans += tb[i][j]; // 增加分數
                    tb[i][k] = tb[i][j] = -1; // 將兩張牌紀錄乘已匹配
                    continue; // 匹配成功後即可忽略這張牌
                }
            }
        }
    }
    cout << ans << endl;
}
```
## [三、搬家](https://zerojudge.tw/ShowProblem?problemid=m372)
### 題意
一個 $n \times m$ 的表格上每格有一個水管 \
水管分成 $H、I、F、7、L$ 等類型 \
每種水管可能連接到上、下、左、右其中某些方向 \
求將水管連起來後最大連通塊

*本題詳細題意建議直接進 ZeroJudge 題目頁面查看

### 想法
簡單來說只要對整張圖做 DFS 並一邊維護連通塊大小即可 \
比較麻煩的地方就是建圖而已 \
這份程式碼部份參考了 [dreamoon 老師的 code](https://hackmd.io/@aacp/APCS20231022) 才得以把它改得這麼乾淨的 ><

時間複雜度 $O(nm)$
### 考點
圖論、DFS / BFS
### 程式碼
```cpp
#include <bits/stdc++.h>

using namespace std;

// 上 右 下 左
map<char, vector<int>> mask{
    {'X', {1,1,1,1}},
    {'I', {1,0,1,0}},
    {'H', {0,1,0,1}},
    {'L', {1,1,0,0}},
    {'7', {0,0,1,1}},
    {'F', {0,1,1,0}},
    {'J', {1,0,0,1}},
    {'0', {0,0,0,0}},
};

vector<int> graph[500000]; // 存圖
bool vis[500000]; // 紀錄造訪過的點
int ans = 0, cur = 0;
int n, m;

// 對每座標分配一個 id
int id (int x, int y) {
    return x * m + y;
}

// DFS 並維護連通塊大小
void dfs(int id) {
    cur++;
    vis[id] = true;
    for (auto &u : graph[id]) {
        if (vis[u]) continue;
        vis[u] = true;
        dfs(u);
    }
}

signed main() {
    cin >> n >> m;
    vector<string> v(n);
    for (int i = 0; i < n; i++) cin >> v[i];
    // 建立整張圖
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // 上配下
            if (i + 1 < n && mask[v[i][j]][2] && mask[v[i + 1][j]][0]) {
                graph[id(i, j)].push_back(id(i + 1, j));
                graph[id(i + 1, j)].push_back(id(i, j));
            }
            // 左配右
            if (j + 1 < m && mask[v[i][j]][1] && mask[v[i][j + 1]][3]) {
                graph[id(i, j)].push_back(id(i, j + 1));
                graph[id(i, j + 1)].push_back(id(i, j));
            }
        }
    }
    // 對每一個節點做 DFS
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cur = 0;
            dfs(id(i, j));
            ans = max(ans, cur); // 嘗試更新答案
        }
    }
    cout << ans << endl;
}
```
## [四、投資遊戲](https://zerojudge.tw/ShowProblem?problemid=m373)
### 題意
題目~~廢話~~劇情就不多寫了 \
簡單來說就是求最大連續子序列合，但可以跳過 $k$ 個元素
### 想法
在不考慮 $k$ 的情況下 \
這是一個非常經典的問題 \
解法的話也非常多元 \
以現在這題來說 `Kadane's Algorithm` 應該會是比較好做的

那如果把 $k$ 的條件加進去呢？ \
把測資範圍仔細讀過之後可以注意到 $k \leq 20$ \
考慮動態規劃的作法 \
我們定義 $dp[i]$ 為考慮陣列前 $i$ 個元素的最佳解 \
然後我們可以往前跳過不超過 $k$ 個 \
因此 $dp[i]$ 可以從 $dp[i-1]、dp[i-2] \cdots dp[i-k-1]$ 轉移過來取 $max$ \
但我們還需要紀錄總共已經使用了幾個金牌 \
所以再開一個維度來維護這個資訊

綜合以上幾點，我們可以推出這樣的轉移式 \
定義 $dp[i][j]$ 為考慮前 $i$ 個元素且使用 $j$ 個金牌的最佳解 \
轉移的部份 $dp[i][j] = \max_{1 \leq l \leq k}(dp[i-l-1][j-l] + val[i])$

最後照著轉移式把程式寫出來就好ㄌ

時間複雜度 $O(n \times k^2)$
### 考點
動態規劃
### 程式碼
```cpp
#include <bits/stdc++.h>
#define int long long

using namespace std;

int v[200000];
int dp[200000][30];

signed main() {
    int n, k;
    cin >> n >> k;
    for (int i = 1; i <= n; i++) cin >> v[i];
    for (int i = 1; i <= n; i++) { // 考慮陣列前 i 個元素
        for (int j = 0; j <= k; j++) { // 只使用 j 個金牌
            for (int l = 0; l <= k; l++) { // 枚舉現在要使用多少金牌
                // 跳過超出表格的狀態
                if (j-l < 0 || i-1-l < 0) continue;
                // 對所有狀態取 max
                dp[i][j] = max({dp[i][j], dp[i-l-1][j-l] + v[i], 0LL});
            }
        }
    }
    int ans = 0;
    // 在所有合法狀態中取最大值
    for (int i = 0; i <= k; i++) {
        for (int j = 1; j <= n; j++) {
            ans = max(ans, dp[j][i]);
        }
    }
    cout << ans << endl;
}

```
## 結語
整體來說 \
這次 APCS 其實不算太難（? \
第三題實做比較麻煩一點以外 \
最後一題 DP 轉移式也還算好推
