from fastapi import Security, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.config import CONFIG

# Define the security scheme
security = HTTPBearer(auto_error=False)

# Token verification logic
def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid authorization header",
        )
    
    token = credentials.credentials
    if token != CONFIG.API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )
