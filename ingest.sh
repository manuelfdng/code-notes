#!/bin/bash

gitingest . \
  -e "**/*.pyc" \
  -e "**/*.pyo" \
  -e "**/__pycache__/**" \
  -e "**/.pytest_cache/**" \
  -e "**/venv/**" \
  -e "**/node_modules/**" \
  -e "**/.git/**" \
  -e "**/dist/**" \
  -e "**/build/**" \
  -e "**/.DS_Store" \
  -e "**/*.log" \
  -i "**/*.py" \
  -i "**/*.js" \
  -i "**/*.jsx" \
  -i "**/*.ts" \
  -i "**/*.tsx" \
  -i "**/*.html" \
  -i "**/*.css" \
  -i "**/*.json" \
  -i "**/*.md" \
  -i "**/*.yml" \
  -i "**/*.toml"