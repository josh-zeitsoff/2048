test = {
  'name': 'Lost',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> starter.have_lost(board)
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
          >>> starter.place_piece('0', 0, 0, board);
          >>> starter.have_lost(board)
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
          >>> board = utils.make_board(2);
          ... starter.place_piece('0', 0, 0, board);
          ... starter.place_piece('0', 1, 0, board);
          ... starter.place_piece('0', 0, 1, board);
          ... starter.place_piece('0', 1, 1, board);
          >>> starter.have_lost(board)
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
          >>> board = utils.make_board(2);
          ... starter.place_piece('1', 0, 0, board);
          ... starter.place_piece('0', 1, 0, board);
          ... starter.place_piece('0', 0, 1, board);
          ... starter.place_piece('1', 1, 1, board);
          >>> starter.have_lost(board)
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
      >>> board = utils.make_board(10)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
