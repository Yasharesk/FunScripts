# FunScripts
Different kind of mostly useless (as in very specific use cases) but fun scripts.

**Coins**:

*Includes coins_price.py:*

​	Used for getting the updated prices for a provided list of cryptocurrencies and uploading the results into a google sheet where the list of purchased crypto coins/tokens is stored. 

​	TODO: Add the structure of the google sheet. 

------

**Clean Film Names:**
برای مرتب کردن اسم فیلم هایی که به صورت فایل دانلود شده اند. اسم سایت ها، مشخصات کیفیت، زیرنویس و مانند آن ها را حذف کنیم و فقط نام فیلم و سال ساخت باقی بماند. 

------

**Wordle**:

*Includes wordle.py:*

Used for cheating at wordle. It gives you suggestions based on highest probablity of letters being included. Use one the suggested words, then give the word and answer back.
Give the answers as five letters:
<ul>
<li>"g" for Green</li>
<li>"y" for Yellow</li>
<li>"m" for grey (Miss)</li>
</ul>
Use one of the words from new suggested list. Repeat until either you win or run out of moves. 

* *wordle_classbased.py:*

    Same as worlde.py, only desinged with class. 

* *wordle_api.py:*

    An API for serving the worlde_classbased.py using FastAPI.

    Endpoints:

        /newgame: Resets the words list and starts a new game.

        /playround: Recieves a played word and response for it and returns updated list of words. 

	
	