
import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك في بوت تحليل السوق 📈\n\n"
        "أرسل EURUSD لتحليل اليورو والدولار\n"
        "أرسل XAUUSD لتحليل الذهب\n\n"
        "التوقعات احتمالية وليست مضمونة."
    )

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    symbol = update.message.text.strip().upper()

    pairs = {
        "EURUSD": "EUR/USD",
        "XAUUSD": "XAU/USD",
    }

    if symbol not in pairs:
        await update.message.reply_text(
            "أرسل EURUSD لليورو/الدولار أو XAUUSD للذهب."
        )
        return

    await update.message.reply_text(
        f"طلب التحليل: {pairs[symbol]}\n"
        "لم نربط مصدر الأسعار بعد، لذلك لا يوجد توقع مباشر حاليًا.\n"
        "سنضيف بيانات السوق في الخطوة التالية."
    )

def main():
    if not TOKEN:
        raise RuntimeError("أضف TELEGRAM_BOT_TOKEN في متغيرات البيئة.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analyze))
    app.run_polling()

if __name__ == "__main__":
    main()
  
