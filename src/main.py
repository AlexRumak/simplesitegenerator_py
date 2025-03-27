import argparse
import os
import yaml
import markdown
from schema import Schema, And, Use, Optional, SchemaError

schema = Schema(
  {
    "blog": {
      "folder": And(str, len),
    }, 
    "about": {
      "path": And(str, len),
    },
    "homepage": {
      "path": And(str, len),
    }
  }
)

def get_config():
  parser = argparse.ArgumentParser(description="Simple Site Generator")
  parser.add_argument('config', type=str, help='Path to the site.yml file')
  args = parser.parse_args()

  config_path = args.config

  if not os.path.isfile(config_path):
    print(f"Error: {config_path} is not a valid file path.")
    exit(1)
  
  with open(config_path) as stream:
    data = yaml.safe_load(stream)
    validated = schema.validate(data)

    validated["basePath"] = os.path.dirname(config_path)
    return validated
  
def get_blog_files(base_path, blog_folder):
  filePaths = []
  targetDir = "{0}/{1}".format(base_path, blog_folder)
  for dir in os.walk(targetDir):
    for file in dir[2]:
      dirPath = dir[0]
      if dirPath.endswith("/"):
        dirPath = dirPath[:-1]
      filePaths.append("{0}/{1}".format(dirPath, file))
  return filePaths

def main():
  config = get_config()

  base_path = config["basePath"]
  blog_folder = config["blog"]["folder"]
  
  print("Searching {0}/{1} for files...".format(base_path, blog_folder))

  blog_paths = get_blog_files(base_path, blog_folder)

  for blog in blog_paths:
    with open(blog) as file:
      content = file.read()
      html = markdown.markdown(content)
      print(html)
      input("Press Enter to continue...")
  

if __name__ == "__main__":
    main()
