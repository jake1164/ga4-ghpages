import os
import sys

tracking_id = os.getenv('INPUT_TRACKING_ID')
file = os.getenv('INPUT_FILE')

print(f"Injecting GA4 code for {tracking_id} into {file}")

if not tracking_id:
    print('GA4 Tracking ID not provided. Exiting script.')
    sys.exit(1)

tracking_code = f"""
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={tracking_id}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{tracking_id}');
</script>
<!-- End Google Analytics -->
"""

# check if INPUT_FILE exists
if not file:
    print('File not provided. Exiting script.')

if not os.path.exists(file):
    print(f'File {file} not found. Exiting script.')
    sys.exit(1)

with open(file, 'r+') as f:
    content = f.read()
    if '</head>' in content:
        content = content.replace('</head>', tracking_code + '\n</head>')
        f.seek(0)
        f.write(content)
        f.truncate()
        print(f'Tracking code injected into {file}')
    else:
        print(f'</head> tag not found in {file}')
sys.exit(0)