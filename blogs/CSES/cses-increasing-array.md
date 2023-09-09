# CSES 題解 - Increasing Array
https://cses.fi/problemset/task/1094/
## 題意
給你一個陣列 \
每次修改可以讓任何一個元素的值加一 \
最少需要修改幾次才能讓整個陣列變成非嚴格遞增的
## 想法
從陣列左邊往右邊掃過去 \
遇到凹洞就把它填滿 \
計算總共需要花多少成本 \
![](https://github.com/dada878/blog/blob/master/assets/Snipaste_2023-09-09_21-36-33.png?raw=true)
## 程式碼
```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
main() {
	ios_base::sync_with_stdio(false);cin.tie(0);
	int n;
	cin >> n;
	int ans = 0;
	vector<int> vec(n);
	for (int i = 0; i < n; i++) {
		cin >> vec[i];
	}
	for (int i = 1; i < n; i++) {
		if (vec[i-1] > vec[i]) {
			ans += vec[i-1] - vec[i];
			vec[i] = vec[i-1];
		}
	}
	cout << ans;
}
```