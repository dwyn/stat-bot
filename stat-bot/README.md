# Running the Discord Bot Locally

This guide provides instructions on how to run your Discord bot written in Python on your local machine.

## **Prerequisites**

- Python installed on your machine.
- `pip` (Python package installer).

## **Steps**

### **1. Install Required Libraries**

Install the necessary Python libraries using `pip`:

\```bash
pip install disnake
\```

### **2. Set Up Environment Variables**

The bot uses environment variables to retrieve the Discord token and guild name. You can set these using a `.env` file or directly in your shell.

#### **a. Using a `.env` file**

1. Create a `.env` file in the same directory as your bot script.
2. Add your Discord bot token and guild name:

\```plaintext
DISCORD_TOKEN=your_discord_token
DISCORD_GUILD=your_discord_guild_name
\```

3. Install the `python-dotenv` library:

\```bash
pip install python-dotenv
\```

4. In your bot script, load the environment variables:

\```python
from dotenv import load_dotenv
load_dotenv()
\```

#### **b. Using Shell**

Set the environment variables in your shell:

\```bash
export DISCORD_TOKEN=your_discord_token
export DISCORD_GUILD=your_discord_guild_name
\```

### **3. Run the Bot**

Navigate to your bot script's directory and run:

\```bash
python your_bot_script_name.py
\```

Replace `your_bot_script_name.py` with the name of your bot script.

### **4. Verify the Bot's Status**

After executing the script, you should see a message indicating the bot's login status. The bot will now be online in your Discord server, and you can interact with it.

> **Note**: Ensure the bot is invited to your Discord server and has the required permissions to read and send messages in the channels you're testing.
