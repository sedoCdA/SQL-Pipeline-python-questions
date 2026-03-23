'''Question 3 : Ride Booking Analytics Dashboard

A ride-hailing company wants to analyze ride performance across vehicle types.
Each record contains: ride_id, vehicle_type, fare, status (COMPLETED / CANCELLED / NO_SHOW)

Pipeline to implement

Step 1 — GROUP BY vehicle_type
For each vehicle type:
total_rides → count of all records
completed_rides → count where status = COMPLETED
total_earnings → sum of fares (COMPLETED only)
avg_earning → mean of COMPLETED fares (round to 2 decimals)
max_earning → highest COMPLETED fare
Step 2 — COMPUTED COLUMN
completion_rate = (completed_rides / total_rides) × 100 (round to 1 decimal)
Step 3 — FILTER
Keep only vehicle types where completed_rides ≥ M
Step 4 — SORT
Sort by total_earnings DESC
Tie-breaker: vehicle_type alphabetically

Output:
Print performance summary per vehicle type
If none qualify → print "No vehicle types qualify."
Constraint:
Use only lists, loops, and if-elif-else
No dictionary, Counter, or Pandas
Input Format:
Line 1: Integer N
Next N lines: ride_id vehicle_type fare status
Last line: Integer M
'''
N = int(input())

rides = []
for i in range(N):
  ride = input().split()
  rides. append(ride)

M = int(input())

vechile = []
for i in rides:
  if i[1] not in vechile:
    vechile.append(i[1])

details = []
for i in vechile:
  vechile_type = i[1]
  total_rides = 0
  completed_rides=0
  total_earnings=0
  avg_earning=0
  max_earning =0
  for j in rides:
    if i == j[1]:
      total_rides+=1
      if j[3] == "COMPLETED":
        completed_rides+=1
        total_earnings+=int(j[2])
        if int(j[2]) > max_earning:
          max_earning = max(j[2])
  if completed_rides > 0:
    avg_earning = total_earnings / completed_rides
  else:
    avg_earning = 0
  completion_rate = (completed_rides/total_rides)*100

  if completed_rides >= M:
    details.append([vechile_type, total_rides, completed_rides, total_earnings, avg_earning, max_earning])
    

details.sort(key = lambda x : (-x[3], x[0]))

if len(details) == 0:
  print("No vehicle types qualify.")
else:
  for i in details:
    print(i[0], i[1], i[2], i[3], i[4], i[5])
