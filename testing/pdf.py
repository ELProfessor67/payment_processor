import pdfkit

# directly from url
pdfkit.from_url("https://google.com", "google.pdf", verbose=True)
print("="*50)