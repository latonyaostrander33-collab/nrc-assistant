import re

with open(r"C:\Users\25817\.openclaw\workspace-qqbot\nrc-assistant\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix 1: Replace broken ref[1:3] pattern
content = content.replace("amm:'AMM '+ref[1:3]+'-00-00'", "amm:''")

# Add a post-init loop to set amm based on num
old = "// ═══════════════ ZONE MAP ═══════════════"
new = (
    "// Set AMM refs dynamically\n"
    "ATA.forEach(function(a){\n"
    "  var ch = a.num;\n"
    "  var isEngine = ['70','71','72','73','74','75','76','77','78','79','80'].indexOf(ch) >= 0;\n"
    "  a.amm = 'AMM ' + ch + (isEngine ? '-50-00' : '-00-00');\n"
    "});\n"
    "\n"
    "// ═══════════════ ZONE MAP ═══════════════"
)
content = content.replace(old, new)

# Fix 2: Malformed step object in default case
# The bug: {step:'确认缺陷位置和范围,basis:'AMM ...} - comma inside string
old2 = "{step:'确认缺陷位置和范围,basis:'AMM '+best.num+'-00-00',工具:'',warn:''}"
new2 = "{step:'确认缺陷位置和范围',basis:'AMM '+best.num+'-00-00',tool:'',warn:''}"
content = content.replace(old2, new2)

with open(r"C:\Users\25817\.openclaw\workspace-qqbot\nrc-assistant\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Fix applied successfully")
