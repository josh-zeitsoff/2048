test = {
  'name': 'Swipe',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'Keeps track of whether swiping left actually did anything or not.',
          'choices': [
            'Keeps track of whether swiping left actually did anything or not.',
            'Gets the piece at a given x and y position on the board.',
            'Places a piece at a given x and y position on the board.',
            'Checks if, at the end of the turn, the game has been lost.'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does the function swipe_left do?'
        },
        {
          'answer': 'If a piece was moved or not.',
          'choices': [
            'If a piece was moved or not.',
            'If this function was called or not.',
            'If a piece was placed on the board.',
            'Nothing.'
          ],
          'hidden': False,
          'locked': False,
          'question': "'What does the variable action_taken represent?'"
        },
        {
          'answer': 'The number of squares along one side of the board.',
          'choices': [
            'The number of squares along one side of the board.',
            'If the game has ended or not.',
            'Nothing, since we never assign it to anything.',
            'Number of total squares on the board.'
          ],
          'hidden': False,
          'locked': False,
          'question': "'What does the variable N represent?'"
        },
        {
          'answer': 'Iteration through each column and row of the board.',
          'choices': [
            'Iteration through each column and row of the board.',
            'Iteration only through each column of the board.',
            'Iteration only through each row of the board.',
            'Nothing.'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does the "for y in range(N) and for x in range(N) represent"?'
        },
        {
          'answer': 'They are an adjacent pair of pieces.',
          'choices': [
            'They are an adjacent pair of pieces.',
            'They are 2 squares on the board.',
            'They are 2 random pieces on the board.',
            'There is no relationship between them.'
          ],
          'hidden': False,
          'locked': False,
          'question': "'What are piece_at_xy and left_adjacent?'"
        },
        {
          'answer': 'I cannot move an empty piece, so just move on.',
          'choices': [
            'I cannot move an empty piece, so just move on.',
            'I can move an empty piece, so I move it.',
            'I place a new piece at the location of piece_at_xy.',
            'Nothing.'
          ],
          'hidden': False,
          'locked': False,
          'question': "What happens if the piece_at_xy is an '*'?"
        },
        {
          'answer': 'I continue since I cannot do anything if the left_adjacent piece is off the edge of the board.',
          'choices': [
            'I continue since I cannot do anything if the left_adjacent piece is off the edge of the board.',
            'I can swap a piece with None, so I swap piece_at_xy and left_adjacent.',
            'I place a new piece at the location of left_adjacent.',
            'Nothing.'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What happens if left_adjacent is None?'
        },
        {
          'answer': 'It is moved to the left and action_taken is set to True.',
          'choices': [
            'It is moved to the left and action_taken is set to True.',
            'It is moved to the left and action_taken is set to False.',
            'It is not moved to the left and action taken is set to True.',
            'Nothing.'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What happens if I can move a piece left?'
        },
        {
          'answer': 'We end our move.',
          'choices': [
            'We end our move.',
            'We keep going.',
            'action_taken is never True.',
            'Nothing.'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What happens if action_taken is True"?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
