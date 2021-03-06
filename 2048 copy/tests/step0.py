test = {
  'name': 'Setup',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>>  #Are all of the dependencies installed 
          >>> def test_getch():
          ...     try:
          ...         import getch
          ...     except ImportError:
          ...         os.system("python3 -m pip install getch")
          >>> def test_termcolor():
          ...     try:
          ...         import termcolor
          ...     except ImportError:
          ...         os.system("python3 -m pip install termcolor")
          >>> test_getch()
          >>> test_termcolor()
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import os as os
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
