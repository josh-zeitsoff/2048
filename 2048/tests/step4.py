test = {
  'name': 'End_move',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> utils.clear();
          >>> utils.pause(3.5);
          >>> starter.end_move(board);
          >>> utils.pause(3.5);
          >>> starter.end_move(board);
          >>> utils.pause(4);
          >>> now = time.time();
          >>> starter.end_move(board);
          >>> after = time.time();
          >>> after - now > .2
          True
          >>> utils.clear();

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
