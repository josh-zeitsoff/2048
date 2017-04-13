test = {
  'name': 'Random',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> for j in range(N**2):
          ...     starter.place_random(board);
          >>> utils.board_full(board)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import starter_2048 as starter
      >>> import utils
      >>> N = 4
      >>> board = utils.make_board(N)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> empty, two, four, eight = 0, 0, 0, 0;
          ... for row in board:
          ...     for piece in row:
          ...          if piece == '*':    empty += 1;
          ...          elif piece == '2':  two += 1;
          ...          elif piece == '4':  four += 1;
          ...          elif piece == '8':  eight += 1;
          ...          else:
          ...               continue;
          >>> empty == 0
          True
          >>> two > four > eight
          True
          >>> 75 >= two >= 45
          True
          >>> 50 >= four >= 25
          True
          >>> 10 >= eight >= 1
          True
          >>> two + four + eight == 100
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import starter_2048 as starter
      >>> import utils
      >>> N = 10
      >>> board = utils.make_board(N)
      >>> while not utils.board_full(board):
      ...   starter.place_random(board);
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
