def check_haiku(commit_message):
        return True

def update_poetry(file_path, isHaiku):
    with open(file_path, "a") as file:
        if isHaiku :
            file.write("Haiku")
        else:
            file.write("Not haiku")
        
