# Simple Traffic Light FSM

A simple simulation of a traffic light system using a Finite State Machine (FSM). This project demonstrates how an FSM can be used to model traffic lights with basic state transitions (Red, Yellow, Green). The program simulates a traffic light that cycles through the states in a loop, displaying the light color and transitioning automatically after a specified duration.

## Features

- **Traffic Light Simulation**: Simulates a traffic light with Red, Yellow, and Green states.
- **FSM Design**: The system uses a finite state machine to manage state transitions.
- **Automatic State Transitions**: The traffic light automatically cycles through Red, Green, and Yellow states.
- **Visual Representation**: The states are represented by emojis (🔴 for Red, 🟢 for Green, 🟡 for Yellow).
- **Duration Control**: Each state has a defined duration before transitioning to the next state.

## How It Works

The program simulates a traffic light using an FSM. It transitions through the states in the following order:
1. **Red**: The light stays red for 5 seconds.
2. **Green**: The light turns green for 4 seconds.
3. **Yellow**: The light turns yellow for 2 seconds.
4. The cycle repeats indefinitely until the program is stopped.

### State Transitions:
- `Red → Green → Yellow → Red → ...`


