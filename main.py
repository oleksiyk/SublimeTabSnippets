import sublime, sublime_plugin

from threading import Timer

class HideAutocompleteAndInsertSnippetCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("hide_auto_complete")
		t = Timer(0.01, self.view.run_command, ["insert_best_completion"])
		t.start()
