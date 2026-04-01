import random

lines_pool = [
    "[+] attaching to process...",
    "[+] dumping memory regions...",
    "[+] scanning signatures...",
    "[!] suspicious pattern detected",
    "[+] patching exploit...",
    "[+] verifying integrity...",
    "[✓] patch applied successfully"
]

selected = random.sample(lines_pool, 5)

svg_content = f"""
<svg width="700" height="220" xmlns="http://www.w3.org/2000/svg">
<style>
.text {{ fill: #00ff00; font-family: monospace; font-size: 14px; }}
.bg {{ fill: black; }}
</style>

<rect width="100%" height="100%" class="bg"/>

<text x="10" y="30" class="text">root@pulse256:~$ ./ac_engine --scan</text>
"""

y = 60
for line in selected:
    svg_content += f'<text x="10" y="{y}" class="text">{line}</text>\n'
    y += 25

svg_content += f'<text x="10" y="{y+10}" class="text">STATUS: SECURE</text>\n'
svg_content += "</svg>"

with open("terminal.svg", "w") as f:
    f.write(svg_content)
