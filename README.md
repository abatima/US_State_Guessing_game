# U.S. States Guessing Game 🤠
An educational geography game designed to test and improve knowledge of U.S. geography. Built using **Python**, **Pandas**, and **Turtle**, this game combines data science fundamentals with interactive graphics.

The project has been architected with **Object-Oriented Programming (OOP)** principles to ensure modularity, scalability, and clean data separation.

## 🚀 Key Features

* **Vectorized Data Handling:** Utilizes **Pandas** for efficient state coordinate lookups and membership verification.
* **OOP Architecture:** Features a modular design with dedicated classes for game state management and UI rendering.
* **Persistent Learning:** Automatically generates a `missing_states.csv` upon exit, allowing players to identify and study the states they missed.
* **Dynamic Coordinate Mapping:** Uses the `teleport()` method for instant, flicker-free labeling of states on a custom-mapped background image.
* **Real-time Scoring:** A dynamic header tracks your progress (e.g., `12/50 States Correct`) as you play.

## 🛠️ Built With

* [Python 3](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/) - For CSV data manipulation and filtering.
* `turtle` library - For the graphical interface and coordinate-based text placement.

## 🕹️ Getting Started

### Prerequisites

You will need Python 3.x and the Pandas library installed:

```bash
pip install pandas

```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/abatima/US_State_Guessing_game.git

```


2. Navigate to the project folder:
```bash
cd US_State_Guessing_game

```



### Running the Game

Launch the interactive map by running:

```bash
python main.py

```

## 📂 File Structure

* `main.py`: The central game engine that manages the primary loop and user input.
* `state_writer.py`: Handles the **Turtle** logic for "teleporting" and writing state names at specific coordinates.
* `scoreboard.py`: Encapsulates the **Pandas** logic, including state verification and high-speed **Set Subtraction** for missing data exports.
* `50_states.csv`: The source dataset containing state names and their corresponding (x, y) coordinates on the map.
* `blank_states_img.gif`: The graphical background used for the game map.

## 📊 Data Management

The game logic utilizes **Set Subtraction** to compare the player's performance against the master list. This ensures  lookup speeds and efficient data cleaning for the final export:

```python
# Efficient SME-level data filtering
missing_states = list(set(all_states) - set(guessed_states))

```

## 📜 License

This project is open-source and available under the [MIT License](https://en.wikipedia.org/wiki/MIT_License).

---

*Developed by [abatima](https://github.com/abatima)
