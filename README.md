# Travel Deal Management System

A RESTful API built with **Python**, **Flask**, **SQLAlchemy**, and **SQLite** for managing travel deals. The application supports creating travel deals, viewing deals, searching, filtering, sorting, tracking recently viewed deals, input validation, and logging.

---

## Features

* Create travel deals
* View all travel deals
* View a single travel deal
* Search deals by destination, platform, or travel type
* Filter deals using minimum and maximum price
* Sort deals by price (ascending or descending)
* Track recently viewed deals
* Input validation
* Query parameter validation
* Error handling
* Activity logging
* Modular project structure
* SQLite database integration using SQLAlchemy


---

## Technology Stack

* Python 3
* Flask
* Flask-SQLAlchemy
* SQLite
* SQLAlchemy ORM

---

## Project Structure

```text
TRAVEL_DEAL/
├── database/
│   ├── db.py
│   └── models.py
│
├── routes/
│   └── deals.py
│
├── services/
│   ├── travel_service.py
│   └── recent_service.py
│
├── utils/
│   └── validators.py
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

## Architecture

The application follows a layered architecture:

```text
Request
   ↓
Routes
   ↓
Validators
   ↓
Services
   ↓
Database
   ↓
Response
```

### Responsibilities

#### Routes

Responsible for:

* Receiving requests
* Reading request data
* Calling validation functions
* Calling service functions
* Returning JSON responses

#### Validators

Responsible for:

* Input validation
* Query parameter validation
* Reusable validation logic

#### Services

Responsible for:

* Business logic
* Database operations
* Query construction

#### Database

Responsible for:

* Models
* Database connection
* Data persistence

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

### RecentView

| Field     | Type     |
| --------- | -------- |
| id        | Integer  |
| deal_id   | Integer  |
| viewed_at | DateTime |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/mhbhuiyan99/Travel_Deal.git
cd TRAVEL_DEAL
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Linux/Mac:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python3 app.py
```

Server will start at:

```text
http://127.0.0.1:5000
```

---

## API Summary

| Method | Endpoint | Description |
|----------|----------|----------|
| POST | /deals | Create a travel deal |
| GET | /deals | Get all travel deals |
| GET | /deals/<id> | Get a single travel deal |
| GET | /deals/search | Search deals |
| GET | /deals/filter | Filter deals by price |
| GET | /deals/sort | Sort deals by price |
| GET | /deals/recent | Get recently viewed deals |

---

## Postman Collection

**Collection File:** [Travel Deal.postman_collection.json](https://github.com/mhbhuiyan99/Travel_Deal/blob/main/Travel%20Deal.postman_collection.json)

### Import into Postman

1. Open Postman.
2. Click **Import**.
3. Select **Upload Files**.
4. Choose the downloaded collection file.
5. Import and start testing the APIs.

---

## API Endpoints

### Health Check

#### GET /

Response

```json
{
  "message": "Travel Deal API is running"
}
```

---

### Add Travel Deal

#### POST /deals

Request Body

```json
{
  "destination": "Dubai",
  "price": 5000,
  "platform": "Booking",
  "rating": 4.5,
  "travel_type": "Luxury"
}
```

Success Response

```json
{
  "message": "Deal created",
  "deal": {
    "id": 1,
    "destination": "Dubai",
    "price": 5000,
    "platform": "Booking",
    "rating": 4.5,
    "travel_type": "Luxury"
  }
}
```

Status Code

```text
201 Created
```

---

### Get All Deals

#### GET /deals

Response

```json
{
  "count": 2,
  "data": []
}
```

Status Code

```text
200 OK
```

---

### Get Single Deal

#### GET /deals/<id>

Example

```http
GET /deals/1
```

Status Code

```text
200 OK
```

or

```text
404 Not Found
```

---

### cURL Example

```bash
curl -X POST http://127.0.0.1:5000/deals \
-H "Content-Type: application/json" \
-d '{
  "destination": "Dubai",
  "price": 5000,
  "platform": "Booking",
  "rating": 4.5,
  "travel_type": "Luxury"
}'
```
```bash
curl "http://127.0.0.1:5000/deals"
```

```bash
curl "http://127.0.0.1:5000/deals/1"
```

```bash
curl "http://127.0.0.1:5000/deals/search?destination=dubai"
```

```bash
curl "http://127.0.0.1:5000/deals/filter?min_price=1000&max_price=5000"
```

```bash
curl "http://127.0.0.1:5000/deals/sort?sort_by=price&order=asc"
```

```bash
curl "http://127.0.0.1:5000/deals/recent"
```

### Search Deals

#### GET /deals/search

Query Parameters

| Parameter   | Description           |
| ----------- | --------------------- |
| destination | Search by destination |
| platform    | Search by platform    |
| travel_type | Search by travel type |

Example

```http
GET /deals/search?destination=dubai
```

Features

* Partial search
* Case-insensitive search

---

### Filter Deals

#### GET /deals/filter

Query Parameters

| Parameter | Description   |
| --------- | ------------- |
| min_price | Minimum price |
| max_price | Maximum price |

Example

```http
GET /deals/filter?min_price=1000&max_price=5000
```

---

### Sort Deals

#### GET /deals/sort

Query Parameters

| Parameter | Description |
| --------- | ----------- |
| sort_by   | price       |
| order     | asc / desc  |

Example

```http
GET /deals/sort?sort_by=price&order=asc
```

---

### Recently Viewed Deals

#### GET /deals/recent

Returns recently accessed travel deals.

Example

```http
GET /deals/recent
```

---

## Validation Rules

### Travel Deal Validation

* destination cannot be empty
* platform cannot be empty
* travel_type cannot be empty
* price must be greater than 0
* rating must be between 0 and 5

### Filter Validation

* min_price cannot be negative
* max_price cannot be smaller than min_price
* price values must be valid numbers

### Sort Validation

* sort_by must be price
* order must be asc or desc

### Search Validation

* At least one search parameter is required

---

## Logging

Application logs are stored in:

```text
app.log
```

The following activities are logged:

* Successful search requests
* Successful filter requests
* Successful sort requests
* Invalid requests
* Database errors
* Failed operations

Logging levels used:

```python
logging.info()
logging.warning()
logging.error()
```

---

## Error Handling

The application returns meaningful JSON error responses.

Example:

```json
{
  "error": "Price must be greater than 0"
}
```

Example Status Codes:

```text
200 OK
201 Created
400 Bad Request
404 Not Found
500 Internal Server Error
```

