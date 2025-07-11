# handlers.py
from aiogram import Router, types, F, Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

router = Router()

def register_handlers(dp):
    dp.include_router(router)

# دالة التحقق من الاشتراك
async def check_user_subscription(user_id, bot: Bot):
    channel_username = "@V_i_V_52"
    try:
        member = await bot.get_chat_member(chat_id=channel_username, user_id=user_id)
        return member.status in ("member", "administrator", "creator")
    except:
        return False

@router.message(Command("start"))
async def start_command(msg: types.Message, bot: Bot):
    user_id = msg.from_user.id
    is_subscribed = await check_user_subscription(user_id, bot)

    if is_subscribed:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🖼 تصفح التصاميم", callback_data="browse")],
            [InlineKeyboardButton(text="📝 طلب تصميم", callback_data="request")],
            [InlineKeyboardButton(text="📞 تواصل معنا", url="https://t.me/V_i_V_52")]
        ])
        await msg.answer("🎨 أهلاً بك في <b>بوت الواقدي للتصاميم</b>\nاختر من القائمة:", reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📢 اشترك في القناة", url="https://t.me/V_i_V_52")],
            [InlineKeyboardButton(text="✅ تحقق من الاشتراك", callback_data="check_sub")]
        ])
        await msg.answer("⚠️ يجب الاشتراك في قناة الواقدي لاستخدام البوت.\n\n📢 بعد الاشتراك اضغط تحقق من الاشتراك.", reply_markup=keyboard)

@router.callback_query(F.data == "check_sub")
async def check_subscription(callback: types.CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    is_subscribed = await check_user_subscription(user_id, bot)

    if is_subscribed:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🖼 تصفح التصاميم", callback_data="browse")],
            [InlineKeyboardButton(text="📝 طلب تصميم", callback_data="request")],
            [InlineKeyboardButton(text="📞 تواصل معنا", url="https://t.me/V_i_V_52")]
        ])
        await callback.message.edit_text("✅ تم التحقق من اشتراكك.\nاختر من القائمة:", reply_markup=keyboard)
    else:
        await callback.message.answer("❌ لم يتم الاشتراك بعد.\nيرجى الاشتراك ثم الضغط على تحقق من الاشتراك.")

@router.callback_query(F.data == "browse")
async def browse_designs(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo="https://via.placeholder.com/600x400.png?text=تصميم+1",
        caption="🖌 تصميم بوستر رمضان\nالسعر: مجاني\nاضغط لطلبه",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🛒 اطلب هذا التصميم", callback_data="request")]
        ])
    )

@router.callback_query(F.data == "request")
async def request_design(callback: types.CallbackQuery):
    await callback.message.answer("✍️ أرسل لنا تفاصيل التصميم الذي تريده (النوع + المحتوى + الألوان)...")
