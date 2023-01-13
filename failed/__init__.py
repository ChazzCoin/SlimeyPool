from F import OS

failed_DIRECTORY = OS.get_cwd()
failed_FILE = lambda fileName: f"{failed_DIRECTORY}/{fileName}"
failed_DIRECTORY = f"{failed_DIRECTORY}/failed"