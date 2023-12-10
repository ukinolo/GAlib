from testing_functions import functions, stored_minimums
import os
import sys
from itertools import zip_longest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.galib import Selection, Crossover, Replacement, Mutation, Fitness, GA

import pandas as pd


#Defining all the parameters for all the algorithms
number_of_creatures = 100
interval_min = -100
interval_max = 100
rounds = 1000

run_times = 10
early_stopping_rounds = 50

mutation_probabilities =  [0.7, 0.9,  0.9, 0.8, 0.7, 0.8, 0.65, 0.9, 0.9]
dimension_probabilitise = [0.2, 0.05, 0.1, 0.2, 0.1, 0.1, 0.1,  0.1, 0.1]

selections = [
    Selection('ranking', max_rank_multiplier=15.0),
    Selection('ranking', max_rank_multiplier=10.0),
    Selection('ranking', max_rank_multiplier=10.0),
    Selection('tournament', tournament_size=3),
    Selection('tournament', tournament_size=5),
    Selection('tournament', tournament_size=8),
    Selection('tournament', tournament_size=8),
    Selection('ranking', max_rank_multiplier=15.0),
    Selection('ranking', max_rank_multiplier=15.0),
]

crossovers = [
    Crossover('sbx', distribution_index=1.5, probability_of_crossover=0.1),
    Crossover('sbx', distribution_index=1.5, probability_of_crossover=0.2),
    Crossover('sbx', distribution_index=1.5, probability_of_crossover=0.2),
    Crossover('sbx', distribution_index=1.3, probability_of_crossover=0.1),
    Crossover('bland', alpha=0.5),
    Crossover('bland', alpha=0.7),
    Crossover('bland', alpha=0.7),
    Crossover('bland', alpha=0.5),
    Crossover('bland', alpha=0.5),
]

replacements = [
    Replacement('elitism', elitism_width=0.1),
    Replacement('best'),
    Replacement('best'),
    Replacement('elitism', elitism_width=0.1),
    Replacement('best'),
    Replacement('elitism', elitism_width=0.05),
    Replacement('elitism', elitism_width=0.05),
    Replacement('elitism', elitism_width=0.05),
    Replacement('elitism', elitism_width=0.05),
]

mutations = [
    Mutation('normal', mutation_probabilities[0], dimension_probabilitise[0], standard_deviation=1.8),
    Mutation('normal', mutation_probabilities[1], dimension_probabilitise[1], standard_deviation=1.8),
    Mutation('normal', mutation_probabilities[2], dimension_probabilitise[2], standard_deviation=1.8),
    Mutation('normal', mutation_probabilities[3], dimension_probabilitise[3], standard_deviation=1.6),
    Mutation('normal', mutation_probabilities[4], dimension_probabilitise[4], standard_deviation=1.6),
    Mutation('normal', mutation_probabilities[5], dimension_probabilitise[5], standard_deviation=2.0),
    Mutation('normal', mutation_probabilities[6], dimension_probabilitise[6], standard_deviation=2.0),
    Mutation('random', mutation_probabilities[7], dimension_probabilitise[7], mutation_strength=0.1),
    Mutation('normal', mutation_probabilities[8], dimension_probabilitise[8], standard_deviation=1.5),
]

columns = ['best individual', 'best fitness', 'rounds', 'time', 'configuration', 'function', 'dimension']

df = pd.DataFrame(None, None)
fit_hist_df = pd.DataFrame(None, None)

print()

for function, system_size in functions[22:]:
    print(f'Testing {function.__name__} with dimension {system_size}')
    fitness = Fitness(lambda x: -function(x), system_size, diversity_control_strat='None', threshold=0.5)
    for config_id in range(len(mutation_probabilities)):
        print(f'Currently on config_id={config_id}')
        ga_config = GA(fitness, selections[config_id], crossovers[config_id], replacements[config_id], mutations[config_id])
        #print(f'Testing {function.__name__} with system_size = {system_size}')
        best_individuals, best_fitness_values, total_rounds, times, fitness_history = ga_config.run(number_of_creatures, interval_min, interval_max, rounds, run_times=run_times, early_stopping_rounds=early_stopping_rounds)
        #print(f'Stored minimum is {stored_minimums(function, system_size)}')
        #print('###########################')

        df = pd.concat([df,
                        pd.DataFrame(list(zip(best_individuals, best_fitness_values, total_rounds, times, ['config_' + str(config_id)] * len(times), [function.__name__] * len(times), [system_size] * len(times))),
                                     columns=columns)], ignore_index=True)
        fit_hist_df = pd.concat([fit_hist_df,
                                 pd.DataFrame(list(zip_longest(*fitness_history, fillvalue=None)), columns=[f'config_{config_id} {function.__name__}_{system_size} run_{i}' for i in range(run_times)])],axis=1)


# name = 'test'
# df.to_csv(name)
# fit_hist_df.to_csv(name+' fit hist')