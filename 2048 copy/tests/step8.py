test = {
  'name': 'Main',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> starter.main()
          >>> assert calls[0] == 'make_board', 'Make sure the first thing you do is create a new 4x4 board.'
          >>> assert calls[1] == 'get_key_press', 'Make sure you are getting the current key pressed.'
          >>> assert calls[2] == 'swipe_up', 'Make sure you have the correct associated key press value for the up arrow, and that you call the correct swipe function.'
          >>> assert calls[3] == 'board_full', 'Make sure you are checking if the game is lost by checking if the board is full.'
          >>> assert calls[5] == 'swipe_down', 'Make sure you have the correct associated key press value for the down arrow, and that you call the correct swipe function.'
          >>> assert calls[8] == 'swipe_right', 'Make sure you have the correct associated key press value for the right arrow, and that you call the correct swipe function.'
          >>> assert calls[11] == 'swipe_left', 'Make sure you have the correct associated key press value for the left arrow, and that you call the correct swipe function.'
          >>> assert calls[14] == 'swap', 'Make sure you have the correct associated key press value for the space bar.'
          >>> assert calls[18] == 'quit', 'Make sure you have the correct associated key press value for the letter q.'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import starter_2048 as starter
      >>> import utils
      >>> index = -1
      >>> calls = []
      >>> def get_key_press():
      ...     global index 
      ...     if index == 5:
      ...        exit()
      ...     calls.append('get_key_press')
      ...     inputs = [65, 66, 67, 68, 32, 113]
      ...     index += 1
      ...     return inputs[index]
      >>> def swipe_up(board):
      ...     calls.append('swipe_up')
      >>> def swipe_down(board):
      ...     calls.append('swipe_down')
      >>> def swipe_right(board):
      ...     calls.append('swipe_right')
      >>> def swipe_left(board):
      ...     calls.append('swipe_left')
      >>> def make_board(N):
      ...     calls.append('make_board')
      >>> def board_full(board):
      ...     calls.append('board_full')
      >>> def swap(board):
      ...     calls.append('swap')
      >>> def print(msg):
      ...     calls.append('print')
      >>> def quit():
      ...     calls.append('quit')
      >>> def end_move(board):
      ...     return 1
      >>> def place_random(board):
      ...     return 1
      >>> def print_board(board):
      ...     return 1
      >>> starter.get_key_press = get_key_press
      >>> starter.swipe_up = swipe_up
      >>> starter.swipe_down = swipe_down
      >>> starter.swipe_right = swipe_right
      >>> starter.swipe_left = swipe_left
      >>> starter.make_board = make_board
      >>> starter.board_full = board_full
      >>> starter.swap = swap
      >>> starter.print = print
      >>> starter.quit = quit
      >>> starter.end_move = end_move
      >>> starter.place_random = place_random
      >>> starter.print_board = print_board
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
