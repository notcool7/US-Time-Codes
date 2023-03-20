import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context("notebook")
data = pd.read_csv('All estimation raw data.csv')

buttonOnTheLeft = data[data.Button == 'L'].Button.count()
buttonOnTheRight = data[data.Button == 'R'].Button.count()
TotalButton = buttonOnTheLeft+buttonOnTheRight
print('There are {} buttons on the left'.format(buttonOnTheLeft))
print('There are {} buttons on the right'.format(buttonOnTheRight))
print('There are {} buttons in total'.format(TotalButton))

print('')

LoseMoney = data[data.Forgone>data.Payoff].Forgone.count()
WinMoney = data[data.Forgone<data.Payoff].Forgone.count()
NeitherWinNorLose = data[data.Forgone==data.Payoff].Forgone.count()
print('There are {} dicisions which payoff is larger than forgone'.format(WinMoney))
print('There are {} dicisions which payoff is smaller than forgone'.format(LoseMoney))
print('There are {} dicisions which payoff is equal to forgone'.format(NeitherWinNorLose))

print('')

Male  = data[data.Gender=='M'].Gender.count()
Female  = data[data.Gender=='F'].Gender.count()
Participants = Male+Female
print('There are {} males in this examination'.format(Male))
print('There are {} females in this examination'.format(Female))
print('There are {} participants in total in this examination'.format(Participants))