# 題解 CSES Missing Number
https://cses.fi/problemset/task/1083/
## 題意
給予一堆數字 $1 \sim n$ 但中間缺少了一個 \
你的任務是找出那個缺少的數字
## 想法
已知數字 $1 \sim n$ 的總和為 $\sum^n_{k=1}k$ \
可以透過梯形公式 $\frac{n(1 + n)}{2}$ 快速求出來 \
所以我們只要用期望的 $1 \sim n$ 總和減掉輸入的所有數字就可以算出答案了
## 程式碼
```cpp
#include <bits/stdc++.h>
#define int long long
using namespace std;
 
main() {
	ios_base::sync_with_stdio(false);cin.tie(0);
	int n, sum = 0;
	cin >> n;
	for (int i = 0; i < n-1; i++) {
		int tmp;
		cin >> tmp;
		sum += tmp;
	}
	cout << ((1 + n) * n) / 2 - sum << endl;
}
```