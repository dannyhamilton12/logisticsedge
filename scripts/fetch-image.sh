#!/bin/bash
# fetch-image.sh — Download a free Unsplash image for an article
# Usage: ./scripts/fetch-image.sh "search terms" "output-filename"
# Example: ./scripts/fetch-image.sh "warehouse logistics uk" "my-article-slug"
#
# Agents should call this when creating new articles.
# It downloads an 800x400 image from Unsplash (free, no API key needed)
# and saves it to public/images/articles/{filename}.jpg
#
# The agent should then add to article frontmatter:
#   image: "/images/articles/{filename}.jpg"

SEARCH_TERMS="${1:?Usage: fetch-image.sh 'search terms' 'output-filename'}"
FILENAME="${2:?Usage: fetch-image.sh 'search terms' 'output-filename'}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="$PROJECT_DIR/public/images/articles"
OUTPUT_FILE="$OUTPUT_DIR/$FILENAME.jpg"

mkdir -p "$OUTPUT_DIR"

# Unsplash source URL (free, no API key, redirects to a relevant photo)
ENCODED_TERMS=$(echo "$SEARCH_TERMS" | sed 's/ /,/g')
URL="https://source.unsplash.com/800x400/?${ENCODED_TERMS}"

echo "Fetching image for: $SEARCH_TERMS"
curl -sL "$URL" -o "$OUTPUT_FILE"

# Verify it's a valid image
FILE_SIZE=$(wc -c < "$OUTPUT_FILE" | tr -d ' ')
if [ "$FILE_SIZE" -lt 1000 ]; then
  echo "WARNING: Downloaded file is too small ($FILE_SIZE bytes), may have failed."
  echo "Falling back to direct Unsplash featured image..."
  # Fallback: use a generic logistics image
  curl -sL "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=800&h=400&fit=crop&crop=center" -o "$OUTPUT_FILE"
fi

FILE_TYPE=$(file -b "$OUTPUT_FILE" | head -1)
if echo "$FILE_TYPE" | grep -qi "jpeg\|jpg"; then
  echo "Saved: $OUTPUT_FILE"
  echo "Add to frontmatter: image: \"/images/articles/$FILENAME.jpg\""
else
  echo "ERROR: Downloaded file is not a JPEG: $FILE_TYPE"
  exit 1
fi
