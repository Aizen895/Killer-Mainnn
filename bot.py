import asyncio
import os
from pyrogram import Client

# Constants for client creation
api_id = 28713982
api_hash = "237e15f7c006b10b4fa7c46fee7a5377"
bot_token = "7251295977:AAEFULfhETjhwwK4O7o_JPqYJlGMDcYHkhs"


async def create_client(client_name):
    """
    Create a new Pyrogram client session.
    """
    try:
        session_name = f"{client_name}_session"
        client = Client(session_name, api_id=api_id, api_hash=api_hash, bot_token=bot_token)
        await client.start()
        print(f"Client '{client_name}' created and started.")
        
        bot_user = await client.get_me()
        bot_username = bot_user.username
        print(f"The bot's username is: @{bot_username}")
        
        return client
    except Exception as e:
        print(f"An error occurred while creating the client: {e}")
        return None


async def delete_client(client_name, client):
    """
    Stop and delete a Pyrogram client session.
    """
    try:
        if client:
            await client.stop()
            print(f"Client '{client_name}' stopped.")
        session_file = f"{client_name}_session.session"
        if os.path.exists(session_file):
            os.remove(session_file)
            print(f"Session file for '{client_name}' deleted.")
    except Exception as e:
        print(f"An error occurred while deleting the client: {e}")


async def main():
    """
    Continuously create and delete client sessions in a loop.
    """
    counter = 1
    while True:
        client_name = f"client_{counter}"
        
        # Create client
        client = await create_client(client_name)
        
        # Wait for a few seconds
        await asyncio.sleep(1)
        
        # Delete client
        if client:
            await delete_client(client_name, client)
        
        # Increment counter for the next client
        counter += 1


if __name__ == "__main__":
    asyncio.run(main())
