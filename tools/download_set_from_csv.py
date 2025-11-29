import re, os, requests, time
import tkinter.filedialog

csv = tkinter.filedialog.askopenfile(
    filetypes=(("Google Sheets CSV", "*.csv"),)
).read()

pattern = r'https?://[^\s,]+'
links = re.findall(pattern, csv)
print(f"found {len(links)} links")

outdir = tkinter.filedialog.askdirectory()
os.makedirs(outdir, exist_ok=True)

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0",
})

def download(url, dest):
    for attempt in range(10):   # retry up to 10 times
        try:
            r = session.get(url, timeout=20, stream=True)
            if r.status_code == 200:
                with open(dest, "wb") as f:
                    for chunk in r.iter_content(8192):
                        f.write(chunk)
                return True
            else:
                print("status", r.status_code, "retrying...")
        except Exception as e:
            print("err:", e, "retrying...")

        time.sleep(1.5)  # cooldown so catbox doesn’t ban you

    print("FAILED:", url)
    return False


for idx, url in enumerate(links, start=1):
    num = f"{idx:03d}"
    ext = url.rsplit(".", 1)[-1]
    filename = f"{num}.{ext}"
    path = os.path.join(outdir, filename)

    print("downloading", filename)
    download(url, path)

print("done!")
