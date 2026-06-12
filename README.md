# Travel Deal Management System

A Flask-based RESTful API backend built for managing travel deals. This system uses a modular project structure separating data layers, routes, business logic, and input utilities.

---

## Prerequisites

Make sure you have Python 3 installed on your computer.

---

## How to Setup and Run

Follow these instructions in your computer terminal or command prompt to run the project.

### 1. Download the Project

Clone the repository and enter the directory:

```bash
git clone https://github.com/mhbhuiyan99/Travel_Deal.git
cd Travel_Deal

```

### 2. Create a Virtual Environment

Isolate the dependencies for this project:

```bash
python3 -m venv .venv

```

### 3. Activate the Virtual Environment

Activate the environment depending on your operating system:

* **Linux / macOS:**
```bash
source .venv/bin/activate

```


* **Windows (Command Prompt):**
```cmd
.venv\Scripts\activate

```



### 4. Install Dependencies

Install all required libraries listed in the requirements file:

```bash
pip install -r requirements.txt

```

### 5. Start the Server

Run the application starter script:

```bash
python3 app.py

```

The application will start running locally at `http://127.0.0.1:5000/`. The database file will initialize automatically upon startup.

---

## API Endpoints

### 1. Add Travel Deal

* 
**Method:** `POST` 


* 
**URL:** `http://127.0.0.1:5000/deals` 


* 
**Request JSON Body:** 



```json
{
  "destination": "Dubai",
  "price": 5000,
  "platform": "Booking",
  "rating": 4.5,
  "travel_type": "Luxury"
}

```

### 2. Get All Deals

* 
**Method:** `GET` 


* 
**URL:** `http://127.0.0.1:5000/deals` 



### 3. Get Single Deal

* 
**Method:** `GET` 


* 
**URL:** `http://127.0.0.1:5000/deals/<id>` 
*(Replace `<id>` with the numerical ID of the deal, such as `1`)*



---

## Postman Collection

You can access and import the workspace testing endpoints collection directly via the following link:

[https://mojammelhaquebhuiyan.postman.co/workspace/Mojammel-Haque-Bhuiyan's-Worksp~ab05c571-6053-4a06-8fb8-855de37e8fbc/collection/43992633-a8e1c16d-b565-46be-80a4-2ea8a51ddbda?action=share&creator=43992633](https://mojammelhaquebhuiyan.postman.co/workspace/Mojammel-Haque-Bhuiyan's-Worksp~ab05c571-6053-4a06-8fb8-855de37e8fbc/collection/43992633-a8e1c16d-b565-46be-80a4-2ea8a51ddbda?action=share&creator=43992633)

## Project Structure
project/
├── app.py               # Application Factory & entry point
├── config.py            # Environment & app configuration constants
├── database/
│   ├── db.py            # SQLAlchemy core engine initialization
│   └── models.py        # Database declarative schemas (TravelDeal model)
├── routes/
│   └── deals.py         # Blueprint endpoint route definitions
├── services/
│   └── travel_service.py # Pure isolated business & database transactions logic
├── utils/
│   └── validators.py    # Type-safe request input constraints validation
├── requirements.txt     # Locked production dependencies
└── README.md            # System installation and architectural blueprint