
## CS 101 Problem Solving & Programming
## Program 2
## Christopher J. Neeley
## Date created: Feb 8, 2015
## Date due: Feb 14, 2015
## PROBLEM:
##      Create a simulation of airline luggage.
##
## SOLUTION:
##      1. Create loop for repeating the instance
##      2. Ask for number of trials
##      3. Ask for detailed output
##      4. Loop through number of trials
##         a. Loop each destination jump
##         b. Add to detailed output
##      5. Display detailed output
##      6. Display end results
##      7. Ask to run again
##################################################################################
# Import randint from random
from random import randint
# Import sys for exit and version, import inspect for terminal/console/shell checking
import sys
import inspect


# Set colors for terminal/console
# 0 = basic color, 1 = error color, 2 = help color, 3 = output color
colorama = ['\033[30m', '\033[31m', '\033[32m', '\033[36m', '\033[34m']

# Set location instances; chance %, location name, location number
directionalLandings = [[[3, 'LVS', 1], [6, 'SEA', 2], [9, 'HNL', 3]], [[2, 'MCI', 0],
  [7, 'SEA', 2], [9, 'HNL', 3]], [[0, 'MCI', 0], [6, 'LVS', 1], [9, 'HNL', 3]]]

# Set all variables
planeHopCount = 0

pythonVersion2     = False
continueTrials     = True
currentlyTraveling = True

# Check Python version for print change
# Primarily used for testing purposes
if int(sys.version[0]) == 2:
  pythonVersion2 = True

# Check to see if run with terminal/console/shell
# Reset text in colorama so they are not displayed in shell
if len(inspect.stack()) > 1:
  colorama[0] = ''
  colorama[1] = ''
  colorama[2] = ''
  colorama[3] = ''
  print('''\nI see you're not using the command line.
That's unfortunate, you just won't see the colors then.\n''')

# Return current location, exit if we're lost at sea
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

# Print out the version name and tell difference
def displayVersion():
  print(colorama[3] + '\nThe version of Python you are using is ' + sys.version[:5])
  print('''This program supports Python 2.X and 3.X
The only difference is the print methods, so no need to worry.
''' + colorama[0])

# Print out the help information
def helpMe():
  print('')
  print(colorama[2] + 'Help Information'.center(100, ' '))
  print('This is a airline luggage simulater.'.center(100, ' '))
  print('You enter a number of trials to run, the number must be greater than 0.'.center(100, ' '))
  print('You will then be asked if you wish to see the output details, this accepts; y, yes, n, no.'.center(100, ' '))
  print('The output details will be each hop that happened in a trial.'.center(100, ' '))
  print('It will then display the percent of successful trials, those trials that are two or less hops.'.center(100,
    ' '))
  print('V Other inputs that are accepted V'.center(100, ' '))
  print("'v' or 'version' will display your current Pythong version.".center(100, ' '))
  print("'h' or 'help' will display the help information.".center(100, ' '))
  print("'q' or 'quit' will exit the program.".center(100, ' ') + colorama[0])
  print('')

# Check other accepted inputs
def checkOtherInput(inputText):
  # Display help information
  if inputText == 'h' or inputText == 'help':
    helpMe()
    return None
  # Display version information
  elif inputText == 'v' or inputText == 'version':
    displayVersion()
    return None
  # Quit program
  elif inputText == 'q' or inputText == 'quit':
    # Goodbye
    print('Goodbye')
    sys.exit(0)
  # Return if none of the above
  else:
    return False

# Input checking for non intergers then no accepted answers
def isItEnglish(inputText, intOrstr):
  otherInput = checkOtherInput(inputText)
  # Integer based only
  if intOrstr == 1:
    # Check to see if answer is a integer
    try:
      int(inputText)
      inputText = int(inputText)
      if inputText > 0:
        # Return if the number is greater than 0
        return inputText
      else:
        # Return False to run again and display problem
        print(colorama[1] + 'You must enter a value greater than 0.' + colorama[0])
        return False
    # Catch error
    except ValueError:
      inputText = inputText.lower()
      # Return False to run again and display problem
      if otherInput == False:
        print(colorama[1] + 'You must enter a value greater than 0.' + colorama[0])
        return False
      else:
        return otherInput
  # String based
  elif intOrstr == 2:
    inputText = inputText.lower()
    # Return True to accept show text/continue
    if inputText == 'y' or inputText == 'yes':
      return True
    # Return False to not show text/quit
    elif inputText == 'n' or inputText == 'no':
      return False
    # Return None to run again and display accepted outputs
    elif otherInput == False:
      print(colorama[1] + 'You must enter Y, YES, N, NO, H, Help, V, VERSION, Q, OR QUIT.' + colorama[0])
      return None
    else:
      return otherInput

