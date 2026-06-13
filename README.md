# 🔫 Laser-Puff-Clash

A fast-paced two-player laser battle game built with **Python** and **Pygame Zero** for **Stanford's Code in Place 2026**.

## 🎮 About the Game

**Laser-Puff-Clash** is a competitive local multiplayer arcade game where two players battle on a split-screen arena.

* 🔴 **Player 1** controls the Red square.
* 🔵 **Player 2** controls the Blue square.
* ⚪ A white dotted line divides the arena into two halves.
* 🚫 Players cannot cross the center line.
* 🔫 Shoot lasers to hit your opponent and earn points.
* 🏆 The first player to score **5 points** wins the match.

---

## 📸 Game Preview

<img width="100%" alt="Laser Puff Clash Gameplay" src="assets/gameplay.png">

---

## 🎯 Controls

| Action       | Player 1 (Red) | Player 2 (Blue) |
| ------------ | -------------- | --------------- |
| Move Up      | W              | ↑ Up Arrow      |
| Move Down    | S              | ↓ Down Arrow    |
| Move Left    | A              | ← Left Arrow    |
| Move Right   | D              | → Right Arrow   |
| Shoot Laser  | F              | / (Slash Key)   |
| Restart Game | R              | R               |

---

## 🛠 Features

* 🎮 Local 2-player gameplay
* 🔫 Laser shooting mechanics
* ⏱️ Shooting cooldown system
* 💥 Collision detection
* 📊 Live score tracking
* 🏆 Win screen and game restart
* 🚫 Arena boundary restrictions
* ⚡ Fast-paced arcade gameplay

---

## 📥 Installation

### Prerequisites

Make sure you have:

* Python 3.7 or higher
* pip (included with Python)

### Verify Python Installation

#### Windows

```bash
python --version
```

#### macOS / Linux

```bash
python3 --version
```

If Python is not installed, download it from:

https://www.python.org/downloads/

---

## 📦 Install Pygame Zero

### Windows

```bash
pip install pgzero
```

### macOS / Linux

```bash
pip3 install pgzero
```

---

## 📂 Download the Project

### Option 1: Clone the Repository

```bash
git clone https://github.com/yourusername/laser-puff-clash.git
cd laser-puff-clash
```

### Option 2: Download ZIP

1. Click **Code**
2. Select **Download ZIP**
3. Extract the downloaded folder

---

## 🚀 Running the Game

### Windows

```bash
pgzrun laser_clash.py
```

### macOS / Linux

```bash
python3 -m pgzrun laser_clash.py
```

### Alternative (macOS)

If `pgzrun` does not work:

```bash
python3 laser_clash_direct.py
```

---

## 🎲 How to Play

1. Launch the game.
2. Control your player using the assigned keys.
3. Stay on your side of the arena.
4. Shoot lasers to hit your opponent.
5. Earn points for every successful hit.
6. Reach **5 points** before your opponent.
7. Press **R** to restart and play again.

---

## ❓ Troubleshooting

| Problem                     | Solution                                       |
| --------------------------- | ---------------------------------------------- |
| `command not found: pgzrun` | Use `python3 -m pgzrun laser_clash.py`         |
| No game window appears      | Check your Dock or taskbar for the game window |
| `ModuleNotFoundError`       | Run `pip install pgzero` again                 |
| Unable to shoot             | Wait for the shooting cooldown to finish       |

---

## 🧠 What I Learned

Building Laser-Puff-Clash helped me learn:

* Event-driven programming
* Keyboard input handling
* Collision detection
* Game state management
* Score tracking systems
* Cooldown mechanics
* Object-oriented programming concepts
* Real-time game development with Python

One of the most challenging parts was implementing accurate laser collision detection and balancing the shooting cooldown. Seeing the game become fully playable was the most rewarding part of the project.

---

## 🏗 Built With

* Python 3
* Pygame Zero
* Stanford Code in Place 2026

---

## 👨‍💻 Author

**Rehan Azim**

Code in Place 2026 Final Project

Passionate about building technology that educates, empowers, and creates impact.

⭐ If you enjoyed this project, consider giving it a star!
