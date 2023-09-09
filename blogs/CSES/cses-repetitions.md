# 題解 CSES - Repetitions
https://cses.fi/problemset/task/1069
## 題意
你有一個由 A、C、G、T 組成的字串 \
目標是算出同樣的字母最多連續重複幾次
## 想法
把整個字串從左邊往右掃 \
用一個 $curLen$ 變數維護目前的答案 \
遇到一個字母時 $curLen$ 加 $1$ \
如果跟上個字母不同就把 $curLen$ 歸零 \
每次掃過一個字母再用 $maxLen$ 維護出現過最大的 $curLen$
## 程式碼
```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
signed main() {
	char chr, tmp = 'X';
	int maxLen = 1, curLen = 1;
	while (cin >> chr) {
		if (tmp != 'X' && tmp == chr) {
			curLen++;
		} else {
			curLen = 1;
		}
		maxLen = max(maxLen, curLen);
		tmp = chr;
	}
	cout << maxLen << endl;
}
```