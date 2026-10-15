from fastapi import FastAPI

app = FastAPI(
    title="Shopify Razorpay Subscription API",
    description="Custom subscription management backend",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Shopify Razorpay Subscription API is running",
        "environment": "local",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}