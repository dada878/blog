# C++ 常見 STL 教學
## piar
### 簡介
pair 是一種可以儲存兩個元素的資料結構
### 用途
通常用來儲存二維座標或者是陣列的 index 與 value \
而且常數較小 \
如果用 `array / vector` 替代有些題目真的會被卡 TLE
### 語法
```cpp
// 宣告一個第一個欄位為 1 第二個欄位為 5 的 pair
// 在一些 c++ 版本較舊的環境下要使用 make_pair(1, 5)
pair<int, int> pos = {1, 5};

// 取得第一個欄位的值
cout << pos.first << endl;

// 取得第二個欄位的值
cout << pos.second << endl;

// 將 pos 的第一個欄位的 1 改成 2
pos.first = 2;

// 將 pos 的第二個欄位的 5 改成 4
pos.second = 4;
```
### 比較
在比較兩個 pair 時會先比第一個元素 \
如果第一個元素相同才會比第二個元素
## vector
### 簡介
跟傳統陣列差不多 \
不過長度是可變的 \
會因為加入更多元素讓 vector 變得更長
### 用途
不用多說了吧 \
就是可以像陣列一樣儲存 n 個元素
### 語法
```cpp
// 直接宣告 vector 的方式
vector<int> v1;

// 宣告長度為 n 的 vector
vector<int> v2(n);

// 宣告長度為 n 且每個元素都是 5 的 vector
vector<int> v3(n, 5);

// 宣告一個有元素 {1, 2, 3, 4} 的 vector
vector<int> v4 = {1, 2, 3, 4}

// 宣告一個跟其他 vector 一樣的 vector (複製)
vector<int> v5(v4);

// 加入元素在尾端
v1.push_back(7);

// 從尾端移除元素
v1.pop_back();

// 存取 vector 中的某一項
cout << v4[2] << endl;

// 取得大小
cout << v2.size() << endl;
```
### 比較
從第一個元素開始比較 \
如果相同就繼續往後比 \
直到第一個不同為止
## queue
### 簡介
像是一個排隊的隊伍 \
可以從一端進入 \
從另一端離開 \
也就是先進去的會先離開
### 用途
大部分情況用來實作一些較複雜的演算法 \
比如 BFS、拓撲排序等等
### 語法
```cpp
// 宣告一個 queue
queue<int> q;

// 將元素 5 推入 queue 後端
q.push(5);

// 取得 queue 前端的元素
cout << q.front() << endl;

// 取得 queue 後端的元素
cout << q.back() << endl;

// 將隊伍前端的元素彈出(移除)
q.pop();

// 檢查 queue 是否為空
if (q.empty()) {
    cout << "empty" << endl;
}

// 取得 queue 的大小
cout << q.size() << endl;

```
## stack
### 簡介
類似於一疊盤子 \
最後放上去的盤子會最先被取走 \
而你不能從中間拿走盤子 \
也就是說後進去的會先出去
### 用途
stack 常用來會處理一些匹配類問題 \
或者是模擬遞迴 \
更進階一點還有單調堆疊之類的玩法
### 語法
```cpp
// 宣告一個 stack
stack<int> stk;

// 將元素 3 推入 stack
stk.push(3);

// 從 stack 頂端取出元素
cout << stk.top() << endl;

// 將 stack 頂端的元素彈出(移除)
stk.pop();

// 檢查 stack 是否為空
if (stk.empty()) {
    cout << "empty" << endl;
}

// 取得 stack 的大小
cout << stk.size() << endl;
```
## set
### 簡介
就是集合的意思 \
用來儲存不重複的元素 \
並會按照元素的大小自動排序
### 用途
主要用於快速插入和查找元素
### 語法
```cpp
// 宣告一個 set
set<int> st;

// 插入元素
st.insert(5);
st.insert(3);
st.insert(7);

// 檢查 set 是否包含某元素
if (st.find(3) != st.end()) {
    cout << "set contains 3" << endl;
} else {
    cout << "set does not contain 3" << endl;
}

// 刪除元素
st.erase(5);

// 遍歷 set 中的元素
for (int e : st) {
    cout << e << " ";
}

// 取得 set 的大小
cout << st.size() << endl;

// 取得 set 的第一項
// 因為回傳的是 iterator 所以要加 *
cout << *st.begin() << endl;

// 取得 set 的最後一項
// 由於 back 是開區間所以要 -1
cout << *--st.end() << endl;
```
## map
### 簡介
語法根陣列有點像 \
不過可以接受整數以外的型態來當作索引值
### 用途
有些時候需要使用負數、非常大的數字、字串等等來當索引值 \
map 就會是一個很方便的工具
### 語法
```cpp
// 宣告一個以 string 為索引，int 為值的 map
map<string, int> mp;

// 把字串對應到數字
mp["one"] = 1;
mp["two"] = 2;
mp["three"] = 3;

// 輸出 one 的值
cout << mp["one"] << endl;

// 在 map 中刪除 one
mp.erase("one");

// 遍歷 map
for (auto [key, value] : mp) {
    cout << key << ", " << value << endl;
}

// 取得 map 的大小
cout << mp.size() << endl;
```
## priority queue
### 簡介
又稱為 heap \
可以支援快速地插入及查詢最大最小值
### 用途
很常使用在一些複雜的演算法內 \
比如最短路徑、最小生成樹等等
### 語法
```cpp
// 宣告一個 priority queue
priority_queue<int> pq;

// 宣告一個 priority queue 並且頂部為最小值
priority_queue<int, vector<int>, greater<int>> pq;

// 插入元素
pq.push(3);
pq.push(1);
pq.push(5);

// 取得頂端的元素(最大值)
cout << pq.top() << endl;

// 移除頂端的元素
pq.pop();

// 檢查 priority queue 是否為空
if (pq.empty()) {
    cout << "empty" << endl;
}

// 取得 priority queue 的大小
cout << pq.size() << endl;
```