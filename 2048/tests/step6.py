test = {
  'name': 'Place',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> starter.swap(board)
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
          >>> starter.place_piece('2', 0, 0, board);
          >>> starter.swap(board)
          False
          >>> starter.place_piece('2', 1, 1, board);
          >>> starter.swap(board)
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
          >>> board = utils.make_board(4);
          >>> starter.place_piece('2', 0, 0, board);
          >>> starter.place_piece('4', 1, 0, board);
          >>> starter.swap(board)
          True
          >>> starter.get_piece(0,0,board)=='4'
          True
          >>> starter.get_piece(1,0,board)=='2'
          True
          >>> starter.get_piece(0,1,board)=='*'
          True
          >>> starter.get_piece(1,1,board)=='*'
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
          >>> board = utils.make_board(4);
          >>> starter.place_piece('2', 0, 0, board);
          >>> starter.place_piece('4', 1, 1, board);
          >>> starter.swap(board)
          True
          >>> starter.get_piece(0,0,board)=='4'
          True
          >>> starter.get_piece(1,1,board)=='2'
          True
          >>> starter.get_piece(0,1,board)=='*'
          True
          >>> starter.get_piece(1,0,board)=='*'
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> board = utils.make_board(4);
          >>> starter.place_piece('2', 0, 0, board);
          >>> starter.place_piece('4', 0, 1, board);
          >>> starter.place_piece('8', 1, 0, board);
          >>> starter.swap(board)
          True
          >>> if starter.get_piece(0,0,board)=='2':
          ...     return starter.get_piece(0,1,board)=='8' and  starter.get_piece(1,0,board)=='4' and  starter.get_piece(1,1,board)=='*'
          True
          >>> if starter.get_piece(0,0,board)=='4':
          ...     return starter.get_piece(0,1,board)=='2' and  starter.get_piece(1,0,board)=='8' and starter.get_piece(1,1,board)=='*'
          True
          >>> if starter.get_piece(0,0,board)=='8':
          ...     return starter.get_piece(0,1,board)=='4' and  starter.get_piece(1,0,board)=='2' and  starter.get_piece(1,1,board)=='*'
          >>>
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
