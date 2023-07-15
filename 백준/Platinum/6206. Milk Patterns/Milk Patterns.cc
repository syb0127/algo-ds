#include <bits/stdc++.h>
#include <unordered_set>
#define rep(i,n) for(int i=0;i<n;++i)
#define REP(i,n) for(int i=1;i<=n;++i)
#define FAST cin.tie(NULL);cout.tie(NULL); ios::sync_with_stdio(false)
using namespace std;

typedef long long ll;

const ll MOD[2] = { 1000000000 + 7,1000000000 + 9 };
const ll BASE = 1000001;

int arr[20000];
ll hs[2], b[2];
int N, K;

unordered_map<ll, int> um;

bool ok(int m) {
    um.clear();
    rep(j, 2) hs[j] = arr[0], b[j] = 1;
    for (int i = 1;i < m;++i) rep(j, 2) {
        hs[j] = (hs[j] * BASE + arr[i]) % MOD[j];
        b[j] = b[j] * BASE % MOD[j];
    }
    um[hs[0] << 32 | hs[1]] = 1;
    for (int i = m;i < N;++i) {
        rep(j, 2) {
            hs[j] = (hs[j] - arr[i - m] * b[j] % MOD[j] + MOD[j]) % MOD[j];
            hs[j] = (hs[j] * BASE + arr[i]) % MOD[j];
        }
        if (++um[hs[0] << 32 | hs[1]] >= K) return true;
    }
    return false;
}

int main() {
    FAST;
    cin >> N >> K;
    rep(i, N) cin >> arr[i];

    int lo = 0;
    int hi = N;
    int best;
    while (lo <= hi) {
        int mid = (lo + hi) >> 1;
        if (ok(mid)) {
            best = mid;
            lo = mid + 1;
        }
        else hi = mid - 1;
    }
    cout << best;
    return 0;
}