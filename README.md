# Changes Required for README (Part 03)

## Features

Replace the Features section with:

* Create travel deals
* View all travel deals
* View a single travel deal
* Update travel deals
* Delete travel deals
* Search deals by destination, platform, or travel type
* Filter deals using minimum and maximum price
* Sort deals by price (ascending or descending)
* Track recently viewed deals
* Track most viewed deals
* API usage statistics
* Search statistics
* View count tracking
* Input validation
* Query parameter validation
* Error handling
* Activity logging
* Modular project structure
* SQLite database integration using SQLAlchemy

---

## Project Structure

```text
TRAVEL_DEAL/
├── database/
│   ├── db.py
│   └── models.py
│
├── routes/
│   ├── deals.py
│   └── stats.py
│
├── services/
│   ├── travel_service.py
│   ├── recent_service.py
│   └── stats_service.py
│
├── utils/
│   ├── validators.py
│   └── responses.py
│
├── instance/
│   └── travel_deal.db
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── app.log
└── .gitignore
```

---

## Database Schema

### TravelDeal

| Field       | Type    |
| ----------- | ------- |
| id          | Integer |
| destination | String  |
| price       | Float   |
| platform    | String  |
| rating      | Float   |
| travel_type | String  |
| view_count  | Integer |

### RecentView

| Field     | Type     |
| --------- | -------- |
| id        | Integer  |
| deal_id   | Integer  |
| viewed_at | DateTime |

### ApiStats

| Field               | Type    |
| ------------------- | ------- |
| id                  | Integer |
| total_requests      | Integer |
| successful_requests | Integer |
| failed_requests     | Integer |

### SearchStats

| Field        | Type    |
| ------------ | ------- |
| id           | Integer |
| destination  | String  |
| search_count | Integer |

---

## API Summary

| Method | Endpoint       | Description              |
| ------ | -------------- | ------------------------ |
| POST   | /deals         | Create a travel deal     |
| GET    | /deals         | Get all travel deals     |
| GET    | /deals/<id>    | Get a single travel deal |
| PUT    | /deals/<id>    | Update a travel deal     |
| DELETE | /deals/<id>    | Delete a travel deal     |
| GET    | /deals/search  | Search deals             |
| GET    | /deals/filter  | Filter deals             |
| GET    | /deals/sort    | Sort deals               |
| GET    | /deals/recent  | Recently viewed deals    |
| GET    | /deals/popular | Most viewed deals        |
| GET    | /stats         | API statistics           |

---

## Popular Deals

### GET /deals/popular

Returns the most viewed travel deals.

Example:

```http
GET /deals/popular
```

Status Code:

```text
200 OK
```

---

## Update Travel Deal

### PUT /deals/<id>

Example:

```http
PUT /deals/1
```

Request Body:

```json
{
  "destination": "Dubai",
  "price": 6000,
  "platform": "Booking",
  "rating": 4.8,
  "travel_type": "Luxury"
}
```

Status Codes:

```text
200 OK
404 Not Found
```

---

## Delete Travel Deal

### DELETE /deals/<id>

Example:

```http
DELETE /deals/1
```

Status Codes:

```text
200 OK
404 Not Found
```

---

## API Statistics

### GET /stats

Returns application usage statistics.

Response:

```json
{
  "total_requests": 50,
  "successful_requests": 45,
  "failed_requests": 5,
  "most_searched_destination": "dubai",
  "most_viewed_deal": {
    "id": 1,
    "destination": "Dubai",
    "price": 5000,
    "platform": "Booking",
    "rating": 4.5,
    "travel_type": "Luxury"
  }
}
```

---

## cURL Examples

```bash
curl -X PUT http://127.0.0.1:5000/deals/1 \
-H "Content-Type: application/json" \
-d '{
  "destination": "Dubai",
  "price": 6000,
  "platform": "Booking",
  "rating": 4.8,
  "travel_type": "Luxury"
}'
```

```bash
curl -X DELETE http://127.0.0.1:5000/deals/1
```

```bash
curl "http://127.0.0.1:5000/deals/popular"
```

```bash
curl "http://127.0.0.1:5000/stats"
```

---

## Statistics Tracking

The application tracks:

* Total API requests
* Successful API requests
* Failed API requests
* Most searched destination
* Most viewed travel deal

---

## Logging

Application logs are stored in:

```text
app.log
```

Tracked activities:

* Travel deal creation
* Travel deal updates
* Travel deal deletion
* Search requests
* Filter requests
* Sort requests
* Statistics requests
* Validation failures
* Database failures
* Failed operations

Logging methods:

```python
logging.info()
logging.warning()
logging.error()
```
