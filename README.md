# SublimeTabSnippets
Fix annoying SublimeText issue with TAB inserting completion and not desired snippet

This simple SublimeText module will make sure TAB will insert the matching snippet (based on snippet's tab trigger) or TAB (\t) if no snippet matches. Other completions can be inserted with ENTER while autocomplete panel is visible.

I'm using it with the following SublimeText options:

```json
"auto_complete_commit_on_tab": false,
"tab_completion": false
```

