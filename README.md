# Discord Bot Automation

This repository contains a simple Discord bot that automatically runs Discord commands once per day using GitHub Actions.

## How It Works

1. The bot sends a sequence of commands to a Discord channel once every 24 hours.
2. GitHub Actions runs the script automatically at midnight UTC daily.
3. Your Discord authentication token is stored securely as a GitHub Secret.
4. The commands are sent in sequence with a 5-second delay between each one.

## Setup Instructions

1. Fork or clone this repository to your GitHub account.

2. Add your Discord token as a repository secret:

   - Go to your repository on GitHub
   - Click on "Settings" > "Secrets and variables" > "Actions"
   - Click "New repository secret"
   - Set the name as `DISCORD_TOKEN`
   - Paste your Discord authentication token as the value
   - Click "Add secret"

3. That's it! The workflow will now run automatically at midnight UTC every day.

## Manual Trigger

You can also manually trigger the workflow anytime:

- Go to the "Actions" tab in your repository
- Select the "Daily Discord Commands" workflow
- Click "Run workflow"

## Security Notes

- Your Discord token is stored securely as a GitHub Secret and is never exposed in logs or code.
- Never commit files containing your token directly to the repository.

## Customization

To modify the commands or timing:

- Edit `bot.py` to change the commands or the delay between them
- Modify `.github/workflows/daily.yml` to adjust the schedule (using cron syntax)

## Command Sequence

The current command sequence is:

1. ,work
2. ,crime
3. ,collect
4. ,dep all

Each command is sent with a 5-second delay between them.
