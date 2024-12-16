import time

class TrafficLightFSM:
    def __init__(self):
        # Define the states and their transitions
        self.states = {
            "Red": {"next": "Green", "duration": 5},
            "Green": {"next": "Yellow", "duration": 4},
            "Yellow": {"next": "Red", "duration": 2},
        }
        self.current_state = "Red"  # Initial state

    def run(self):
        print("Traffic Light FSM Started. Press Ctrl+C to stop.")
        try:
            while True:
                # Get the current state's details
                state_info = self.states[self.current_state]
                print(f"Current State: {self.current_state}")
                print(f"Light: {self.get_light_color(self.current_state)}")
                time.sleep(state_info["duration"])  # Wait for the state's duration
                # Transition to the next state
                self.current_state = state_info["next"]
        except KeyboardInterrupt:
            print("\nTraffic Light FSM Stopped.")

    @staticmethod
    def get_light_color(state):
        # Map states to light colors for visualization
        colors = {
            "Red": "🔴",
            "Green": "🟢",
            "Yellow": "🟡",
        }
        return colors.get(state, "❓")

# Run the Traffic Light FSM
if __name__ == "__main__":
    fsm = TrafficLightFSM()
    fsm.run()
