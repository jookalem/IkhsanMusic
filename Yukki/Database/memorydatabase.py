

import config
from Yukki.core.mongo import mongodb


autoenddb = mongodb.autoend


# Shifting to memory [ mongo sucks often]
autoend = {}

# Auto End Stream


async def is_autoend() -> bool:
    chat_id = 123
    mode = autoend.get(chat_id)
    if not mode:
        user = await autoenddb.find_one({"chat_id": chat_id})
        if not user:
            autoend[chat_id] = False
            return False
        autoend[chat_id] = True
        return True
    return mode


async def autoend_on():
    chat_id = 123
    autoend[chat_id] = True
    user = await autoenddb.find_one({"chat_id": chat_id})
    if not user:
        return await autoenddb.insert_one({"chat_id": chat_id})


async def autoend_off():
    chat_id = 123
    autoend[chat_id] = False
    user = await autoenddb.find_one({"chat_id": chat_id})
    if user:
        return await autoenddb.delete_one({"chat_id": chat_id})

# Active Voice Chats
async def get_active_chats() -> list:
    return active


async def is_active_chat(chat_id: int) -> bool:
    if chat_id not in active:
        return False
    else:
        return True


async def add_active_chat(chat_id: int):
    if chat_id not in active:
        active.append(chat_id)


async def remove_active_chat(chat_id: int):
    if chat_id in active:
        active.remove(chat_id)
