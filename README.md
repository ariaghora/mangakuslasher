Mangaku Slasher:
================

Mangaku Slasher
---------------

Skrip python untuk download manga dari mangaku.web.id. Skrip ini membutuhkan pustaka BeautifulSoup. 

Penggunaan
----------
1. Install BeautifulSoup

		pip install BeautifulSoup

2. Jalankan skrip 
	- Untuk download satu episode gunakan paramenter -s (--single) diikuti link episode:

			python mangakuslasher.py -s http://mangaku.web.id/bloody-monday-chapter-01-part-a/

	- Untuk download seluruh episode gunakan parameter -a (--all) diikuti link manga:
	
			python mangakuslasher.py -a http://mangaku.web.id/bloody-monday-manga/
