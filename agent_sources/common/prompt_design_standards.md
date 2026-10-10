**Good Prompt Design:**
```markdown
# ✅ GOOD: Modular, precise boundaries, concrete negative constraints, and explicit exit conditions
- **Tone Directive**: Ban conversational fillers (e.g. "Sure!", "Certainly!").
- **Fail-Safe Loop Breaking**: Limit error-fixing loops to a maximum of 5 attempts.
- **Scope Restriction**: Only touch configuration files in `/configs/`.
```

**Bad Prompt Design:**
```markdown
# ❌ BAD: Vague, conversational, missing exit rules, and open-ended directives
You are a very helpful assistant. Try your best to write good code and make sure you clean up files when you are done. Feel free to explain your thoughts to the user.
```
