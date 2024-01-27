# 圖論入門
## 什麼是圖
首先 \
我們要先來了解什麼是圖

簡單來說 \
圖 (Graph) 就是由多個節點 (Node) 並透過邊 (Edge) 連結成的我們
像是下面的示意圖

![](https://github.com/dada878/blog/blob/master/assets/image-20240128-1.png?raw=true)

## 建立一張圖
在知道圖是什麼之後 \
我們要來看的是如何在 C++ 中儲存一張圖

在大部分的情況下 \
我們會以節點關係來儲存一張圖

像是上面那張圖片的範例 \
我們知道節點 1 會連接到節點 2 跟 3 \
節點 2 會連接到節點 1 跟 3 \
節點 3 會連接到節點 2 跟 4 \
節點 4 會連接到節點 3 跟 5 \
節點 5 會連接到節點 4 

也就是說 \
我們實際上要存的資料大概長這樣：
```
1 -> [2, 3]
2 -> [1, 3]
3 -> [2, 4]
4 -> [3, 5]
5 -> [4]
```
C++ 內可以使用傳統陣列套 vector 來實現
```cpp
// MAXN 最大節點數量
vector<int> graph[MAXN];

// 下面的操作就是相當於我們從節點 1 建立了兩條邊分別指向 2 跟 3
graph[1].push_back(2);
graph[1].push_back(3);
```
## 拜訪圖上的節點
在很多的情境下 \
我們會需要拜訪整張圖上面的所有節點來得知一些資訊

這邊會簡單的介紹一下 DFS (深度優先搜尋) 演算法的作法 \
這個演算法就是利用遞迴的特性遍歷整張圖

這個演算法會儘可能深的搜尋圖的分支 \
當節點的所有邊都已經被搜尋過 \
則會回溯到上個節點 \
這個過程會一直重複到搜尋完整張圖為止

![](https://github.com/dada878/blog/blob/master/assets/image-20240128-5.png?raw=true)

程式碼應該不難理解 \
直截來看看吧：

```cpp
vector<int> graph[MAXN]; // 存圖
bool vis[MAXN]; // 紀錄哪些節點拜訪過

void dfs(int v) {
    // 枚舉每一個 v 可以走到的節點
    for (int u : graph[v]) {
        // 如果走過就略過
        if (vis[u]) continue;
        // 標記為走過
        vis[u] = true;
        // 造放進節點 u
        dfs(u);
    }
}
```
## 樹狀圖
樹其實就是圖的一種 \
有一些特性：
- 不存在環
- 每個節點均可以走到其他每個節點
- 若有 $n$ 個節點，邊就是 $n-1$ 條

這邊先補充一下 \
環就是指像是最上面的示意圖 1 -> 2 -> 3 那部分的結構

然後樹的其他部分都跟圖差不多 \
不過 DFS 可以寫的比圖簡單
```cpp
void dfs(int v, int p) {
    // 枚舉每一個 v 可以走到的節點
    for (int u : graph[v]) {
        // 不能走回上個節點
        if (u == p) continue;
        // 造放進節點 u
        dfs(u, v);
    }
}
```
## 練習
這裡是一些簡單的練習題：
- [CSES 
Building Roads](https://cses.fi/problemset/task/1666)
- [CSES Message Route](https://cses.fi/problemset/task/1667)
## 延伸閱讀
或者你也可以在這邊了解一些更進階的內容：
- [最短路演算法](https://dada878.com/blogs/graph-shortest-path)
