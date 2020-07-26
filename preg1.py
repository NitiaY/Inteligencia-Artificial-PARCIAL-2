# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:12:30 2020

@author: Usuario
"""
import array
import random
import pandas as pd
import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

heart =pd.read_csv('heartN.csv')
x=numpy.array(heart['trestbps'])
y=numpy.array(heart['chol'])
z=numpy.array(heart['oldpeak'])
#print(x)

IND_SIZE =10
creator.create("FitnessMin", base.Fitness, weights=(1.0,))
creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("indices", random.sample, range(IND_SIZE), IND_SIZE)

toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalTSP(individual):
    distance =0
    for i in range(IND_SIZE):
        distance += x[individual[i]]+y[individual[i]]+z[individual[i]]
       #print(distance)
    return distance,


toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.02)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evalTSP)

def main():
    random.seed(169)

    pop = toolbox.population(n=10)

    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    algorithms.eaSimple(pop, toolbox, 0.5, 0.2, 20, stats=stats, 
                        halloffame=hof)
    
    return pop, stats, hof

if __name__ == "__main__":
    pop,stats,hof=main()
    #print(hof)
    #print(evalTSP(hof[0]))