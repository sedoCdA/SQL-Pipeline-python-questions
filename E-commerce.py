'''Question 5 : E-commerce Seller Performance Leaderboard

An e-commerce platform wants to rank top-performing sellers based on delivered orders and commission earned.
You are given two tables:
  
Sellers table:
seller_id, seller_name, seller_type (PREMIUM / STANDARD / BASIC)
  
Orders table:
order_id, seller_id, order_value, status (DELIVERED / CANCELLED)
  
Write a function get_commission_rate(seller_type):
PREMIUM → 10%
STANDARD → 7%
BASIC → 4%
  
Pipeline to implement:
Step 1 — FILTER
Keep only orders where status = 'DELIVERED'
Step 2 — LOOKUP
Map each order to seller_name and seller_type using seller_id
Step 3 — ELEMENT-WISE COMPUTATION
commission = (order_value × rate) // 100
Step 4 — GROUP BY seller_id
For each seller compute:
order_count
total_sales
total_commission
Step 5 — FILTER AGAIN
Keep sellers where total_sales ≥ S
Step 6 — SORT
By total_commission DESC
Tie → seller_name alphabetically
Step 7 — OUTPUT
Print ranked seller leaderboard
If none qualify → "No sellers qualify."

Constraints:
Use only loops, lists, and if-elif-else
No dictionaries, Counter, or libraries

Input Format:
Line 1: N (sellers)
Next N lines: seller_id seller_name seller_type
Line after: M (orders)
Next M lines: order_id seller_id order_value status
Last line: Integer S '''


def get_commision(type):
  return 10 if type =="Premium" else 7 if type =="Standard" else 4

n1 = int(input())
sellers = []
for i in range(n1):
  seller = input().split()
  #seller_id = seller[0]
  #seller_name = seller[1]
  #seller_type = seller[2]
  sellers.append(seller)

n2 = int(input())
orders =[]
for i in range(n2):
  order = input().split()
  #order_id =  order[0]
  #seller_id = order[1]
  #order_value = order[2]
  #status = order[3]
  orders.append(order)

t= int(input())

delivered =[]
for i in orders:
  if i[3] =="DELIVERED":
    delivered.append(i)

results = []

for s in sellers:
  seller_id = s[0]
  seller_name = s[1]
  seller_type = s[2]
  order_count=0
  total_sales=0
  total_commission=0

  for d in delivered:
    if d[1] ==  seller_id:
      order_count+=1
      total_sales+=int(d[2])
      commision = get_commision(seller_type) * int(d[2]) // 100
      total_commission += commission

  if total_sales >= t:
    results.append([seller_id, seller_name, order_count, total_sales, total_commission])


results.sort(key = lambda x: (-x[-1], x[1]))


if len(results)==0:
  print("No seller")
else:
  for i in results:
    print(i[0], i[1], i[2], i[3], i[4])


