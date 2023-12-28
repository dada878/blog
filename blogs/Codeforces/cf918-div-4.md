# Codeforces 918 Div 4 題解
## 前言
為了慶祝第一次在 CF 破台所以難得來寫一下題解 \
這成績我可以開心一個禮拜了 :> \
~~然後今天早上過的太廢一題都沒寫不知道是不是因為這樣把能量都留到這場釋放了~~
![](https://github.com/dada878/blog/blob/master/assets/2023-12-29-01-57-27.png?raw=true)
## pA - Odd One Out
### 題意
給定三個數，其中兩個數相同，找到不同的那一個數
### 思路
直接照題意模擬做就行了，實作的部分用 map 很方便
### 程式碼
```cpp
#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int t, tmp;
    cin >> t;
    while (t--) {
        map<int, int> cnt;
        // 計算每個數字出現幾次
        for (int i = 1; i <= 3; i++) {
            cin >> tmp;
            cnt[tmp]++;
        }
        // 找到出現次數為 1 的那個數
        for (auto [num, frq] : cnt) {
            if (frq == 1) cout << num << endl;
        }
    }
}
```
## pB - Not Quite Latin Square
### 題意
給予一個 3x3 的矩陣，每行、列都剛好包含各一個 A、B、C 字母，但某一格未知，任務是找到未知的那格是什麼
### 思路
直接照題意模擬做就行了，實作的部分用 set 很方便
### 程式碼
```cpp
#include <bits/stdc++.h>
using namespace std;

char tb[5][5];

// 檢查矩陣是否合法
bool check() {
    // 檢查每個 row
    for (int i = 0; i < 3; i++) {
        set<char> st;
        for (int j = 0; j < 3; j++) {
            st.insert(tb[i][j]);
        }
        if (st.size() != 3) return false;
    }
    // 檢查每個 column
    for (int i = 0; i < 3; i++) {
        set<char> st;
        for (int j = 0; j < 3; j++) {
            st.insert(tb[j][i]);
        }
        if (st.size() != 3) return false;
    }
    return true;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int px, py; // 未知格的座標
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                cin >> tb[i][j];
                if (tb[i][j] == '?') {
                    px = i;
                    py = j;
                }
            }
        }
        // 枚舉該放哪個字母
        for (char c = 'A'; c <= 'C'; c++) {
            tb[px][py] = c;
            // 如果合法就輸出
            if (check()) {
                cout << c << endl;
            }
        }
    }
}
```
## pC - Can I Square?
### 題意
有 $n$ 個盒子，第 $i$ 個盒子裝著 $a_i$ 個 1x1 的紙片，求是否可以剛好用所有的紙片拼成一個平片的正方形？
### 思路
事實上題目問的就只是 $\sum_{i=1}^n a_i$ 是否為完全平方數 \
所以只需要加總後開根在平方看是否跟原始的數相等就行了
### 程式碼
```cpp
#include <bits/stdc++.h>
#define int long long
#define square(x) ((x)*(x))
using namespace std;

signed main() {
    int t;
    cin >> t;
    while (t--) {
        int n, tmp, sum = 0;
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> tmp;
            sum += tmp;
        }
        if (square((int)sqrt(sum)) == sum) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}
```
## pD - Unnatural Language Processing
### 題意
有一種只包含 a、b、c、d、e 的語言，這些字母被分成兩種類型
- Vowels — 包含字母 a 和 e，用 V 表示
- Consonants — 包含字母 b、c、d，用 C 表示

一個合法的段落可能為 CV 或 CVC \
給予一串文字 \
求將它按照規則分段的結果
### 思路
直接隨便取的話會出一些問題 \
不過其實只需要觀察到兩個 C 不能連再一起就完事了 \
雖然我也還沒完整的證過 (因為我不是數學家)
### 程式碼
```cpp
#include <bits/stdc++.h>
using namespace std;

// 儲存每個字母是 v 或 c 類
map<char, char> tb = {
    {'a', 'v'},
    {'b', 'c'},
    {'c', 'c'},
    {'d', 'c'},
    {'e', 'v'},
};

void sol() {
    int n;
    string s; // 題目給的字串
    string ss; // 轉換過後只包含 c 跟 v 的字串
    cin >> n >> s;
    // 轉換字串
    for (auto c : s) ss += tb[c];
    // 分段後的結果
    vector<string> ans;
    for (int i = 0; i < s.size(); ) {
        if (i == s.size() - 3) { // 只剩下最後三個字就直接全取
            ans.push_back(s.substr(i, 3));
            break;
        }
        if (ss[i+3] == ss[i+2] && ss[i+2] == 'c') {
            // 如果選 CV 會導致兩個連續 C 的情況出現就改選 CVC
            ans.push_back(s.substr(i, 3));
            i = i + 3;
        } else {
            // 否則就選 CV
            ans.push_back(s.substr(i, 2));
            i = i + 2;
        }
    }    
    // 輸出解
    for (int i = 0; i < ans.size(); i++) {
        if (i != 0) cout << ".";
        cout << ans[i];
    }
    cout << endl;
}
 
int main() {
    int t;
    cin >> t;
    while (t--) sol();
}
```
## pE - Romantic Glasses
### 題意
給定一個陣列，求是否存在一段連續的區間滿足偶數 index 的所有元素加起來等於奇數 index 的元素
### 思路
把偶數 index 的元素都加上負號再套上前綴和之後 \
題目就被轉換成找到一個區間滿足總和為 0

也就是說只要從左掃到右 \
並對於每個位置檢查左邊是否存在相同值的元素即可
### 程式碼
```cpp
#include <bits/stdc++.h>
#define int long long
using namespace std;
 
void sol() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (i % 2 == 0) a[i] *= -1;
    }
    vector<int> psum(n + 1);
    partial_sum(a.begin(), a.end(), psum.begin() + 1);
    set<int> st;
    for (auto e : psum) {
        if (st.find(e) != st.end()) {
            cout << "YES" << endl;
            return;
        }
        st.insert(e);
    }
    cout << "NO" << endl;
}
 
signed main() {
    int t;
    cin >> t;
    while (t--) sol();
}
```
## pF - Greetings
### 題意
有 $n$ 個人在數線上以每秒 1 格的速度往右走，第 $i$ 個人的起點為 $a_i$ 終點為 $b_i$，求他們倆倆碰面（同時出現在同一格）的次數
### 思路
仔細觀察之後會發現 \
只有 $a_i$ > $a_j$ 且 $b_i$ < $b_j$ 的情況下 $i$ 跟 $j$ 才會碰面 \
(也就是一個區間把另外一個區間包住的情況)

可以發現其實就跟 CSES 的 [Nested Ranges Count](https://cses.fi/problemset/task/2169) 完全一樣 \
那這題網路上題解很多 \
算法細節就不多提了
### 程式碼
```cpp
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define int long long

using namespace std;
using namespace __gnu_pbds;

template <class T> using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

void sol() {
    int n;
    cin >> n;
    vector<int> becon(n), yidx(n);
    vector<tuple<int, int, int>> b(n), c(n);
 
    for (int i = 0; i < n; ++i) {
		int l, r;
		cin >> l >> r;
        b[i] = {l, r * -1, i};
        c[i] = {r, l * -1, i};
    }
 
    sort(b.begin(), b.end());
    sort(c.begin(), c.end());
    
	for (int i = 0; i < n; ++i)
        yidx[get<2>(b[i])] = i;
 
    ordered_set<int> s;
    
    for (int i = 0; i < n; ++i) {
        int idx = get<2>(c[i]);
        int cur = yidx[idx];
        becon[idx] = s.size() - s.order_of_key(cur);
        s.insert(cur);
    }
 
    int ans = 0;
    for (int i = 0; i < n; ++i) ans += becon[i];
    cout << ans << endl;
}
 
signed main() {
    io;
    int t;
    cin >> t;
    while (t--) sol();
}
```
## pG - Bicycles
### 題意
給一張無向帶權圖，第 $i$ 條邊連接著 $v_i$ 及 $u_i$ 且權重為 $w_i$，你可以在節點 $i$ 拿到一台速度為 $s_i$ 的腳踏車，騎著速度為 $s_i$ 的腳踏車經過第 $j$ 條邊時需要花費 $s_i \times w_j$，求全程騎腳踏車從 $1$ 走到 $n$ 的最少時間花費
### 思路
不難想到從點 $v$ 獲得腳踏車後到其他每個點 $u$ 的最少時間花費為 $dist(v, u) * s_v$ (其中 $dist$ 代表兩點最短路徑長度) \
那其實就只要依照上面的規則把那些邊都建在新的圖上 \
最後對新的圖做最短路就可以了

補充資料: [最短路演算法](https://dada878.com/blogs/graph-shortest-path)
```cpp
#include <bits/stdc++.h>
#define int long long
#define pii pair<int, int>
#define ff first
#define ss second

using namespace std;

const int maxn = 1e3 + 10;
const int inf = 1e13;
 
int n, m;
vector<pii> g[maxn];
int bike[maxn];
 
vector<pii> g2[maxn];
int dist2[maxn][maxn];
 
int dist[maxn];
 
void sol() {
    // 初始化 & 讀取輸入
    cin >> n >> m;
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= n; j++) {
            dist2[i][j] = inf;
        }
    }
    for (int i = 0; i <= n; i++) {
        g[i].clear();
        g2[i].clear();
    }
    for (int i = 0; i < m; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        g[a].push_back({b, w});
        g[b].push_back({a, w});
    }
    for (int i = 1; i <= n; i++) {
        cin >> bike[i];
    }
    // 在原始的圖上求每個點對得最短路
    for (int v = 1; v <= n; v++) {
        // 初始化
        for (int i = 1; i <= n; i++) {
            dist[i] = inf;
        }
        // 使用 dijkstra 演算法
        priority_queue<pii, vector<pii>, greater<pii>> pq;
        pq.push({0, v});
        dist[v] = 0;
        while (pq.size()) {
            auto now = pq.top(); pq.pop();
            if (now.ff > dist[now.ss]) continue;
            for (auto other : g[now.ss]) {
                if (dist[other.ff] > dist[now.ss] + other.ss) {
                    dist[other.ff] = dist[now.ss] + other.ss;
                    pq.push({dist[other.ff], other.ff});
                }
            }
        }
        // 建邊在新的圖上
        for (int i = 1; i <= n; i++) {
            if (i == v) continue;
            g2[v].push_back({i, dist[i] * bike[v]});
        }
    }
    // 初始化 (準備在新的圖上做最短路)
    for (int i = 1; i <= n; i++) {
        dist[i] = inf;
    }
    // 使用 dijkstra 演算法
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({0, 1});
    dist[1] = 0;
    while (pq.size()) {
        auto now = pq.top(); pq.pop();
        if (now.ff > dist[now.ss]) continue;
        for (auto other : g2[now.ss]) {
            if (dist[other.ff] > dist[now.ss] + other.ss) {
                dist[other.ff] = dist[now.ss] + other.ss;
                pq.push({dist[other.ff], other.ff});
            }
        }
    }
    // 輸出解
    cout << dist[n] << endl;
}
 
signed main() {
    int t;
    cin >> t;
    while (t--) sol();
}
```