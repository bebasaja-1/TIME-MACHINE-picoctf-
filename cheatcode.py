#!/usr/bin/env python3
import sys
import os
import re
import subprocess
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def cari_flag():
    try:
        subprocess.run(['unzip', 'challenge.zip'])
        print('(+) extract selesai')
        
        if os.path.exists('drop-in'):
            os.chdir('drop-in')
            print('(+) masuk ke directory drop-in')
            
            if os.path.exists('.git'):
                os.chdir('.git')
                print('(+) masuk ke directory .git')
                
                # Jalankan git log -p dan cari flag
                try:
                    process = subprocess.Popen(['git', 'log', '-p'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors='ignore')
                    out, err = process.communicate()
                    
                    if out:
                        flags = re.findall(r'picoCTF\{.*?\}', out)
                        print(flags)
                        for flag in flags:
                            print(f'(+) FOUND FLAG: {flag}')
                    else:
                        print('(!) git log tidak menghasilkan output / terjadi error')
                        print(err)
                except Exception as e:
                    print(f'(!) Error running git: {e}')
                    
            else:
                print('(!) directory .git tidak ditemukan dalam drop-in')
        else:
            print('(!) directory drop-in tidak ditemukan')
            
    except Exception as e:
        print(f'(+) error extract: {e}')


def download(url, s):
    r = s.get(url, verify=False)
    filename = url.split('/')[-1]
    if not filename:
        filename = "challenge.zip"
    
    with open(filename, 'wb') as f:
        f.write(r.content)
    print(f'(+) download selesai: {filename}')
    
def main():
    if len(sys.argv) != 2:
        print('(+) link zip nya %s <url> ' % sys.argv[0])
        sys.exit(1)

    url = sys.argv[1]
    s = requests.Session()
    print('(+) mulai')
    download(url, s)
    cari_flag()

if __name__ == "__main__":
    main()