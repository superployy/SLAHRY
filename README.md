# MUSIC-V1 Discord Bot

A Discord music bot supporting YouTube, Spotify, SoundCloud, and Bandcamp.

## Railway Deployment

### 1. Push to GitHub
```bash
git add .
git commit -m "Initial commit"
git push
```

### 2. Create Railway project
- Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub Repo
- Select your repository

### 3. Set Environment Variables in Railway
Go to your service → Variables tab and add:

| Variable | Description |
|---|---|
| `BOT_TOKEN` | Your Discord bot token |
| `SPOTIFY_ID` | Spotify Client ID (optional) |
| `SPOTIFY_SECRET` | Spotify Client Secret (optional) |
| `BOT_PREFIX` | Command prefix (default: `$`) |

### 4. Enable Required Bot Intents
In the [Discord Developer Portal](https://discord.com/developers/applications):
- Go to your app → Bot tab
- Enable: **Message Content Intent**, **Server Members Intent**, **Presence Intent**

### 5. Invite Bot
Use this URL (replace CLIENT_ID):
```
https://discord.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot&permissions=3165184
```

## Commands

| Command | Aliases | Description |
|---|---|---|
| `$play <song>` | `$p`, `$yt` | Play a song or URL |
| `$skip` | `$s` | Skip current song |
| `$pause` | — | Pause playback |
| `$resume` | — | Resume playback |
| `$stop` | `$st` | Stop and clear queue |
| `$queue` | `$q` | Show queue |
| `$loop` | `$l` | Toggle loop |
| `$shuffle` | `$sh` | Shuffle queue |
| `$prev` | `$back` | Play previous song |
| `$volume <0-100>` | `$vol` | Set volume |
| `$songinfo` | `$np` | Now playing info |
| `$history` | — | Song history |
| `$connect` | `$c` | Connect to voice channel |
| `$disconnect` | `$dc` | Disconnect from voice |

## Local Development
```bash
pip install -r requirements.txt
# Create a .env or export variables:
export BOT_TOKEN="your_token_here"
python run.py
```
