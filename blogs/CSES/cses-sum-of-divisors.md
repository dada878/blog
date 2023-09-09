# 題解 CSES - Sum of Divisors
https://cses.fi/problemset/task/1082/
## 題意
定義 $f(x)$ 為 $x$ 的所有因數之和 \
給予一個 $n$ 求 $\sum^n_{k=1}f(k)$ 之值
## 想法
以 $12$ 為例 \
先看一下這張圖列出了 $1 \sim 12$ 的所有因數

![](https://github.com/dada878/blog/blob/master/assets/Snipaste_2023-09-10_05-15-11.png?raw=true)

可以發現每兩個數字就會出現一次 $2$ \
每三次數字就會出現一次 $3$ \
觀察後可知 \
對於一個數字 $x$ 它的出現次數會是 $\lfloor \frac{n}{x} \rfloor$ \
因為每 $x$ 個數字就會出現一個 $x$ 的倍數 \
用這個做法枚舉每個數字計算就可以得到一個 $O(n)$ 的算法 \
但這樣還不夠快到足以處理這題 $10^{12}$ 的資料量

如果我們把剛剛那張圖的呈現方式改一下 \
上面那一橫排代表因數 $1 \sim 12$ \
下面那一行排代表該因數出現的次數

![](https://github.com/dada878/blog/blob/master/assets/Snipaste_2023-09-10_05-33-56.png?raw=true)

可以發現這張圖內有幾串連續的因數出現次數相同 \
因為事實上在計算這個的過程中只會出現最多 $2 \sqrt n$ 個相異數字

<details>
  <summary>證明</summary>
  :D
</details>

上面那張圖每個紅色圈起來代表一塊 \
如果我們可以塊為單位來計算就可以把時間複雜度降到 $O(\sqrt{n})$ 了

## 程式碼
```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;

const int mod = 1e9 + 7;
const int inv = 500000004;
 
signed main() {
    int n;
    cin >> n;
    int cur = 1;
    int ans = 0;
    while (cur <= n) {
        int cnt = n / cur;
        int next = n / cnt;
        int sum = ((((next + cur) % mod) * ((next - cur + 1) % mod) % mod) * inv) % mod;
        ans += ((sum % mod) * (cnt % mod)) % mod;
        cur = next + 1;
    }
    cout << ans % mod << endl;
}
```