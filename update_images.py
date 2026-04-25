import os
import re

blog_dir = 'src/content/blog'
files = [f for f in os.listdir(blog_dir) if f.endswith('.md')]

for i, filename in enumerate(sorted(files)):
    file_path = os.path.join(blog_dir, filename)
    
    # Extract industry
    if '-for-' in filename:
        industry = filename.split('-for-')[1].replace('.md', '')
    else:
        # Split by first dash that is not part of a brand like 'monday.com'
        # Actually, most follow brand-industry.md
        parts = filename.split('-')
        if len(parts) > 1:
            industry = '-'.join(parts[1:]).replace('.md', '')
        else:
            industry = 'technology' # fallback
    
    # Clean up industry tag for better search
    tag = industry.replace('-', ',')
    
    new_url = f"https://loremflickr.com/800/600/{tag}?lock={i}"
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace heroImage
    new_content = re.sub(r'heroImage: ".*"', f'heroImage: "{new_url}"', content)
    
    with open(file_path, 'w') as f:
        f.write(new_content)

print(f"Updated {len(files)} files.")
