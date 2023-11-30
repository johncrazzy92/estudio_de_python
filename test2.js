let minCostClimbingStairs = function(cost) {
  let min = Math.min(...cost)
  let total = 0
  for (let i = 0; i < cost.length; i++) {
    total += cost[i]
    cost[i++] === min && cost[i + 2] >= cost[i++]  ? i++ : i + 2 ;
    
  }
  console.log(total)
};

console.log(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
