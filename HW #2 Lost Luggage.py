from random import randint
import sys
import inspect

directionalLandings = [[[3, 'LVS', 1], [6, 'SEA', 2], [9,'HNL', 3]], [[2, 'MCI', 0],
  [7, 'SEA', 2], [9, 'HNL', 3]], [[0, 'MCI', 0], [6, 'LVS', 1], [9, 'HNL', 3]]]

numberOfRounds  = 0
startingCount   = 1
planeHopCount   = 0
successfulHops  = 0
currentLocation = 0
maxNumberOfHops = 0
trialLogger = ''

loopAmount         = None
showOutputText     = None
continueTrials     = True
currentlyTraveling = True

# 0 = basic color, 1 = error color, 2 = help color, 3 = output color
colorama = ['\033[30m', '\033[31m', '\033[32m', '\033[36m']

if len(inspect.stack()) > 1:
  colorama[0] = ''
  colorama[1] = ''
  colorama[2] = ''
  colorama[3] = ''

def getLocation(currentLocation):
  if currentLocation == 0:
    return 'MCI'
  elif currentLocation == 1:
    return 'LVS'
  elif currentLocation == 2:
    return 'SEA'
  elif currentLocation == 3:
    return 'HNL'
  else:
    print(colorama[1] + 'We lost her captain...' + colorama[0])
    sys.exit(0)

def helpMe():
  print(colorama[2] + 'Help menu!' + colorama[0])

def isItEnglish(inputText, intOrstr):
  if intOrstr == 1:
    try:
      int(inputText)
      inputText = int(inputText)
      if inputText > 0:
        return inputText
      else:
        print(colorama[1] + 'You must enter a value greater than 0.' + colorama[0])
        return False
    except ValueError:
      if inputText == 'h' or inputText == 'help':
        helpMe()
      else:
        print(colorama[1] + 'You must enter a value greater than 0.' + colorama[0])
        return False
  elif intOrstr == 2:
    inputText = inputText.lower()
    if inputText == 'y' or inputText == 'yes':
      return True
    elif inputText == 'n' or inputText == 'no':
      return False
    elif inputText == 'h' or inputText == 'help':
      helpMe()
      return None
    else:
      print(colorama[1] + 'You must enter Y, Yes, N or NO.' + colorama[0])
      return None

while continueTrials:

  loopAmount     = None
  showOutputText = None
  currentLocation = 0
  maxNumberOfHops = 0
  startingCount   = 1

  while loopAmount == None or loopAmount == False:
    loopAmount = isItEnglish(input('How many rounds do you want to run lost luggage? '), 1)

  loopAmount = int(loopAmount)

  while showOutputText == None:
    showOutputText = isItEnglish(input('Do you want to output details? '), 2)

  if showOutputText:
    print(colorama[3] + 'Trials' + colorama[0] + '\n')

  while startingCount <= loopAmount:
    trialLogger = colorama[3] + 'Trial ' + str(startingCount) + colorama[0] + '   MCI'
    currentLocation = 0
    currentlyTraveling = True
    planeHopCount = 0
    while currentlyTraveling:
      newLocation = randint(0, 9)
      if newLocation <= directionalLandings[currentLocation][0][0]:
        currentLocation = directionalLandings[currentLocation][0][2]
      elif newLocation <= directionalLandings[currentLocation][1][0]:
        currentLocation = directionalLandings[currentLocation][1][2]
      elif newLocation <= directionalLandings[currentLocation][2][0]:
        currentLocation = directionalLandings[currentLocation][2][2]
      else:
        print(colorama[1] + 'We are terribly sorry, but it appears that your' +
         'luggage has been sent to Mars. Have a nice day.' + colorama[0])
        sys.exit(0)

      planeHopCount += 1

      if showOutputText:
        trialLogger = trialLogger + '-> ' + getLocation(currentLocation)

      if currentLocation == 3:
        currentlyTraveling = False
        if planeHopCount <= 2:
          successfulHops += 1
        elif planeHopCount > maxNumberOfHops:
          maxNumberOfHops = planeHopCount

    startingCount += 1

    if showOutputText:
      print(trialLogger)

  print("""\nThe baggage was on time %0.3f%% of the time. (%0.f / %0.f)
  The max hops that occured was %0.f""" % ((float(successfulHops) / float(loopAmount) * 100),
    successfulHops, loopAmount, maxNumberOfHops))

  continueTrials = None

  while continueTrials == None:
    continueTrials = isItEnglish(input('Do you want to run again? '), 2)
