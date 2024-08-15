```bash
 █████╗ ██████╗  ██████╗  ██████╗ █████╗ ██╗  ██╗   ██╗██████╗ ███████╗███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔══██╗██║  ╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝
███████║██████╔╝██║   ██║██║     ███████║██║   ╚████╔╝ ██████╔╝███████╗█████╗
██╔══██║██╔═══╝ ██║   ██║██║     ██╔══██║██║    ╚██╔╝  ██╔═══╝ ╚════██║██╔══╝
██║  ██║██║     ╚██████╔╝╚██████╗██║  ██║███████╗██║   ██║     ███████║███████╗
╚═╝  ╚═╝╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝     ╚══════╝╚══════╝

██████╗  █████╗ ██████╗ ██╗███████╗████████╗ █████╗
██╔══██╗██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗
██████╔╝███████║██████╔╝██║███████╗   ██║   ███████║
██╔══██╗██╔══██║██╔══██╗██║╚════██║   ██║   ██╔══██║
██████╔╝██║  ██║██║  ██║██║███████║   ██║   ██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝

     +-+ +-+ +-+ +-+   +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+
     |T| |H| |E| |'| |9| |0| |s| |A| |R| |E| |B| |A| |C| |K| |!| |!|
     +-+ +-+ +-+ +-+   +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+
```

# Apocalypse Barista

Welcome to *Apocalypse Barista*, a procedurally generated game where you navigate through a post-apocalyptic world, avoid enemies, collect items, and survive!

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Game Mechanics](#game-mechanics)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

*Apocalypse Barista* is a 2D top-down game developed using Pygame. As a player, you'll explore a procedurally generated world that contains barriers, enemies, and items. The main objective is to survive by avoiding enemies, collecting items, and navigating through the barriers that come your way.

## Installation

To run this game, you'll need Python 3.x and Pygame installed on your machine. Please follow the steps below to set up the environment:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/nkkko/apocalypse-barista.git
    cd apocalypse-barista
    ```

2. **Install Pygame:**

    ```bash
    pip install pygame
    ```

## How to Play

1. **Start the game:**

    Run the following command to start the game:

    ```bash
    python main.py
    ```

2. **Controls:**

    - **Arrow Keys**: Move the player
    - **ESC**: Quit the game

3. **Objective:**

    - Avoid enemies as they will decrease your HP.
    - Collect green items to increase your items_collected score.
    - Navigate through blue barriers to explore the world.

## Game Mechanics

- **Player**: The player is represented by a black square. It starts in the middle of the screen, and can move in any direction using the arrow keys.

- **Enemies**: Enemies are represented by red squares. They move in random directions and will change their direction every 0.5-2 seconds. Contact with enemies will reduce the player's HP.

- **Items**: Items are represented by green squares. Collecting these increases the `items_collected` score.

- **Barriers**: Barriers are represented by blue rectangles. They act as obstacles, and the player cannot pass through them.

- **Procedural Generation**: The world is divided into cells, where each cell can contain barriers, items, and enemies. The generation happens dynamically as the player moves.

## Contributing

We welcome contributions to this project. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Send a pull request with a detailed explanation of the changes.

## License

This project is licensed under the Apache 2.0 License. See the `LICENSE` file for details.

---

Enjoy playing *Apocalypse Barista*! If you have any questions or feedback, feel free to open an issue on GitHub or message me directly. Happy exploring!