# Begin running Trials
while continueTrials:

  # Set and reset variables
  loopAmount     = None
  showOutputText = None
  maxNumberOfHops = 0
  successfulHops  = 0
  startingCount   = 1

  # Loop for input on the number of trials to run
  while loopAmount == None or loopAmount == False:
    # Switch based on Python version
    if pythonVersion2:
      loopAmount = isItEnglish(raw_input('How many rounds do you want to run lost luggage? ' + colorama[4]), 1)
    else:
      loopAmount = isItEnglish(input('How many rounds do you want to run lost luggage? ' + colorama[4]), 1)

  # Reset color
  print(colorama[0])
  # Set loopAmount to integer
  loopAmount = int(loopAmount)

  # Loop for input to display details or not
  while showOutputText == None:
    # Switch based on Python version
    if pythonVersion2:
      showOutputText = isItEnglish(raw_input('Do you want to output details? ' + colorama[4]), 2)
    else:
      showOutputText = isItEnglish(input('Do you want to output details? ' + colorama[4]), 2)

  # Reset color
  print(colorama[0])
  # Display details if wanted
  if showOutputText:
    print(colorama[3] + '\nTrials' + colorama[0] + '\n')

  # Begin loop through each trial
  while startingCount <= loopAmount:
    # Set and reset variables in loop
    trialLogger = colorama[3] + 'Trial ' + str(startingCount) + colorama[0] + '   MCI'
    currentlyTraveling = True
    currentLocation = 0
    planeHopCount   = 0

    # Loop through single trial instance
    while currentlyTraveling:
      # Get random number of 0 to 9
      newLocation = randint(0, 9)
      # Check if number is less than or equal to the next location and set next location
      if newLocation <= directionalLandings[currentLocation][0][0]:
        currentLocation = directionalLandings[currentLocation][0][2]
      elif newLocation <= directionalLandings[currentLocation][1][0]:
        currentLocation = directionalLandings[currentLocation][1][2]
      elif newLocation <= directionalLandings[currentLocation][2][0]:
        currentLocation = directionalLandings[currentLocation][2][2]
      else:
        # Exit if we're unable to locate the luggage, aliens must of stolen it, not our problem, walk away
        print(colorama[1] + 'We are terribly sorry, but it appears that your' +
         'luggage has been sent to Mars. Have a nice day.' + colorama[0])
        sys.exit(0)

      # Keep a count on the number of times the luggage jumps
      planeHopCount += 1

      # Add details if asked to
      if showOutputText:
        trialLogger = trialLogger + '-> ' + getLocation(currentLocation)

      # Quit loop if at destination
      if currentLocation == 3:
        currentlyTraveling = False
        # Check if luggage was on time
        if planeHopCount <= 2:
          successfulHops += 1
        # Check if time was longest
        if planeHopCount > maxNumberOfHops:
          maxNumberOfHops = planeHopCount

    # Add to trial count
    startingCount += 1

    # Display details if asked to
    if showOutputText:
      print(trialLogger)

  if showOutputText:
    print('') # For better readability print out

  # Print trial runs success rate and max hops.
  print('''The baggage was on time %0.2f%% of the time. (%0.f / %0.f)
The max hops that occured was %0.f.\n''' % ((float(successfulHops) / float(loopAmount) * 100),
    successfulHops, loopAmount, maxNumberOfHops))

  # Reset continueTrials for rerun
  continueTrials = None

  # Ask if they wish to run again
  while continueTrials == None:
    # Switch based on Python version
    if pythonVersion2:
      continueTrials = isItEnglish(raw_input('Do you want to run again? ' + colorama[4]), 2)
    else:
      continueTrials = isItEnglish(input('Do you want to run again? ' + colorama[4]), 2)

    # Reset color
    print(colorama[0])

# Goodbye
print('Goodbye')
