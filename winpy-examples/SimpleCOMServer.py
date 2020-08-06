# SimpleCOMServer.py

class PythonUtilities:
    _public_methods_ = ['SplitString']
    _reg_progid_ = "PythonDemos.Utilities"

    # NEVER copy the following ID
    # Use print pythoncom.CreateGuid() to create a new one
    _reg_clsid_ = "{1DCE0ACF-7F78-4280-A87C-E3182AE57BBF}"

    # implementation
    def SplitString(self, val, item=None):
        import string
        if item:
            item = str(item)
        return string.split(str(val), item)

# Add code so that when this script is run, it self-registers
if __name__ == '__main__':
    print "Registering COM server..."
    import win32com.server.register
    win32com.server.register.UseCommandLine(PythonUtilities)
