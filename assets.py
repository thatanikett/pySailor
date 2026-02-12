import os
import tkinter

class AssetManager:
    def __init__(self):
        # Find the absolute path to the directory this file is in
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.cache = {}

    def get_image(self, filename, folder="resources"):
        
        #Searches for an image in a specific sub-folder.
        #Example: manager.get_image("rocket.png", "resources/emojis")
        #and also prepares cache of paths for future use
        
        if filename in self.cache:
            return self.cache[filename]

        # Build the path dynamically
        path = os.path.join(self.root_dir, folder, filename)

        if not os.path.exists(path):
            print(f"Error: Could not find {path}")
            return None

        # Load and store in cache to prevent garbage collection
        img = tkinter.PhotoImage(file=path)
        self.cache[filename] = img
        return img