import os
import requests
#from crewai_tools import tool
from crewai.tools import BaseTool,tool

@tool
def github_downloader(repo_url: str, save_directory: str) -> str:
    """
    Downloads a GitHub repository as a zip file from the given URL.

    Args:
        repo_url (str): The URL of the GitHub repository.
        save_directory (str): The directory where the repository will be saved.

    Returns:
        str: The path to the downloaded zip file.
    """
    try:
        # Validate and construct the download URL
        if not repo_url.endswith("/"):
            repo_url += "/"
        zip_url = f"{repo_url}archive/refs/heads/main.zip"
        
        # Prepare download path
        response = requests.get(zip_url, stream=True)
        response.raise_for_status()  # Raise an error for bad HTTP status
        
        # Ensure save directory exists
        os.makedirs(save_directory, exist_ok=True)
        file_path = os.path.join(save_directory, f"{repo_url.split('/')[-1]}-main.zip")
        
        # Save the file
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return f"Repository downloaded successfully to {file_path}"
    
    except Exception as e:
        return f"Failed to download repository: {str(e)}"
