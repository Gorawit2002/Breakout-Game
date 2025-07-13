# 🧱 Breakout Game with Procedural Patterns, Power-Ups & Dynamic Difficulty

An enhanced version of the classic **Breakout game**, built using **Python** and **Pygame**. This version introduces **procedural level generation**, **power-ups**, **multi-ball**, **paddle resizing**, **state-based architecture**, and **custom theming** with JSON sprite files.

> 🎥 [Watch Gameplay Demo on YouTube](https://youtu.be/vKd_EFJYfuM)

[![Gameplay Video](https://img.youtube.com/vi/vKd_EFJYfuM/0.jpg)](https://youtu.be/vKd_EFJYfuM)

---

## 🎮 Game Overview

This Breakout game blends fast-paced arcade mechanics with creative upgrades. Levels are generated using procedural patterns like **RAINBOW**, **CHECKERBOARD**, and more. Players can collect power-ups, manage multiple balls, and adapt as gameplay gets harder over time.

---

## 🧩 Key Features

### 🔁 Procedural Content Generation (PCG)
- Auto-generates bricks using visual patterns:  
  `RAINBOW`, `DOTTED`, `CHECKERBOARD`, `SOLID`, etc.

### ⚡ Power-Ups & Items

- **Spread Ball Power-Up**  
  Adds multiple balls that launch in different directions.

- **Ball Speed Increase Power-Up**  
  Boosts the ball’s speed by 20%, increasing difficulty.

- **Paddle Size Increase Power-Up**  
  Temporarily enlarges the paddle to make hitting easier.

- **Paddle Speed Decrease Power-Up**  
  Slows down paddle movement (negative item), encouraging players to avoid it.

---

### 🎮 Gameplay Mechanics

- Multi-ball support with independent ball physics  
- Boost mechanics and paddle physics  
- Ball deflects accurately based on paddle hit position  
- Dynamic score and health bar UI  

---

### 🎨 Visual & Audio

- Game themed with sprite-based assets defined in structured JSON  
- Paddle/ball color changes based on state  
- Custom font, sound effects (if enabled)

---

## 🛠️ Tech Stack

- **Language**: Python 3  
- **Library**: Pygame  
- **Game Architecture**: Modular OOP with state machines  
- **Asset Design**: JSON metadata for sprite and layout definition

---

## 🚀 How to Run

1. Install dependencies:
```bash
pip install pygame
```

2. Run the game:
```bash
python main.py
```
## 🎮 Controls

- **Arrow Keys (← / →)**: Move paddle  
- **Enter**: Start / Confirm selection  
- **Escape**: Exit / Go back  
- Multi-ball handled automatically during gameplay

---

## 📚 What I Learned

- Designing **procedural level generators** using algorithmic patterns  
- Implementing a **modular state machine** to manage menus, play, pause, and game over  
- Creating **interconnected gameplay systems** (e.g., ball-paddle-brick interactions with upgrades)  
- Integrating **custom sprite rendering** and item metadata using JSON  

---

## 📄 License

This project is for educational and portfolio use only.

---

## 🙌 Credits
 
- Sprites designed using JSON layout files  
- Sounds and fonts (if used) from open-source libraries
