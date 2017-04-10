test = {
  'name': 'Pieces',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> starter.get_piece(-1, -1, board) == None
          True
          >>> starter.get_piece(N, N, board) == None
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
          >>> starter.place_piece('*', -1, -1, board)
          False
          >>> starter.place_piece('*', N, N, board)
          False
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
          >>> to_place = '0'
          >>> for y in range(N):
          ...    for x in range(N):
          ...        starter.place_piece(to_place, x, y, board);
          ...        if to_place != starter.get_piece(x, y, board):
          ...          raise AssertionError("Placed a piece at {} {} but did not get same piece back".format(x, y))
          ...        to_place = chr(ord(to_place) + 1)
          >>> # The board needs to be full after placing these pieces
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
          >>> # Checks against data abstraction violations
          >>> starter.place_piece('7', 7, 7, board)
          True
          >>> starter.get_piece(7, 7, board) == None
          False
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import starter_2048 as starter
      >>> import utils
      >>> board = utils.make_board(10)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
