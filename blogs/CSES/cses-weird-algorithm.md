# 題解 CSES Weird Algorithm
https://cses.fi/problemset/task/1068
## 題意
給予一個數字 $n$ \
如果他是偶數就把他除 $2$ \
否則就把他乘 $3$ 再加 $1$ \
重複直到 $n$ 變成 $1$
## 想法
沒什麼特別的概念 \
直接模擬操作就可以了
## 程式碼
```cpp
#include <bits/stdc++.h>
#define int long long
using namespace std;
signed main() {
	int n;
	cin >> n;
	while(n != 1) {
		cout << n << " ";
		if (n & 1 == 1) {
			 n *= 3;
			 n++;
		} else {
			n /= 2;
		}
	}
	cout << 1 << endl;
}
```