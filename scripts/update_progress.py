from datetime import datetime
import math
import re

# Configurações
start = datetime(2025, 2, 1)
end = datetime(2028, 12, 1)
total_semesters = 8

# Calcular semestre atual
now = datetime.now()
elapsed_months = (now.year - start.year) * 12 + now.month - start.month
semester = min(max(1, math.floor(elapsed_months / 6) + 1), total_semesters)
progress_percent = (semester / total_semesters) * 100

# Criar barra visual
filled = "🟩" * semester
empty = "⬜" * (total_semesters - semester)
progress_bar = f"{filled}{empty} ({progress_percent:.1f}%)"

# Atualizar README
with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

start_tag = "<!-- PROGRESS_START -->"
end_tag = "<!-- PROGRESS_END -->"
new_block = f"{start_tag}\n📚 Engenharia de Software\n{progress_bar}\n_Semestre atual: {semester} / {total_semesters}_\n{end_tag}"

content = re.sub(f"{start_tag}.*?{end_tag}", new_block, content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as file:
    file.write(content)
