"""
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
 

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
 

Constraints:

1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= steps <= 100
homepage and url consist of  '.' or lower case English letters.
At most 5000 calls will be made to visit, back, and forward.

"""
# time complex visit O(1), back and forward O(step), worst case O(N)
# space create a linkedlist O(N)

# Algorithm
# Create a class DLLNode for each node of the doubly linked list:
# It contains a string variable data to store the URL string.
# And two pointers prev and next pointing to the rest of the doubly linked list.
# In the BrowserHistory class, we create two variables:
# linkedListHead, points to the head of our doubly linked list and is storing the homepage URL.
# current, it will always point to the current URL node in our doubly linked list.
# Implementing visit(url) method:
# We create a new node for url.
# Make our current node's next point to this new node and the new node's prev point to the current node. Thus, deleting the link of the next nodes of current and inserting the new node in our doubly linked list.
# Then, mark this new node as the current node.
# Implementing back(steps) method:
# We will move the current pointer towards the left (using prev pointer) in the doubly linked list if nodes are present and the step number of nodes is not traversed.
# At the end, we return the current node's URL.
# Implementing forward(steps) method:
# We will move the current pointer towards the right (using next pointer) in the doubly linked list if nodes are present and the step number of nodes is not traversed.
# At the end, we return the current node's URL.

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head


    def visit(self, url: str) -> None:
        visit_node = Node(url)
        self.curr.next = visit_node
        visit_node.prev = self.curr
        self.curr = visit_node



        

    def back(self, steps: int) -> str:
        while steps and self.curr.prev:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)