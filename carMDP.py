import numpy as np

# define a "state" class
# which consists of its name, reward, and a list of possible actions from this state
class State:
    def __init__(self, name, actions):
        self.name = name
        self.actions = actions
    
    def __str__(self):
        return self.name
    
# Define 3 states Cool, Warm, and Overheated
# and possible actions from each state

Cool = State("Cool", ["Slow", "Fast", "slow", "fast"])
Warm = State("Warm", ["Slow", "Fast","slow","fast"])
Overheated = State("Overheated", ["Slow","Fast","slow","fast"])

# Initialize the current state to Cool
current_state = Cool

# Initialize the total reward to 0
total_reward = 0

# Initialize the list of states visited to empty
states_visited = []

# Initialize the total distance to 0
total_distance = 0




# First line is the number of actions
num_actions = int(input("enter no of actions "))

actions = []

# Read the actions
for i in range(num_actions):
    actions.append(input())

# Iterate over the actions
for action in actions:
    # Check if the action is valid
    if action not in current_state.actions:
        print("Invalid action")
        break

    # Add the current state to the list of states visited
    states_visited.append(current_state)

    # Update the current state and the total reward and distance based on the action
    if current_state.name == "Warm":
        if action == "Slow" or action == "slow":
            x = np.random.randint(0, 2)
            if x == 0:
                current_state = Warm
            else:
                current_state = Cool
            total_reward += 1
            total_distance += 0.5
        elif action == "Fast" or action == "fast":
            current_state = Overheated
            total_reward -= 10
            
        else:
            print("Invalid action")
            break
    elif current_state.name == "Cool":
        if action == "Slow" or action == "slow":
            current_state = Cool
            total_reward += 1
            total_distance += 1
        elif action == "Fast" or action == "fast":
            x = np.random.randint(0, 2)
            if x == 0:
                current_state = Cool
            else:
                current_state = Warm
            total_reward += 2
            total_distance += 2
        else:
            print("Invalid action")
            break
    elif current_state.name == "Overheated":
        
        break
    else:
        print("Something went wrong")
        break

# Print the states visited
print("States visited:")
for state in states_visited:
    print(state)

# Print the total reward and distance
print("Total reward: ", total_reward)
print("Total Distance: ",total_distance)

# Print whether car reached the end or halted midway
if  current_state.name != "Overheated":
    if total_distance < 20 and current_state.name != "Overheated":
        print("Halted midway")
    else:
        print("Reached")





