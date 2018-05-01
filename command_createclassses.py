
import sublime
import sublime_plugin
import os, sys

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'libs')

sys.path.append(vendor_dir)

from bs4 import BeautifulSoup

"""
	Cria as classes a partir do html
	"""
class CreateclassesCommand(sublime_plugin.TextCommand):
	"""
		Executa o plugin
		"""
	def run(self, edit):
		# Verifica se é um arquivo HTML
		#if self.view.settings().get("syntax").find("HTML.sublime-syntax") > 0:
		
		#allcontent = sublime.Region(0, self.view.size())
		#print(self.view.substr(allcontent))

		htmldata = self.view.substr((self.view.sel())[0])
		soup = BeautifulSoup(htmldata, "html.parser")
		#print(htmldata)

		css = self.find_childs("", soup)
		print("CSS: \n" + css)

	def find_childs(self, father_css, soup):
		css_str = ""

		#for element in soup.children:
		#	#css_str += father_css + " " + (".".join(element['class'])) + "\n"
		#	print("Element: " + '.'.join(element[0]['class']))

		children = soup.firstChild()
		for child in children:
			print(child)

		return css_str
