# F - Dist Max 2 題解
https://atcoder.jp/contests/abc215/tasks/abc215_f
## 題意
給予 $n$ 個數字 \
求 $n$ 個數中兩兩相乘的所有結果中第 $k$ 小的是多少
## 想法
轉化一下題目 \
要找第 $k$ 小其實就是找到一個最小 $x$ 的數字滿足 $cnt(x) \leq k$

> 定義 $cnt(x)$ 為小於等於 $x$ 的數字個數

再來只要套上二分搜即可 \
檢查答案的部份用雙指標就可以很容易的實現 \
比較麻煩的是這題會出現負數 \
所以要分成 `負數乘負數`、`正數乘負數`、`正數乘正數` 三種 Case 來處理

整體時間複雜度 $O(n log n)$
## 程式碼
```cpp
#include <bits/stdc++.h>
#define int long long
#define endl "\n"
#define szz(x) ((int)x.size())
#define dbg(x) cerr << #x << " = " << (x) <<  endl;

using namespace std;

int n, k, tmp;
vector<int> neg, pos, v;

bool cnt(int x) {
    // 負數乘正數
    int cnp = 0;
    for (int i = 0, j = 0; i < szz(pos); i++) {
        while (j < szz(neg) && neg[j] * pos[i] <= x) {
            j++;
        }
        cnp += j;
    }
    // 正數乘正數
    int cpp = 0;
    for (int i = 0, j = szz(pos)-1; i < szz(pos); i++) {
        while (j > i && pos[i] * pos[j] > x) {
            j--;
        }
        cpp += max(j - i, 0LL);
    }
    // 負數乘負數
    int cnn = 0;
    for (int i = szz(neg)-1, j = 0; i >= 0; i--) {
        while (i > j && neg[i] * neg[j] > x) {
            j++;
        }
        cnn += max(i - j, 0LL);
    }
    // 判斷三種 case 總和是否 >= k
    int all = cpp + cnn + cnp;
    return all >= k;
}

signed main() {
    // io 優化
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        // 分開正數與負數
        if (tmp < 0) neg.push_back(tmp);
        else pos.push_back(tmp);
    }
    // 排序以方便做雙指標
    sort(pos.begin(), pos.end());
    sort(neg.begin(), neg.end());
    int l = -1e18 - 100;
    int r = 1e18 + 100;
    // 對 cnt() 二分搜
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (cnt(mid)) r = mid;
        else l = mid + 1;
    }
    cout << l << endl;
}
```