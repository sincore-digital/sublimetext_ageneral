# https://www.sublimetext.com/docs/3/api_reference.html
# https://stackoverflow.com/questions/12814731/how-do-i-get-the-current-caret-position

import sublime
import sublime_plugin

"""
	Cria os placeholders
	"""
class CsscommentCommand(sublime_plugin.TextCommand):
	"""
		Executa o plugin
		"""
	def run(self, edit):
		for pos in self.view.sel():
			self.view.insert(edit, pos.begin(), "\t========================================================================== */\n")
			self.view.insert(edit, pos.begin(), "\t\n")
			self.view.insert(edit, pos.begin(), "/*\n")

		#self.view.sel().add(pos.begin())
		self.view.run_command("move", {"by": "lines", "forward": False, "extend": False})
		self.view.run_command("move", {"by": "lines", "forward": False, "extend": False})
		self.view.run_command("move_to", {"to": "eol"})
			
