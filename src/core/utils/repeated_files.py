import os
import hashlib
from logger import log
import traceback


repeated: dict = {}
    
    
def hash_file(filename, *args):
    hash = hashlib.md5()

    try:
        with open(filename, 'rb') as file:
            while chunk := file.read(8192):
                hash.update(chunk)
        return hash.hexdigest()
    except (OSError, PermissionError):
        log(f'{__file__} - {traceback.format_exc()}')
    return None
        
    
def delete_repeated(path: str):
    try:
        for root, dirs, files in os.walk(path):
            dirs[:] = [
                d for d in dirs 
                if not d.startswith('.') 
                and d not in ['AppData', 'OpenVPN']
            ]
            for file in files:
                if not file.endswith(('.DAT', '.LOG1', '.LOG2')):
                    full_path = os.path.join(root, file)
                    file_hash = hash_file(full_path)
                
                    if file_hash is None:
                        continue
                    
                    if file_hash in repeated:
                        os.remove(full_path)
                    else:
                        repeated[file_hash] = full_path
    except Exception:
        log(f'{__file__} - {traceback.format_exc()}')


def main(user_name: str):
    user_path = os.path.join(f'C:\\Users\\{user_name}')
    delete_repeated(path=user_path)

        
if __name__ == '__main__':
    main('Emili')

