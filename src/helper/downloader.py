import requests
from pathlib import Path

# Helper Function to Download file in the local Directory 
def download_to_local(url:str, out_path:Path,parent_mkdir:bool=True):
    if not isinstance(out_path,Path):
        raise ValueError(f"{out_path} must me valid pathlib. Path Object")
    if parent_mkdir:
        out_path.parent.mkdir(parents=True,exist_ok=True)

    try:
        response = requests.get(url)
        response.raise_for_status()
        #Write the file out in binary mode to prevent any newline conversions
        out_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f"failed to download {url}:{e}")
        return False
