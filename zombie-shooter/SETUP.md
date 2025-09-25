# Zombie Survival Shooter - Complete Setup Guide

## 🎮 Game Features

### Single-Player Mode
- **Movement**: WASD keys or Arrow keys
- **Shooting**: Arrow keys for directional shooting or Mouse click to shoot towards cursor
- **Health System**: Visual health bar, lose health when hit by zombies
- **Wave System**: Increasing difficulty with each wave
- **Boss Zombies**: Every 5 waves spawn a mini-boss with more health
- **Weapons**: Pistol (default) and Shotgun (spread shot)
- **Power-ups**: Health packs, weapon upgrades, ammo boosts

### Backend Features
- **User Authentication**: Register/Login system
- **Leaderboard**: Top 10 high scores
- **Score Tracking**: Save player progress and statistics
- **Inventory System**: Weapon unlocks and upgrades
- **WebSocket Ready**: Infrastructure for future multiplayer

## 🚀 Quick Start

### Backend Setup

1. **Navigate to backend directory**:
```bash
cd backend
```

2. **Create and activate virtual environment**:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run migrations**:
```bash
python manage.py migrate
```

5. **Create superuser (optional)**:
```bash
python manage.py createsuperuser
```

6. **Start Django server**:
```bash
python manage.py runserver
```

Backend will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**:
```bash
cd frontend
```

2. **Install dependencies**:
```bash
npm install
```

3. **Start React development server**:
```bash
npm start
```

Frontend will be available at `http://localhost:3000`

## 🎯 Game Controls

- **Movement**: WASD keys or Arrow keys
- **Shooting**: 
  - Arrow keys for directional shooting (up/down/left/right)
  - Mouse click to shoot towards cursor position
- **Objective**: Survive as many waves as possible!

## 🔧 Database Configuration

### SQLite (Default - Development)
The project uses SQLite by default for easy setup. No additional configuration needed.

### PostgreSQL (Production)
To use PostgreSQL:

1. **Install PostgreSQL** and create database:
```sql
CREATE DATABASE zombie_shooter;
CREATE USER postgres WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE zombie_shooter TO postgres;
```

2. **Update environment**:
```bash
export USE_SQLITE=False
```

3. **Run migrations**:
```bash
python manage.py migrate
```

## 📊 API Endpoints

### Authentication
- `POST /api/users/register/` - Register new player
- `POST /api/users/login/` - Login player
- `GET /api/users/profile/` - Get player profile

### Scores
- `GET /api/scores/leaderboard/` - Get top 10 scores
- `POST /api/scores/submit/` - Submit game score

### Inventory
- `GET /api/inventory/weapons/` - List all weapons
- `GET /api/inventory/inventory/` - Get player inventory
- `POST /api/inventory/unlock/{id}/` - Unlock weapon
- `POST /api/inventory/equip/{id}/` - Equip weapon

## 🎨 Game Mechanics

### Sprites & Graphics
- **Player**: Green square (32x32px)
- **Zombies**: Red squares (24x24px)
- **Boss Zombies**: Dark red squares (48x48px) - 5x health
- **Bullets**: Yellow squares (8x8px)
- **Power-ups**: 
  - Health: Blue squares (16x16px)
  - Shotgun: Orange squares (16x16px)
  - Ammo: Gray squares (16x16px)

### Scoring System
- **Regular Zombie**: 10 points
- **Boss Zombie**: 100 points
- **Wave Completion**: Bonus points

### Power-up System
- **Health Pack**: Restores 50 health points
- **Shotgun**: Fires 3 bullets in spread pattern, limited ammo
- **Ammo Boost**: Adds 30 rounds to current weapon

## 🔮 Future Enhancements

### Multiplayer Features (WebSocket Ready)
- Co-op survival mode
- Player revival system
- Shared loot and resources
- Real-time communication

### Additional Features
- More weapon types
- Character upgrades
- Different zombie types
- Environmental hazards
- Sound effects and music

## 🐛 Troubleshooting

### Common Issues

1. **CORS Errors**: Make sure both servers are running on correct ports
2. **Database Errors**: Run `python manage.py migrate` after any model changes
3. **Node Version**: Ensure Node.js version 16+ for React compatibility
4. **Port Conflicts**: Change ports in settings if 3000/8000 are occupied

### Development Tips

1. **Hot Reload**: Both React and Django support hot reloading during development
2. **Debug Mode**: Django debug mode is enabled by default for development
3. **Browser Console**: Check browser console for frontend errors
4. **Django Admin**: Access admin panel at `http://localhost:8000/admin/`

## 📁 Project Structure

```
zombie-shooter/
├── frontend/                 # React + Phaser.js
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── game/           # Phaser game logic
│   │   ├── scenes/         # Game scenes
│   │   └── services/       # API services
│   └── package.json
├── backend/                 # Django REST API
│   ├── users/              # User authentication
│   ├── scores/             # Leaderboard system
│   ├── inventory/          # Weapons & upgrades
│   ├── zombie_shooter/     # Main Django project
│   └── requirements.txt
└── README.md
```

## 🎉 Ready to Play!

Once both servers are running:
1. Open `http://localhost:3000`
2. Click "PLAY" to start the game
3. Use "LOGIN" to create an account and save scores
4. Check "LEADERBOARD" to see top players

Survive the zombie apocalypse! 🧟‍♂️