# 題解 CSES Trailing Zeros
https://cses.fi/problemset/result/5470956/
# 題意
n 階乘求數字有幾個後綴 0
# 想法
不難發現   
後綴幾個 0 就等於乘進去的 10 的個數   
而 $10 = 5 \times 2$ \
所以後綴 0 數量就相當於計算把每個數質因數分解後 5 和 2 的較少的那個的個數   
那當然 5 一定會比 2 少   
所以我們要做的是就是計算 5 的個數   
那要如何計算呢？   
   
以 30 為例   
我們知道要求得 30 階就是要把下面這些數字乘起來   

![](https://github.com/dada878/blog/blob/master/assets/image20240126.png?raw=true)

不過我們可以先排除掉質因數分解後裡面沒有 5 的數字   
然後把下面的數字都各取走一個質因數分解裡面的 5（相當於除與 5）   
並把答案加上 6 (因為下面有 6 個數字)   

![](https://github.com/dada878/blog/blob/master/assets/image20240126-2.png?raw=true)

變成這樣   
可以看到下面的數字剛好就是 6 階乘的子問題   

![](https://github.com/dada878/blog/blob/master/assets/image20240126-3.png?raw=true)

像剛剛的作法一樣   
把跟 5 無關的數字排除並把它取走一個 5 的質因數   
答案 += 1

![](https://github.com/dada878/blog/blob/master/assets/image20240126-4.png?raw=true)

這樣就完成 30 階的計算了！   
   
根據上面的操作   
可以推出下列遞迴式   

$$
f(x) = f(\lfloor \frac nx \rfloor) + \lfloor \frac nx \rfloor
$$
不過寫成程式其實用 while 迴圈就可以了   
```cpp
#include <bits/stdc++.h>
#define int long long
using namespace std;
signed main() {
    int n;
    cin >> n;
    if (n % 2) {
        cout << 0 << endl;
        return 0;
    }
    int ans = 0;
    while (n >= 5) {
        n /= 5;
        ans += n;
    }
    cout << ans << endl;
}
```
