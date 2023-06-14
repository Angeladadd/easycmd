import os

def main():
    cur_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(cur_path, 'easycmd'), 'w') as file:
        file.write(f"""
        #!/bin/bash

        python3 {cur_path}/easycmd.py -s {cur_path} "$@"
        """)



if __name__ == '__main__':
    main()