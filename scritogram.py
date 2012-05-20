#Scott scttcper@gmail.com
#################################### IMPORTS ###################################

import sublime, sublime_plugin
from datetime import datetime

################################## BASE CLASS ##################################

class ScriptogramCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(
			edit,
			self.view.sel()[0].begin(),
			"---\nTitle: My blog post\nDate: "
			)
		self.view.insert(
			edit,
			self.view.sel()[0].begin(),
			datetime.now().strftime("%Y-%m-%d %H:%M")
			)
		self.view.insert(
			edit,
			self.view.sel()[0].begin(),
			"\n---"
			)

