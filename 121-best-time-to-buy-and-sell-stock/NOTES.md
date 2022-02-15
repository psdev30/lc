#two pointers
* always want to buy at the lowest price, right? so keep track of that in a var
* now, you move to the next day and its price.. if it's higher, great! calculate the profit
* --> if this newly found profit is > the current maximum profit, update the max profit!
* now if the price is lower, though, selling would be a net negative..
* --> while this isn't good, there's a bright side! we found a lower price that we could buy at instead of the previous price we thought was the best price to buy at, so make this our lowest price!
* ---------> while this doesn't guarantee we'll find a better maxProfit from this move, it gives us a chance, and we already are tracking the maximum profit as of now in the case that there isn't a better maxProfit than we already found