test = {
  'name': 'End_move',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> starter.end_move(board);
          >>> utils.made_move(board)
          True
          >>> utils.num_pieces(board) == 1
          True
          >>> starter.end_move(board);
          >>> utils.made_move(board)
          True
          >>> utils.num_pieces(board) == 2
          True
          >>> starter.end_move(board);
          >>> utils.made_move(board)
          True
          >>> utils.num_pieces(board) == 3
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
    }
  ]
}
