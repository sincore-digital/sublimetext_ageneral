# https://www.sublimetext.com/docs/3/api_reference.html

import sublime
import sublime_plugin

"""
	Cria os placeholders
	"""
class PlaceholderCommand(sublime_plugin.TextCommand):
	"""
		Executa o plugin
		"""
	def run(self, edit):
		# Verifica se é um arquivo CSS
		if self.view.settings().get("syntax").find("CSS.sublime-syntax"):
			# Recupera o seletor CSS
			selector = self.view.substr((self.view.sel())[0])

			# Cria o view.settings().get("syntax")
			placeholder_str = selector + "::-webkit-input-placeholder {}\n"
			placeholder_str += selector + ":-moz-placeholder {}\n"
			placeholder_str += selector + "::-moz-placeholder {}\n"
			placeholder_str += selector + ":-ms-input-placeholder {}\n"
			placeholder_str += selector + "::-ms-input-placeholder {}\n"

			content = (self.view.sel())[0]
			self.view.replace(edit, content, placeholder_str)
