from exceptions import AccessDeniedError, NotFoundError
import requests

def download_file(url, filename="latest.csv"):
    try:
        response = requests.get(url, stream=True)
        
        if response.status_code == 404:
            raise NotFoundError(f"Resource not found at {url}")
        elif response.status_code == 403:
            raise AccessDeniedError(f"Access denied to {url}")

        response.raise_for_status()
        
        with open(filename, 'wb') as handle:
            for chunk in response.iter_content(chunk_size=8192):
                handle.write(chunk)
        
        print(f"File downloaded -> {filename}")
    
    except NotFoundError as e:
        print(f"NotFoundError: {e}")
    except AccessDeniedError as e:
        print(f"AccessDeniedError: {e}")
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {e}")
    except Exception as e:
        print(f"Other error: {e}")
