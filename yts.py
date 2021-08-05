#Licenced under MIT License
#charset = "utf-8"
#Language = "Python3"
#Bot Framework = "python-telegram-bot"
#The Code is without Proxy, Actual code contains Proxy
#Proxy should be used is of the type SOCKS5
#Special thanks to cyberboySumanjay
#The bot will work till you press ctrl+c in the terminal or command line.,

#import the required files
import requests
import logging
from telegram import *
from telegram.ext import *

#enable logger (optional)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = "Your Token Here"

#CommandHandler for message "Start"
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"""*Hi {update.effective_chat.first_name},* 
Welcome to the Torrent Searcher Bot. Here you will find all the torrents you search for :)
Type /help to know how to use the bot
Type /info to know about the developer""", parse_mode=ParseMode.MARKDOWN)

#CommandHandler for message "Help"
def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""Send me the query you want to search and i will do the rest!
If any error occurs, feel free to pm me on https://t.me/unkusr""", parse_mode=ParseMode.MARKDOWN)


#CommandHandler to get torrents for the query
def find(update: Update, context: CallbackContext) -> None:
    try:
        update.message.reply_text("Searching results for 👉{}👈".format(update.message.text))
        #yts api
        url = "https://api-tor.herokuapp.com/yts/{}".format(update.message.text)
        results = requests.get(url).json()
        print(results)
        for item in results:
            name = item.get('Name')
            up = item.get('ReleasedDate')
            gen = item.get('Genre')
            rat = item.get('Rating')
            time = item.get('Runtime')
            img = item.get('Poster')
            lnk1 = item.get('Dwnload1')
            lnk2 = item.get('Download2')
            lnk3 = item.get('Download3')
            update.message.reply_text(f"""*➲Name:* `{name}`
Released on {up}
Watch Time {time}
*Genre:* {gen}
*Rating:* {rat}
*Poster:* {img}
*Link1:* `{lnk3}`
*Link2:* `{lnk1}`
*Link3:* `{lnk2}`""", parse_mode=ParseMode.MARKDOWN)
        update.message.reply_text("End of Results")
    except:
        update.message.reply_text("""Search Completed""")

#CommandHnadler for message "info"
def info(update: Update, context: CallbackContext) -> None:
    #Never Mind :-)
    update.message.reply_text("""Bot by @unkusr""", parse_mode=ParseMode.MARKDOWN)

#Add all handlers to the main function.
def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), find))
    updater.start_polling() #set bot to polling, if you use webhooks, replace this statement with the url of webhook.,
    updater.idle()

#Call the main function
if __name__ == '__main__':
    main()
