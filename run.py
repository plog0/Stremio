from fastapi import FastAPI
from mediaflow_proxy.main import app as mediaflow_app  # Import mediaflow app

main_app = FastAPI()

# Add a simple health endpoint
@main_app.get("/api/health")
async def health():
    return {"status": "ok"}

# Manually add only non-static routes from mediaflow_app
for route in mediaflow_app.routes:
    if route.path != "/":  # Exclude the static file path
        main_app.router.routes.append(route)

# Run the main app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(main_app, host="0.0.0.0", port=7860)
