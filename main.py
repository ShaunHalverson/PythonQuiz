if __name__ == "__main__":
  questions = [
    "What book holds the record for the fastest selling book in history?",
    "How old was Queen Elizabeth II when she was first crowned the Queen of England?",
    "Which blood type is a universal donor?"
  ]

  answers = [
    "A. The Hunger Games \nB. Harry Potter and the Deathly Hallows \nC. To Kill A Mockingbird",
    "A. 27 \nB. 24 \nC. 31",
    "A. O negative \nB. B Positive \nC. AB"
  ]

  correctAnswers = [1,1,0]
  playerScore = 0

  print("Welcome to the best quiz app ever :)")
  for i in range(len(questions)):
    print("Question #", i+1)
    print(questions[i])
    print(answers[i])

    ### Promt user for answer
    userInput = input("Please answer the question ('A','B','C')> ").upper()

    ### Validate input
    if(userInput == 'A' and correctAnswers[i] == 0):
      playerScore += 1
    elif(userInput == 'B' and correctAnswers[i] == 1):
      playerScore += 1
    elif(userInput == 'C' and correctAnswers[i] == 2):
      playerScore += 1

  print("Quiz Completed :)")
  print("Your score is: {0}/{1}".format(playerScore, len(questions)))
  
