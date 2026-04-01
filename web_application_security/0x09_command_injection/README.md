# Command Injection and Bash Scripting Project

## Layihə Haqqında
Bu layihə Command Injection (Əmr İnjeksiyası) boşluqlarının necə işlədiyini, Bash xüsusi dəyişənlərini və sistemlərin bu cür hücumlardan necə qorunmalı olduğunu öyrənmək üçün hazırlanmışdır. Layihə çərçivəsində Bash skriptlərinin yazılması və təhlükəsizlik konseptlərinin dərindən başa düşülməsi hədəflənir.

## Öyrənmə Məqsədləri
Bu layihənin sonunda aşağıdakı suallara cavab verə bilmək hədəflənir:
* **Command Injection nədir?** Tətbiqin istifadəçidən aldığı məlumatı birbaşa sistem əmri kimi icra etməsi nəticəsində yaranan boşluqdur.
* **Payload-lar:** Hücum zamanı istifadə olunan `;`, `&&`, `||`, `|` kimi operatorlar və onların funksiyaları.
* **Bash Xüsusi Dəyişənləri:** `$0`, `$1`, `$#`, `$@`, `$$` və s. kimi dəyişənlərin skript daxilində rolu.
* **IFS (Internal Field Separator):** Bash-da sözləri bir-birindən ayırmaq üçün istifadə olunan simvolun (default olaraq boşluq) manipulyasiyası.
* **Qorunma Yolları:** Giriş məlumatlarının filtrasiyası (input validation) və təhlükəli funksiyalardan qaçınmaq.

## Tələblər
* Bütün skriptlər **Kali Linux** mühitində test edilmişdir.
* Skriptlər tam olaraq **2 sətirdən** ibarətdir.
* IP diapazonu üçün mövqe dəyişəni olan `$1` istifadə olunur.
* Hər bir fayl yeni sətir (`\n`) ilə bitməlidir.

## Mövzuların İzahı

### 1. Əmr Ayırıcıları
* `&&`: Yalnız birinci əmr uğurla bitdikdə ikincini işlədir.
* `;`: Birincinin nəticəsindən asılı olmayaraq bütün əmrləri ardıcıl işlədir.

### 2. IFS Manipulyasiyası
Hücumçular boşluq simvolunun qadağan olunduğu yerlərdə `$IFS` dəyişənindən istifadə edərək filtrləri keçə bilərlər. Məsələn: `cat$IFS/etc/passwd`.

### 3. Bash Mövqe Dəyişənləri
* `$0`: Skriptin adı.
* `$1`: Skriptə ötürülən birinci arqument (bu layihədə IP diapazonu).
* `$#`: Ötürülən arqumentlərin sayı.

## İstifadə Olunan Alətlər
* **Vi / Vim / Emacs:** Skriptlərin redaktəsi üçün.
* **Interactsh / Burp Suite:** Şəbəkə sorğularını izləmək və test etmək üçün.
* **Bash:** Skriptlərin icra mühiti.

## Təhlükəsizlik Xəbərdarlığı
Bu layihədə öyrənilən metodlar yalnız təhsil və etik kiber təhlükəsizlik testləri (Penetration Testing) üçün nəzərdə tutulub. İcazəsiz sistemlərə müdaxilə qanunsuz və qeyri-etikdir.
