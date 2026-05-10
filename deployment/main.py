import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), 'env', '.env')
load_dotenv(env_path)

if __name__ == "__main__":
    uvicorn.run("app/main:app", host="0.0.0.0", port=8000
                ,log_level=int(os.getenv('LOG_LEVEL', '20'))
                #,reload=True
                )
