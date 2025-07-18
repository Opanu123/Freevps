import os
import sys
import dropbox

ACCESS_TOKEN = os.getenv("DROPBOX_TOKEN")
dbx = dropbox.Dropbox(ACCESS_TOKEN)

def upload(local_path, remote_path):
    with open(local_path, "rb") as f:
        dbx.files_upload(f.read(), remote_path, mode=dropbox.files.WriteMode.overwrite)
        print(f"Uploaded {local_path} to {remote_path}")

def download(remote_path, local_path):
    with open(local_path, "wb") as f:
        metadata, res = dbx.files_download(path=remote_path)
        f.write(res.content)
        print(f"Downloaded {remote_path} to {local_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: dropbox_helper.py [upload|download] local_path remote_path")
        sys.exit(1)
    cmd, local, remote = sys.argv[1], sys.argv[2], sys.argv[3]
    if cmd == "upload":
        upload(local, remote)
    elif cmd == "download":
        download(remote, local)
    else:
        print("Invalid command")
