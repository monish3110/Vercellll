from vercel.workers import subscribe, get_asgi_app
@subscribe("payments")
def process(payload, metadata):
    print("PWNED! PAYLOAD EXECUTED:", payload)
    return True
app = get_asgi_app()
