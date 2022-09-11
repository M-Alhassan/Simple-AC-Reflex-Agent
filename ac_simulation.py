# Agent class
class SimpleACReflexAgent(object):
    def __init__(self, min_threshold, max_threshold):
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold
    
    # turn AC on or Off
    def select_action(self, percept):
        current_temp = percept[0]
        isOn = percept[1]

        # inistalize status (for console display)
        if isOn:
            status = "On"
        else:
            status = "Off"
        
        # comment this line if testing using test.py 
        print("current temp:", current_temp, "status", status)
        
        # returning the action depending on current temperature and status
        if current_temp <= self.min_threshold:
            if isOn:
                return "TurnOff"
            else:
                return None
        if current_temp >= self.max_threshold:
            if not isOn:
                return "TurnOn"
            else:
                return None
        
# Environment class
class SimpleACEnvironment(object):
    def __init__(self, ac_agent, starting_temp = 28):
        self.ac_agent = ac_agent
        self.temperature = starting_temp
        self.num_agent_actions = 0
        self.is_ac_on = False

    # change the temperature of the room on each call
    def tick(self):
        action = self.ac_agent.select_action([self.temperature, self.is_ac_on])
        if action == "TurnOn":
            self.num_agent_actions +=1
            self.is_ac_on = True

        elif action == "TurnOff":
            self.num_agent_actions +=1
            self.is_ac_on = False

        if self.is_ac_on:
            self.temperature -=1    #decrement room temperature

        elif not self.is_ac_on:
           self.temperature +=1     #increment room temperature

    def simulate(self, num_timesteps):
        for i in range(1, num_timesteps+1):
            self.tick()


############################ Test ############################
# comment this section if testing using test.py

ac_agent = SimpleACReflexAgent(min_threshold=18, max_threshold=26)
ac_env = SimpleACEnvironment(ac_agent)

ac_env.simulate(60)