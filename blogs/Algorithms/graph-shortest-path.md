# 很多最短路演算法
## Dijkstra
### 概念
每次選擇最近的節點 \
嘗試透過該節點來更新相鄰節點距離
### 實作
將所有節點距離初始化為 $\infty$ ( 起點為 0 ) \
選擇目前距離起點最近的節點 \
如果目前節點距離加上相鄰節點與目前節點距離小於起點到相鄰節點的距離就更新
### 程式碼
```cpp
for (int i = 1; i <= n; i++) distance[i] = INF;
distance[x] = 0;
q.push({0, x});
while (!q.empty()) {
	int a = q.top().second; q.pop();
    // 絕對不會更新到的話直接 continue 掉
    if (a.first > dist[now.second]) continue;
	for (auto u : adj[a]) {
		int b = u.first, w = u.second;
		if (distance[a] + w < distance[b]) {
			distance[b] = distance[a] + w;
            // 因為要讓距離小的排在前面所以加負號
			q.push({-distance[b], b});
		}
	}
}
```
## Floyd-WarShall
### 概念
這個演算法是由某個 DP 概念延伸出來的 \
最初的轉移式大概長這樣

定義:

> $dp[k][i][j]$ 為 $i$ 到 $j$ 的最短距離，且只能經過額外的 $k$ 個點

轉移式:

> $\mathrm {dp} (i,j,k)=\mathrm {min} {\Big (}\mathrm {dp} (i,j,k-1),\mathrm {dp} (i,k,k-1)+\mathrm {dp} (k,j,k-1){\Big )}$

### 實作
依照 DP 轉移式枚舉每個點做轉移就好了 \
實作上由於 k 是按照順序轉移的所以可以把空間壓到二維 \
記得要注意迴圈是由外而內順序是 $k$、$i$、$j$ 

### 程式碼
```cpp
for (int k = 1; k <= n; k++) {
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
		}
	}
}
```
### 奇怪的小技巧
如果不小心忘記寫成 $i$ $j$ $k$ 的話只要做三次就會對了 \
2019 年的某篇論文上提到了這點

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fd477b2f1-0d39-4fe4-a359-31eac3004e02%2FUntitled.png?table=block&id=033abae1-3cc2-443d-ab3a-59a5b6e68366&spaceId=090471c9-4258-4339-8654-7be181344180&width=1720&userId=72aeb5d8-6609-42c6-8c49-344fc9073da7&cache=v2)

### 判斷負環
如果任一個 $dist[i][i] < 0$ 若且唯若存在負環 \
代表有一個點自己繞一圈回到自己距離小於 0 \
但如果是無向圖的話的負環就很難判斷了

## Bellman-Ford
### 概念
對於每個邊嘗試更新連接的兩個點對於起點的距離
### 實作
重複 n-1 次嘗試更新所有的邊
### 程式碼
```cpp
for (int i = 1; i <= n; i++) dist[i] = INF;
	dist[x] = 0;
	for (int i = 1; i <= n-1; i++) {
		for (auto e : edges) {
			int a, b, w;
			tie(a, b, w) = e;
			dist[b] = min(dist[b], dist[a] + w);
		}
	}
}
```
### 判斷負環
如果更新了 n-1 次還能繼續更新 \
代表這張圖存在負環
## 結論
看完這些之後 \
想必一定有人會覺得「為什麼要學這麼多種最短路演算法」 \
原因很簡單，因為這些演算法各自有不同的特性與效率 \
所以需要適時挑選適合的演算法來使用

不過比較值得注意的是 \
事實上如果要求多源最短路的話 \
枚舉每個點做 Dijkstra 甚至比 Floyd-Warshall 還快

|  | Bellman-Ford | Dijkstra | Floyd-Warshall |
| --- | --- | --- | --- |
| 類型 |  單點源 | 單點源 | 全點對 |
| 限制 | 任意圖 | 無負邊 | 任意圖 |
| 時間複雜度 | $O(VE)$ | $O(E log E)$ | $O(V^3)$ |
| 用途 | 檢查負環 | 快速單點源 | 負邊全點對 |
