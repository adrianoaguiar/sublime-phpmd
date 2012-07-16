import sublime, sublime_plugin, subprocess

# Run phpcs, used in other commands
def runPhpmd(path):
    command = "phpmd \"" + path + "\" text codesize,unusedcode,design"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    stdOut = process.communicate()[0]
    returnCode = process.returncode
    return stdOut

# Get the output view
def getOutputView():
    window = sublime.active_window()
    view = window.new_file()
    view.set_name('PHPMD Results')
    view.set_scratch(True)
    return view

# Send to an output view
def sendToView(view, text):
    edit = view.begin_edit()
    view.replace(edit, sublime.Region(0, view.size()), text)
    view.sel().clear()
    view.end_edit(edit)

# Check if a file is PHP
def isPhpFile(path):
    return path.endswith(".php")

# Run phpcs as a window command from a hotkey
class PhpmdCommand(sublime_plugin.WindowCommand):
    def run(self):
        path = self.window.active_view().file_name()
        if not path:
            sublime.error_message("You need to save the file before running phpmd")
            return
        elif isPhpFile(path):
            result = runPhpmd(path)
            if result:
                view = getOutputView()
                sendToView(view, result)

# Run phpcs from the sidebar
class PhpmdSidebarCommand(sublime_plugin.WindowCommand):
    def run(self, paths):
        result = ""
        for path in paths:
            if isPhpFile(path):
                result = result + runPhpmd(path)
        if result:
            view = getOutputView()
            sendToView(view, result)
