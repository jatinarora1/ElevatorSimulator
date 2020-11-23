# ElevatorSimulator

Like all elevators, ours can go up and down. We define constants for these. The elevator also happens to be in a building with six floors.
Made an Elevator class that simulates an elevator. It will delegate to another class which contains the elevator logic, i.e. deciding what the elevator should do.

A user can interact with the elevatorby pressing the up or down button on any floor, and can select a destination floor by pressing the button for that floor on the panel in the elevator.

## Simulation
The simulation runs in steps. Each time step consists of the elevator moving a single floor, or pausing at a floor. Either way, the logic delegate gets notified. Along the way, I print out the movements of the elevator so that I can keep track of it. I also define a few helper methods that advance the simulation to points of interest, for ease of testing.

# Result
To run the elevator simulator run command 
`python3 result.py`
Enter the dest_floor and direction as per choice
