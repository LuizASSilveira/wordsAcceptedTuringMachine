#!/usr/bin/python
# -*- coding: utf-8 -*-

from turing_machine import turing_machine # representa a turing machine
from tape import Tape # representa uma unidade de fita
import sys


def getLine(arquivo):
    fp = open(arquivo, "r") #abre em modo de leitura o arquivo com a definicao da maquina de turing
    lines_cmd = fp.readlines()
    lines = []
    for line in lines_cmd:
        lines.append(line.rstrip())
    return lines, lines[0].split()

def work(lines,fitas) :
    
    number_of_lines  = len(lines)
    '''valores de entrada que representam a turing machine de entrada'''
    input_alphabet   = lines[0].split()
    tape_alphabet    = lines[1]
    whitespace       = lines[2]
    states           = lines[3].split()
    initial_state    = lines[4]
    final_states     = lines[5].split()
    number_of_tapes  = lines[6]
    transitions      = []
    
    '''laco que pegara as transicoes'''
    for i in range(7, number_of_lines):
        transitions.append(lines[i].split())

    tape_list = [] #lista de fitas
    number_of_args = int(number_of_tapes) #+2
    '''laco de repeticao que construira a lista de fitas'''
    for i in range(0, number_of_args): #2
        if len(fitas) >= i : # caso tenha simbolos, ele coloca na fita
            tape_list.append(Tape(whitespace, tape_alphabet, list(fitas[i])))
        else: # caso nao tenha, coloca simbolos que representam o branco
            tape_list.append(Tape(whitespace,tape_alphabet,[whitespace]))

    '''Instancia a turing machine'''
    tm = turing_machine(states, final_states, initial_state, transitions, whitespace, tape_list)

    '''executa a turing machine'''
    result = tm.run()
    if result[0] == 1:
        return True
    # else:
        # print("Rejeitou")
    # print(result[1])

if __name__ == "__main__":
    
    lines,input_alphabet = getLine(sys.argv[1]) #Abre arquivo txt
    alphabetLower = []

    for ia in input_alphabet:
        if(ia.islower() and ia != '#'):
            alphabetLower.append(ia)
            
    
    alphabetLower.insert(0,' ')
    saidas = []
    num = 0
    tam = len(alphabetLower)
    for a in range(tam):
        for b in range(tam):
            for c in range(tam):
                for d in range(tam):
                    for e in range(tam):
                        for f in range(tam):
                            for g in range(tam):
                                for h in range(tam):
                                    for i in range(tam):
                                        for x in range(1,tam):
                                            word=[''.join(alphabetLower[a] + alphabetLower[b] + alphabetLower[c] + alphabetLower[d] + alphabetLower[e] +  alphabetLower[f] +  alphabetLower[g] +  alphabetLower[h] +  alphabetLower[i] +  alphabetLower[x]).replace(' ','')]
                                            if(work(lines,word) and not word in saidas):
                                                saidas.append(word)
                                                num += 1 
                                                print(num,'->',word[0])
                                                  

