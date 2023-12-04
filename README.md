# Vertexcover Assignment
This is my solution for the Vertexcover take home assignment.  
Deployed at: https://vertexcover-216ec2f7cbaa.herokuapp.com/

Repo links:
1. HTTPS: https://github.com/doesitbyte/Vertexcover.git
2. SSH: git@github.com:doesitbyte/Vertexcover.git

## Setup Instructions
1. Clone the repository
2. Navigate into the root of the repo
### For MacOS/Linux  
   Run the following commands
   ```sh
   $ python3 -m venv .venv
   ```
   ```sh
   $ .venv/bin/activate
   ```
   ```sh
   $ pip install -r requirements.txt
   ```
   ```sh
   $ flask run
   ```

### For Windows  
   Run the following commands
   ```sh
   $ py -3 -m venv .venv
   ```
   ```sh
   $ .venv\Scripts\activate
   ```
   ```sh
   $ pip install -r requirements.txt
   ```
   ```sh
   $ flask run
   ```

*Note: Use the /status endpoint to check if the server is running*

## Test Instructions

### Unit Tests

From the root of the project run 

```sh
python -m unittest tests.py
```

to exceute the unit tests already designed to test the APIs for various conditions.

### API Testing (Deployment)

Use curl to test individual APIs

**Add Coupon**
```
curl -X POST -H "Content-Type: application/json" -d '{"code": "TEST123", "user_total_repeat_count": 2, "user_per_day_repeat_count": 1, "user_per_week_repeat_count": 1, "global_total_repeat_count": 5}' https://vertexcover-216ec2f7cbaa.herokuapp.com/coupon/add
```
**Verify Coupon Validity**
```
curl -X POST -H "Content-Type: application/json" -d '{"code": "TEST123", "user_id": "user1"}' https://vertexcover-216ec2f7cbaa.herokuapp.com/coupon/validate
```
**Apply Coupon**
```
curl -X POST -H "Content-Type: application/json" -d '{"code": "TEST123", "user_id": "user1"}' https://vertexcover-216ec2f7cbaa.herokuapp.com/coupon/apply
```
**Coupon Details**
```
curl -X POST -H "Content-Type: application/json" -d '{"code": "TEST123"}' https://vertexcover-216ec2f7cbaa.herokuapp.com/coupon/apply
```

### API Testing (Local)

Use curl to test individual APIs

**Add Coupon**
```
curl -X POST -H "Content-Type: application/json" -d '{"code": "TEST123", "user_total_repeat_count": 2, "user_per_day_repeat_count": 1, "user_per_week_repeat_count": 1, "global_total_repeat_count": 5}' http://127.0.0.1:5000/coupon/add
```
**Verify Coupon Validity**
```
curl -X POST -H "Content-Type: application/json" -d '{"code": "TEST123", "user_id": "user1"}' http://127.0.0.1:5000/coupon/validate
```
**Apply Coupon**
```
curl -X POST -H "Content-Type: application/json" -d '{"code": "TEST123", "user_id": "user1"}' http://127.0.0.1:5000/coupon/apply
```
**Coupon Details**
```
curl -X POST -H "Content-Type: application/json" -d '{"code": "TEST123"}' http://127.0.0.1:5000/coupon/apply
```

*Note: Port number might be different for your local instance of the flask app. Please replace 5000 with whatever port your flask app is running on.*
   
## Assumptions

1. There exists a way to get some form of a unique identifier for all users, referred to as 'user_id' in the API implementation.
2. The coupon codes are in the form of standard strings.
3. Validity for coupons on the time axes are done purely by calculating the time difference using previous usages of coupons by the user rather than implementing a 'refresh at midnight' approach.

## Trade Offs

1. One major trade off is the use of a in-memory database abstraction rather than a persistent memory store for simplicity which may lead to challenges handling large datasets and server restarts.
2. The current implementation does not allow updating coupon codes for increasing limits for usage.
3. For the sake of simplicity, security measures were not covered deeply (Eg. encryption of coupon codes, token based authentication, rate limiting)

## Scalability Challenges
Increased computation times, data sync errors and potential bottlenecks may arise as the API scales for a large number of users due to the in-memory nature of the solution. Caching mechanisms, load balancing, and database sharding could be explored to enhance scalability.

## More Tests
1. Invalid input data
2. Missing required fields
3. Concurrent requests
4. Load testing