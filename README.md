# Conveyor Belt Simulation

## Overview
This project simulates a conveyor belt production line where workers pick components (A and B) from the belt, assemble them into a finished product (C), and place the product back onto the conveyor belt. The simulation tracks the number of completed products and unused components.

## Project Structure
```
conveyor_belt_simulation/
│── tests/
│   ├── test_conveyor_simulation.py  # Unit tests for Worker and ConveyorBeltSimulation
│
├── src/
│   ├── worker.py                     # Worker class definition
│   ├── simulation.py                  # ConveyorBeltSimulation class definition
│
├── main.py                           # Entry point to run the simulation
│── flowchart.png                     # Flow chart of conveyor belt
│── README.md                         # Documentation
```

## Thought Process 
### 1️⃣ Flowchart & Planning
- The initial idea was to design a simple but extensible simulation that follows conveyor belt systems.
- Using ChatGPT, I first crafted a flowchart outlining how components appear randomly on the belt, how workers interact with components and how finished products are placed back onto the belt.
- However, the initial flowchart had inefficiencies, including duplicated actions, redundant worker-pair logic and missing steps and cases. I optimized the system by reducing duplicate actions and ensuring that workers coordinate effectively by adding suitable steps.

### 2️⃣ Code Development 
The code was broken down into modular sections:
- `worker.py`: Worker actions and states.
- `simulation.py`: Conveyor belt logic and worker interactions.
- `main.py`: Entry point to run the simulation.
- `test_conveyor_simulation.py`: Unit tests for core functionalities.
  
ChatGPT assisted in refining function structures and improving code maintainability & flexibility.

## File Descriptions
### **1️⃣ `worker.py`**
- Contains the `Worker` class, responsible for picking components and assembling products.
- Handles item collection, assembly process and product placement.

### **2️⃣ `simulation.py`**
- Contains the `ConveyorBeltSimulation` class, which manages conveyor belt movement, worker interactions with the belt and tracking finished products and unused components.
- Implements the main logic for the factory simulation.

### **3️⃣ `main.py`**
- Serves as the entry point to start the simulation.
- Runs an instance of `ConveyorBeltSimulation` and prints results.

### **4️⃣ `test_conveyor_simulation.py`**
- Contains unit tests to validate the correctness of the `Worker` and `ConveyorBeltSimulation` classes.
- Ensures correct:
  - Worker behavior (picking items, assembling products, etc.).
  - Conveyor belt movement and product handling.
  - Overall simulation results (finished products and unused components).

## Installation
### **Prerequisites**
- Python 3.6+


## Running the Simulation
To start the conveyor belt simulation, run:
```sh
python main.py
```

## Running Tests
To ensure everything is working correctly, run:
```sh
python -m unittest discover tests
```


## How It Works
1. Components `A`, `B` and `None` appear randomly on the conveyor belt.
2. Workers pick up these components and start assembling a product `C`.
3. Assembly takes 4 steps by default.
4. Once assembled, workers place the product back onto the conveyor belt.
5. The simulation runs for 100 steps and calculates the number of completed products and unused components.

## Expected Test Output
When running unit tests, you should see output like:
```sh
.
----------------------------------------------------------------------
Ran X tests in Y.YYYs

OK
```
If you see:
```sh
Unused Components: {'A': 0, 'B': 0}
```
It means all components were picked up successfully, and the system was highly efficient.

## Assumptions
- Workers can hold only two items at a time (one in each hand).
- Each worker pair must work together without interfering in the same conveyor slot simultaneously.
- The probability of a component appearing is equally distributed (1/3 for `A`, `B`, or `None`).
- The simulation assumes workers react instantly and optimally to components appearing on the conveyor belt.
- There is no downtime or inefficiency modeled in worker behavior.

## Evaluate Code Quality and Extensibility
- The code is structured in a way that allows for easy modification and extension.
- Each major component (worker, conveyor belt, simulation) is separated into individual files for maintainability.
- The logic is modular, making it easier to introduce new features such as:
  - Additional worker constraints (fatigue, skill levels,...).
  - Different conveyor belt speeds or component probabilities.
  - More complex product recipes beyond just `A + B = C`.
- While the solution is somewhat flexible, excessive complexity (such as a full simulation engine) was avoided to keep the implementation readable and maintainable.

## Areas for Improvements
### Code Quality
- Logging: Currently, print statements are used to display results. Using Python’s logging module would be better for debugging and tracking issues.
- Exception Handling: The code assumes that all input conditions are valid. Adding error handling for unexpected cases (such as invalid component values) would improve robustness.

### Extensibility
- Encapsulation of Configuration: Parameters like assembly_time, conveyor_len, etc., are hardcoded in simulation.py. Moving them to a separate config.py file would improve flexibility.

### Flexibility
- Limited dynamic behavior: Workers always act optimally and never make mistakes. Adding randomness (failure to pick items, dropping items,...) would make the system more flexible.

### Maintainability
- Code Duplication in Worker Actions: The logic for picking up items and checking if an item can be placed has some repetition, which could be refactored for clarity.
- Testing Could Be Expanded: Right now, tests cover core functionalities, but edge cases (such as conveyor failures, worker inefficiencies) could be tested as well.

