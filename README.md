# Traffic Light Simulator

This project is a simple traffic light simulator implemented in Python using the `tkinter` library. It provides a graphical user interface (GUI) that simulates traffic lights for both vehicles and pedestrians. The simulator can be used to demonstrate the basic functionality of traffic lights and pedestrian crossing signals.

## Features

- **Two Traffic Light Systems:** 
  - A set of traffic lights for vehicles.
  - A set of traffic lights for pedestrians.
  
- **Traffic Light Colors:**
  - Vehicle lights: Red, Yellow, Green.
  - Pedestrian lights: Red, Green.

- **Automatic Light Change:** The traffic lights automatically change colors according to the standard traffic light sequence.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python installations)

## How to Run

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/traffic-light-simulator.git
    cd traffic-light-simulator
    ```

2. **Run the script:**
    ```bash
    python Traffic_Light.py
    ```

3. **View the simulation:**
   - Once you run the script, a window will appear showing the traffic light simulation.
   - The lights will automatically change from red to green to yellow for vehicles and from red to green for pedestrians.

## How It Works

The simulator creates a window using `tkinter` with two sets of traffic lights. The lights are represented as colored circles that change their color based on a timed sequence:

- **Vehicle Traffic Lights:**
  - Red: Stop
  - Yellow: Get Ready
  - Green: Go

- **Pedestrian Traffic Lights:**
  - Red: Do Not Cross
  - Green: Cross

The sequence of light changes is controlled by a loop within the program, with a delay between each light change to simulate the timing of real traffic lights.

## Screenshots

_Add screenshots of the traffic light simulator here._

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was developed as a simple demonstration of a traffic light system using Python.

---

Feel free to fork this project and modify it to add more features or improve the existing ones!
