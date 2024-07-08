import os
import re

def create_directories(directory_structure_file):
  """
  構造記法で書かれたディレクトリリストを読み込み、ディレクトリと.gitignoreを生成します。

  Args:
    directory_structure_file: ディレクトリ構造が記述されたファイルのパス。
  """

  with open(directory_structure_file, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

  root_dir = lines[0].strip()
  parent_dirs = [root_dir]  # 親ディレクトリのスタック

  for line in lines[1:]:
    depth = line.count('    ') + line.count('│   ') + line.count('├──') + line.count('└──')
    line = line.strip()
    dir_name = line.strip('│├───└ ').replace('\\', '/')

    # 親ディレクトリのスタックを更新
    while len(parent_dirs) > depth:
      parent_dirs.pop()
    
    # ディレクトリを作成
    dir_path = os.path.join(parent_dirs[-1], dir_name)
    os.makedirs(dir_path, exist_ok=True)

    # .gitignoreを作成
    with open(os.path.join(dir_path, ".gitignore"), "w", encoding="utf-8") as g:
      g.write("")

    # 親ディレクトリのスタックを更新
    parent_dirs.append(dir_path)

# directory_structure.txtを読み込み、ディレクトリと.gitignoreを生成
create_directories(os.path.join(os.path.dirname(__file__), "directory_structure.txt"))