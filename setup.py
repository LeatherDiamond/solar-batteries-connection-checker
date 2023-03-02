import cx_Freeze

executables = [cx_Freeze.Executable("solar_batteries_connection_checker.py", base="Win32GUI")]

cx_Freeze.setup(
    name = "ping_ips",
    options = {"build_exe": {"packages":["os","smtplib","datetime","concurrent.futures","PySimpleGUI"],"include_files":["ips.txt"]}},
    version = "0.1",
    description = "Pings a list of IP addresses and sends an email if any are not responding",
    executables = executables
)
