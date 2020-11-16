# Requirements
- Install Docker

# Usage
Run docker compose and build `docker-compose up --build -d` (only needed 1st time)
Next time you can just run `docker-compose up -d`

Docker compose will run 2 containers: `app` container and `db` container

open this http://localhost:5000/api/coordinate/monas on your browser
open this http://localhost:5000/api/location?latitude=-6.175307&longitude=106.82734 on your browser

### API

#### GET http://localhost:5000/api/coordinate/monas
```
{
    "latitude": 106.82734,
    "longitude": 106.82734,
    "location": "monas"
}
```

#### GET http://localhost:5000/api/location?latitude=-6.175307&longitude=106.82734
```
response:
{
    "location": "monas",
    "status": "green"
}
```