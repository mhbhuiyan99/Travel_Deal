# Travel Deal Management System

A RESTful API built with **Python**, **Flask**, **SQLAlchemy**, and **SQLite** for managing travel deals. The application supports creating, viewing, updating, deleting, searching, filtering, sorting, tracking deal popularity, tracking recently viewed deals, and generating API usage statistics.

---

## Features

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

## Architecture

The application follows a layered architecture.

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

### Routes

Responsible for:

* Receiving requests
* Reading request data
* Calling validation functions
* Calling service functions
* Returning JSON responses

### Validators

Responsible for:

* Input validation
* Query parameter validation
* Reusable validation logic

### Services

Responsible for:

* Business logic
* Database operations
* Query construction
* Statistics management

### Database

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

## Installation

### Clone Repository

```bash
git clone https://github.com/mhbhuiyan99/Travel_Deal.git
cd Travel_Deal
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Linux / macOS:

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

Server starts at:

```text
http://127.0.0.1:5000
```

---

## API Summary

| Method | Endpoint       | Description            |
| ------ | -------------- | ---------------------- |
| POST   | /deals         | Create a travel deal   |
| GET    | /deals         | Get all travel deals   |
| GET    | /deals/<id>    | Get single travel deal |
| PUT    | /deals/<id>    | Update travel deal     |
| DELETE | /deals/<id>    | Delete travel deal     |
| GET    | /deals/search  | Search travel deals    |
| GET    | /deals/filter  | Filter travel deals    |
| GET    | /deals/sort    | Sort travel deals      |
| GET    | /deals/recent  | Recently viewed deals  |
| GET    | /deals/popular | Most viewed deals      |
| GET    | /stats         | Application statistics |

---

## Postman Collection

**Collection File:** [Travel Deal.postman_collection.json](https://github.com/mhbhuiyan99/Travel_Deal/blob/main/Travel%20Deal.postman_collection.json)

### Import into Postman

1. Open Postman.
2. Click **Import**.
3. Select **Upload Files**.
4. Choose the downloaded collection file.
5. Import and start testing APIs.

---

## API Endpoints

### Health Check

#### GET /

Response

```json
{
  "message": "Welcome to Travel Deal"
}
```

---

### Create Travel Deal

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

Status Code

```text
201 Created
```

---

### Get All Deals

#### GET /deals

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

Status Codes

```text
200 OK
404 Not Found
```

---

### Update Travel Deal

#### PUT /deals/<id>

Example

```http
PUT /deals/1
```

Request Body

```json
{
  "destination": "Dubai",
  "price": 6000,
  "platform": "Booking",
  "rating": 4.8,
  "travel_type": "Luxury"
}
```

Status Codes

```text
200 OK
404 Not Found
```

---

### Delete Travel Deal

#### DELETE /deals/<id>

Example

```http
DELETE /deals/1
```

Status Codes

```text
200 OK
404 Not Found
```

---

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

Example

```http
GET /deals/filter?min_price=1000&max_price=5000
```

---

### Sort Deals

#### GET /deals/sort

Example

```http
GET /deals/sort?sort_by=price&order=asc
```

---

### Recently Viewed Deals

#### GET /deals/recent

Example

```http
GET /deals/recent
```

---

### Most Viewed Deals

#### GET /deals/popular

Example

```http
GET /deals/popular
```

---

### API Statistics

#### GET /stats

Returns:

* Total API requests
* Successful requests
* Failed requests
* Most searched destination
* Most viewed deal

Example Response

```json
{
  "total_requests": 100,
  "successful_requests": 95,
  "failed_requests": 5,
  "most_searched_destination": "dubai",
  "most_viewed_deal": {
    "id": 1,
    "destination": "Dubai"
  }
}
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
* values must be valid numbers

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

Tracked Activities:

* Create requests
* Update requests
* Delete requests
* Search requests
* Filter requests
* Sort requests
* Popular deal requests
* Statistics requests
* Validation failures
* Database failures

Logging Levels:

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
  "error": "Deal not found"
}
```

Common Status Codes:

```text
200 OK
201 Created
400 Bad Request
404 Not Found
500 Internal Server Error
```
