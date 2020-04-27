import numpy as np

class SIRmodel:
    
    def __init__(self, total_pop):
        
        self.total_pop = total_pop
        self.days_ill = 10
    
    def run_reduced_model(self, days, r_0, initial_sick):
                
        N_infected, N_recovered = self.run_model(days=days, initial_sick=initial_sick, r_0=r_0)
        
        return N_infected + N_recovered
    
    def run_model(self, days, r_0, initial_sick):
        
        days_of_contagion = len(days)
        p_rec = 1./self.days_ill
        current_day = 0
        
        N_infected = []
        N_recovered = []
        N_uninfected = []
        N_last_n_days = np.zeros(self.days_ill)

        # use the same parameters as the logistic model to look at the total number of infected
        N_inf = initial_sick
        N_rec = 0
        
        while current_day < days_of_contagion:
            N_infected.append(N_inf)
            N_recovered.append(N_rec)
            N_uninfected.append(self.total_pop - N_rec - N_inf)

            new_cases = r_0 * N_inf * (self.total_pop - N_rec - N_inf)/self.total_pop
            cured_cases = np.sum(N_last_n_days * p_rec)
            N_inf = N_inf - cured_cases + new_cases
            N_rec = N_rec + cured_cases
            N_last_n_days[1:] = N_last_n_days[:-1]
            N_last_n_days[0] = new_cases
            current_day += 1
            
        N_recovered = np.array(N_recovered)
        N_infected = np.array(N_infected)
        N_uninfected = np.array(N_uninfected)
                                                 
        return N_infected, N_recovered
