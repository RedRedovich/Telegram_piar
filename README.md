# Telegram Piar

![welcome](https://user-images.githubusercontent.com/125751648/226340280-48917970-8992-44c0-ba8f-776351edea9e.gif)


> demo

| Information      | Returns          | 
| ------------- |:-------------:|
| ``` author ``` |[Redpiar](https://t.me/Redpiar)|
| ``` telegram ``` |[Channel](https://t.me/BotesForTelegram)|
| ``` version ``` |1.0.0| 
| ``` CopyRight ``` |[Redpiar](https://t.me/Redpiar)|

| functions      | Added          | 
| ------------- |:-------------:|
| ``` Piar_LS ``` |✔|
| ```Piar_Group ``` |✔| 
| ```information ``` |✔|

> **instruction**:

1. download archive from github

2. go to the files folder and open the accounts.txt file

3. fill in the accounts.txt file, example:

```{api_id} {api_hash} {number1} {number2} {number3} [...]```

![Снимок](https://user-images.githubusercontent.com/125751648/226343770-4366a25b-ea6f-4309-b072-a2cf1075880c.PNG)

notation:

**to get api_id and api_hash go to the site** [my.telegram.org](https://my.telegram.org/auth)

4. after that, go to the LS_chat.txt file and add people to whom we will send ads
  
  ```or you can use the get_users.py script```
  
  ![Снимок](https://user-images.githubusercontent.com/125751648/226350458-b146a462-55e5-4c8a-876e-b95c95e606e9.PNG)


5. then you can fill in the group.txt file, I think it’s not so difficult to find groups in Google

![Снимок](https://user-images.githubusercontent.com/125751648/226350975-6c6d9861-d5fd-402f-b7c8-1247338633f2.PNG)

6. next you have to write a PR message for mailing in message.txt file
7. if you want to change the name of the files, then first change the name of these files in settings.py
8. if you want to change the delay between sending SMS, go to the settings.py file and change the variable time_sleep = 1
9. run main.py and check the work
