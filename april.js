// LeetCode # 121 : Best Time to Buy and Sell Stock

var maxProfit = function(prices) {
    let first = prices[0]
    let maxProfit = 0
    
    for (let i=0; i < prices.length; i++){
        if(prices[i] < first){
            first = prices[i]
        } else {
            maxProfit = Math.max(maxProfit, prices[i] - first)
        }
    }
    
    return maxProfit
};

// LeetCode # 70 : Climbing Stairs

var climbStairs = function(n) {
    if(n >= 0 && n < 3) {
        return n
    }
    
    let arr = [1,2]
    for(let i=2; i < n; i++){
        arr[i] = arr[i-1]+arr[i-2]
    }
    return arr[n-1]
};