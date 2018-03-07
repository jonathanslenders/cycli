from __future__ import unicode_literals
from prompt_toolkit.key_binding import KeyBindings

key_bindings = KeyBindings()

@key_bindings.add("{")
def curly_left(event):
  b = event.app.current_buffer
  b.insert_text("{")
  b.insert_text("}", move_cursor=False)

@key_bindings.add("}")
def curly_right(event):
  b = event.app.current_buffer
  char = b.document.current_char

  if char == "}":
    b.cursor_right()
  else:
    b.insert_text("}")

@key_bindings.add("(")
def paren_left(event):
  b = event.app.current_buffer
  b.insert_text("(")
  b.insert_text(")", move_cursor=False)

@key_bindings.add(")")
def paren_right(event):
  b = event.app.current_buffer
  char = b.document.current_char

  if char == ")":
    b.cursor_right()
  else:
    b.insert_text(")")

@key_bindings.add("[")
def bracket_left(event):
  b = event.app.current_buffer
  b.insert_text("[")
  b.insert_text("]", move_cursor=False)

@key_bindings.add("]")
def bracket_right(event):
  b = event.app.current_buffer
  char = b.document.current_char

  if char == "]":
    b.cursor_right()
  else:
    b.insert_text("]")

@key_bindings.add("'")
def apostrophe(event):
  b = event.app.current_buffer
  char = b.document.current_char

  if char == "'":
    b.cursor_right()
  else:
    b.insert_text("'")
    b.insert_text("'", move_cursor=False)

@key_bindings.add("\"")
def quote(event):
  b = event.app.current_buffer
  char = b.document.current_char

  if char == "\"":
    b.cursor_right()
  else:
    b.insert_text("\"")
    b.insert_text("\"", move_cursor=False)

@key_bindings.add("`")
def backtick(event):
  b = event.app.current_buffer
  char = b.document.current_char

  if char == "`":
    b.cursor_right()
  else:
    b.insert_text("`")
    b.insert_text("`", move_cursor=False)

@key_bindings.add('backspace')
def backspace(event):
  b = event.app.current_buffer
  current_char = b.document.current_char
  before_char = b.document.char_before_cursor

  patterns = [("(", ")"), ("[", "]"), ("{", "}"), ("'", "'"), ('"', '"'), ("`", "`")]

  for pattern in patterns:
    if before_char == pattern[0] and current_char == pattern[1]:
      b.cursor_right()
      b.delete_before_cursor(2)
      return

  b.delete_before_cursor()
