#!/bin/bash

# Absolute path to the directory of this script
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

app_list=$(awk '/# Apps Start/{flag=1;next}/# Apps End/{flag=0}flag' "$DIR/sandbox.yml" | awk '!/#/' | awk -F',|:' '/role/ {print $2}' | tr -d ' ' | grep -v -E "(settings|sanity_check)" | sort -u | tr '\n' ',' | sed 's/,$//')
folder_list=$(ls "$DIR/roles" | grep -v -E "(settings|sanity_check)" | tr '\n' ',' | sed 's/,$//')
missing_app=$(comm -23 <(echo $app_list | tr ',' '\n' | sort) <(echo $folder_list | tr ',' '\n' | sort))
missing_folder=$(comm -13 <(echo $app_list | tr ',' '\n' | sort) <(echo $folder_list | tr ',' '\n' | sort))

if [[ -n $missing_app || -n $missing_folder ]]; then
  echo -e "In app list, not in folder list:\n$missing_app\n\nIn folder list, not in app list:\n$missing_folder" >&2
  exit 1
fi
