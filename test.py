if __name__ == "__main__":
    ############################### test ac_simulation
    from ac_simulation import *
    ac_agent = SimpleACReflexAgent(min_threshold=0, max_threshold=100)
    ac_env = SimpleACEnvironment(ac_agent, starting_temp=50)
    
    print("AC simulation #1 starting conditions:")
    print("min-max thresholds: {}, {}".format(ac_agent.min_threshold, ac_agent.max_threshold))
    print("env temperature: {}, num_agent_actions: {}, is_ac_on: {}".format(ac_env.temperature, ac_env.num_agent_actions, ac_env.is_ac_on))
    
    print("-----simulating for 60 timesteps-----")
    ac_env.simulate(60) # expecting temperature: 90, num_agent_actions: 1, is_ac_on: True
    print("env temperature: {}, num_agent_actions: {}, is_ac_on: {}".format(ac_env.temperature, ac_env.num_agent_actions, ac_env.is_ac_on))
    print('______________________')
    
    ac_agent = SimpleACReflexAgent(min_threshold=15, max_threshold=25)
    ac_env = SimpleACEnvironment(ac_agent, starting_temp=20)
    print("AC simulation #2 starting conditions:")
    print("min-max thresholds: {}, {}".format(ac_agent.min_threshold, ac_agent.max_threshold))
    print("env temperature: {}, num_agent_actions: {}, is_ac_on: {}".format(ac_env.temperature, ac_env.num_agent_actions, ac_env.is_ac_on))
    
    print("-----simulating for 48 timesteps-----")
    ac_env.simulate(48) # expecting temperature: 18, num_agent_actions: 5, is_ac_on: True
    print("env temperature: {}, num_agent_actions: {}, is_ac_on: {}".format(ac_env.temperature, ac_env.num_agent_actions, ac_env.is_ac_on))
    print('_______________________________________________________________________')
