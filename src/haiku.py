def update_poetry():
    file_name = "poetry.md"
    file_path = file_name.replace("/github/workspace/", "")
    with open(file_path, "a") as file:
        file.write("First haiku")