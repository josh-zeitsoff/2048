test = {
  'name': 'Setup',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Are all of the dependencies installed?
          >>> # Try running: python3 -m pip install getch
          >>> import getch
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Are all of the dependencies installed?
          >>> # Try running: python3 -m pip install termcolor
          >>> import termcolor
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
