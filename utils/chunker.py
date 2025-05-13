from pypdf import PdfReader

def chunk_pdf(file_path, chunk_size=500, overlap=50):
    reader = PdfReader(file_path)
    full_text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
    words = full_text.split()

    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks