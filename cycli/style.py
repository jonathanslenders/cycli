import re

from pygments.lexer import RegexLexer
from pygments.token import Comment, Operator, Keyword, Name, String, Number, Token
from prompt_toolkit.styles import Style


class CypherLexer(RegexLexer):
  name = 'Cypher'
  aliases = ['cypher']
  filenames = ['*.cyp', '*.cypher']

  flags = re.IGNORECASE

  tokens = {
    'root': [
      (r'//.*?\n', Comment.Single),
      (r'\b(abs|acos|all|allShortestPaths|AND|any|AS|ASC|ASCENDING|asin|ASSERT|atan|atan2|avg'
       r'|BY'
       r'|CASE|ceil|coalesce|collect|COMMIT|CONSTRAINT|CONTAINS|cos|cot|count|CREATE|CYPHER'
       r'|degrees|DELETE|DESC|DESCENDING|DETACH|DISTINCT|DROP'
       r'|e|ELSE|END|endNode|ENDS|exists|exp|EXPLAIN|extract'
       r'|FALSE|FIELDTERMINATOR|filter|floor|FOREACH|FROM'
       r'|has|haversin|head|HEADERS'
       r'|id|ILIKE|IN|INDEX|IS'
       r'|keys'
       r'|labels|last|left|length|LIKE|LIMIT|LOAD CSV|log|log10|lower|ltrim'
       r'|MATCH|max|MERGE|min'
       r'|node|nodes|none|NOT|NULL'
       r'|ON|OPTIONAL|OR|ORDER'
       r'|percentileCont|percentileDisc|PERIODIC|pi|PROFILE'
       r'|radians|rand|range|reduce|rel|relationship|relationships|REMOVE|replace|RETURN|reverse|right|round|rtrim'
       r'|SCAN|SET|shortestPath|sign|sin|single|size|SKIP|split|sqrt|START|startNode|STARTS|stdev|stdevp|str|substring|sum'
       r'|tail|tan|THEN|timestamp|toFloat|toInt|trim|TRUE|type'
       r'|UNION|UNIQUE|UNWIND|USING|upper'
       r'|WHEN|WHERE|WITH'
       r'|XOR)\b', Keyword),
      (r'[+*/<>=~!@#%^&|`?-]', Operator),
      (r'quit|exit|help|refresh|run-[0-9]+|save-csv|schema-[a-z]+|schema|env|export', Number),
      (r'[0-9]+', Name),
      (r'[a-zA-Z_][a-zA-Z0-9_]*', Name),
      (r"'(''|[^'])*'", String.Single),
      (r'"(""|[^"])*"', String.Symbol),
      (r'[\]\)]-[\(\[]|[\]\)]->\(|\)<-[\[\(]|[\)\]]-->\(|\)<--[\(\[]|[\)\]]--[\(\[]', Token.Pattern),
      (r'\.', Token.Pattern),
      (r'\(|\)|\]|\[|{|}', Token.Pattern),
    ]
  }


cypher_style = Style.from_dict({
    'pygments.keyword': '#3498db',
    'pygments.literal.string': '#e67e22',
    'pygments.name': '#1abc9c',
    'pygments.pattern': '#e74c3c',
    'pygments.literal.number': '#bf5fff',

    'line': 'bg:#000000 #ffffff',

    'linenumber': 'bg:#ffffaa #000000',
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar': 'bg:#00aaaa',
    'scrollbar.button': 'bg:#003333',

    'completion-toolbar': 'bg:#888800 #000000',
    'completion-toolbar.arrow': 'bg:#888800 #000000',
    'completion-toolbar.completion': 'bg:#aaaa00 #000000',
    'completion-toolbar.completion.current': 'bg:#ffffaa #000000 bold',

    'afterinput': 'bg:#ff44ff #000000'
})
