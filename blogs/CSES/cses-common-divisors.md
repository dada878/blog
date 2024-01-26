# 題解 CSES Common Divisors
https://cses.fi/problemset/task/1081/
## 題意
找到兩個數字 \
使得兩數的最大公因數盡量大
## 想法
可以把題目想成 \
找到最大的 x 使得陣列中出現至少兩個他的倍數 \
於是我們可以先用 $cnt$ 陣列紀錄每個數字的出現次數 \
然後枚舉每個可能的因數 (假設目前枚舉到 k) \
從 $k$、$2k$、$3k$ $\dots$ 計算陣列中存在多少個倍數 \
根據[調和級數](./harmonic-series)可以算出時間複雜度為 $O(n \log n)$
## 實作
```cpp
#include <bits/stdc++.h>
#define int long long

const int maxn = 1e6 + 10;
int cnt[maxn];

signed main() {
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
        cnt[v[i]]++;
    }
    for (int k = maxn; k > 0; k--) {
        int cur = 0;
        for (int j = k; j < maxn; j += k) {
            cur += cnt[j];
        }
        if (cur >= 2) {
            cout << k << endl;
            return 0;
        }
    }
}
```