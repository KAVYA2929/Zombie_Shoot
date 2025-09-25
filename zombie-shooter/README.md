# Zombie Survival Shooter

A web-based zombie survival game built with React + Phaser.js frontend and Django backend.

## Features

- **Single-player survival mode**: Move with WASD, shoot with arrow keys or mouse
- **Wave-based zombie spawning**: Increasing difficulty with each wave
- **Health and scoring system**: Track your survival progress
- **REST API backend**: User authentication and leaderboard
- **Real-time gameplay**: Smooth 2D graphics with Phaser.js

## Tech Stack

- **Frontend**: React + TypeScript + Phaser.js
- **Backend**: Django + Django REST Framework
- **Database**: SQLite (development)

## Setup Instructions

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Activate virtual environment and install dependencies:
```bash
source venv/bin/activate
pip install django djangorestframework django-cors-headers channels psycopg2-binary
```

3. Run the Django server:
```bash
python manage.py runserver
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the React development server:
```bash
npm start
```

The game will be available at `http://localhost:3000`

## Game Controls

- **Movement**: WASD keys or Arrow keys
- **Shooting**: 
  - Mouse click to shoot towards cursor
  - Arrow keys for directional shooting
- **Objective**: Survive as many waves as possible!

## API Endpoints

- `POST /api/users/register/` - Register new player
- `POST /api/users/login/` - Login player
- `GET /api/users/profile/` - Get player profile
- `GET /api/scores/leaderboard/` - Get top 10 scores
- `POST /api/scores/submit/` - Submit game score

## Game Mechanics

- **Player**: Green square (32x32px)
- **Zombies**: Red squares (24x24px) that chase the player
- **Bullets**: Yellow squares (8x8px)
- **Waves**: Each wave spawns more zombies with increased speed
- **Health**: Player starts with 100 health, loses 20 per zombie hit
- **Scoring**: 10 points per zombie killed

## Development

The project is structured as:
```
zombie-shooter/
├── frontend/          # React + Phaser.js game
│   ├── src/
│   │   ├── components/
│   │   └── game/
└── backend/           # Django REST API
    ├── users/         # User authentication
    ├── scores/        # Leaderboard system
    └── zombie_shooter/ # Main Django project
```