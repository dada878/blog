# CSES 題解 - Permutations
https://cses.fi/problemset/task/1070/
## 題意
給予一個數字 $n$ \
你要使用數字 $1 \sim n$ 構造一個陣列 \
使得不存在任意兩個相鄰數字的差為 1
## 想法
把 $n$ 個數字分成 $1 \sim \lfloor \frac{n}{2} \rfloor$ 和 $\lfloor \frac{n}{2}+1 \rfloor \sim n$ 兩堆 \
並穿插構造 $ans$ 陣列就可以保證任兩數的差大約為 $\frac{n}{2}$ \
最後跑過整個陣列驗證是否合法即可 \
![](https://github.com/dada878/blog/blob/master/assets/Snipaste_2023-09-09_21-50-43.png?raw=true)
## 程式碼
```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
signed main() {
	ios_base::sync_with_stdio(false);cin.tie(0);
	int n;
	cin >> n;
	vector<int> arr(n);
	deque<int> ans;
	int mid = n/2;
	for (int i = 1; i <= n/2; i ++) {
		int leftVal = i;
		int rightVal = mid + i;
		ans.push_back(rightVal);
		ans.push_back(leftVal);
	}
	if ((n & 1) == 1) {
		ans.push_front(mid + n/2 +1);
	}
	for (int i = 0; i < n-1; i++) {
		if (abs(ans[i+1] - ans[i]) == 1) {
			cout << "NO SOLUTION" << endl;
			return 0 ;
		}
	}
	for (int i = 0; i < n; i ++) {
		cout << ans[i] << " ";
	}
	cout << endl;
}
```