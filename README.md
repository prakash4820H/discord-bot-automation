# Discord Bot Automation

This repository contains a simple Discord bot that automatically runs Discord commands using GitHub Actions.

## How It Works

1. The bot sends a sequence of commands to a Discord channel.
2. GitHub Actions is configured to run the script at 3:15 PM IST (9:45 AM UTC) daily.
3. Your Discord authentication token is stored securely as a GitHub Secret.
4. The commands are sent in sequence with a 5-second delay between each one.

## Important Note About GitHub Actions Scheduling

GitHub Actions scheduled workflows sometimes experience delays due to how GitHub's shared runners work. If the workflow doesn't run exactly at 3:15 PM IST, this is normal and expected behavior. From GitHub's documentation and community reports:

- Scheduled workflows can be delayed by 3 to 60+ minutes depending on GitHub's server load
- There's no guarantee that a workflow will run at the exact scheduled time
- This is a known limitation of GitHub's free runners

## Solutions

1. **Manual Trigger**: You can manually trigger the workflow anytime from the Actions tab.
2. **Multiple Triggers**: The workflow is now also set to run when changes are made to the bot.py file.

## Setup Instructions

1. Fork or clone this repository to your GitHub account.

2. Add your Discord token as a repository secret:

   - Go to your repository on GitHub
   - Click on "Settings" > "Secrets and variables" > "Actions"
   - Click "New repository secret"
   - Set the name as `DISCORD_TOKEN`
   - Paste your Discord authentication token as the value
   - Click "Add secret"

3. The workflow will run automatically based on the schedule (with possible delays).

## Manual Trigger

You can manually trigger the workflow anytime:

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
