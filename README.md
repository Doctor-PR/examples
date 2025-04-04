Doctor PR is your AI-powered code review assistant that automatically addresses review feedback with code changes.

## 🚀 What Doctor PR Does

![workflow](https://github.com/user-attachments/assets/c3c99537-345b-4c3a-ab73-cd6b3a78b3f9)

1. When a review is submitted, an "Address with Doctor PR" button gets added
2. Click the button to tell Doctor PR to address the review
3. Doctor PR creates a new PR with the fixes
4. Review the changes and merge into to your branch if you're happy with them

## 🔥 Why You'll Love It

- **Save time**: Stop context-switching between reviews and fixing issues
- **Learn faster**: See how AI solves the problems in your code
- **Ship quicker**: Address review feedback without delay
- **Privacy first**: Your code never leaves GitHub's servers

## 🛠️ Quick Start

![setup](https://github.com/user-attachments/assets/d5323d83-72d8-47a2-baa7-81ac43c4fb73)

1. Install the [Doctor PR GitHub App](https://github.com/apps/doctor-pr)
2. Enable GitHub Actions permissions:
   - Go to `Settings -> Actions -> General -> Workflow permissions`
   - Check `Read and write permissions`
   - Check `Allow GitHub Actions to create and approve pull requests`
3. Add your API key:
   - Go to `Settings -> Secrets and variables -> Actions -> New repository secret`
   - Add `ANTHROPIC_API_KEY` (get one [here](https://console.anthropic.com/settings/keys))
4. Create a workflow file at `.github/workflows/doctor-pr.yml`:

```yaml
name: Doctor PR
on:
  workflow_dispatch:
    inputs:
      action_input:
        required: true
        type: string
jobs:
  doctor-pr:
    runs-on: ubuntu-latest
    steps:
      - name: Doctor PR
        uses: Doctor-PR/action@latest
        with:
          action_input: ${{inputs.action_input}}
          anthropic_api_key: ${{secrets.ANTHROPIC_API_KEY}}
```

## 🔒 Security

Your code stays secure because:
- Doctor PR runs entirely in GitHub Actions
- Your code never leaves GitHub's servers
- We use open-source components ([Aider](https://github.com/Aider-AI/aider))
- All AI processing uses Anthropic's Claude (via your own API key)

## 💬 Questions?

Have questions or feedback? [Open an issue](https://github.com/Doctor-PR/action/issues) or reach out to us at [support@drpr.app](mailto:support@drpr.app).
