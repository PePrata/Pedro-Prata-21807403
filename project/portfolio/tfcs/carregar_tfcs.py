import json
import django
 
django.setup()
 
from portfolio.models import TFC, Tecnologia, Licenciatura, AreaTematica
 
 
def normalizar_grau(degree):
    d = degree.lower()
    if "doutora" in d:
        return "doutoramento"
    if "mestr" in d:
        return "mestrado"
    return "licenciatura"
 
 
with open('portfolio/tfcs/theses.json', encoding='utf-8') as f:  # ← ajuste o caminho se necessário
    dados = json.load(f)
 
criados = 0
for idx, tfc in dados.items():
    titulo = (tfc.get("title") or "").strip()
    autor  = (tfc.get("author") or "").strip()
 
    if not titulo or not autor:
        continue
    if TFC.objects.filter(titulo=titulo, autor=autor).exists():
        continue
 
    degree = tfc.get("degree", "")
    licenciatura, _ = Licenciatura.objects.get_or_create(nome=degree)
 
    obj = TFC.objects.create(
        licenciatura = licenciatura,
        titulo       = titulo,
        autor        = autor,
        email_autor  = (tfc.get("email") or "").strip(),
        supervisor   = (tfc.get("supervisor") or "").strip(),
        grau         = normalizar_grau(degree),
        ano          = int(tfc["year"]) if tfc.get("year") else None,
        resumo       = (tfc.get("resumo") or "").strip(),
        keywords     = (tfc.get("keywords") or "").strip(),
        download     = (tfc.get("download_url") or "").strip(),
        destaque     = 1 if tfc.get("download_url") else 0,
    )
 
    for tech in (tfc.get("techs") or "").split(";"):
        if tech.strip():
            t, _ = Tecnologia.objects.get_or_create(nome=tech.strip())
            obj.tecnologias.add(t)
 
    for area in (tfc.get("areas") or "").split(";"):
        if area.strip():
            a, _ = AreaTematica.objects.get_or_create(nome=area.strip())
            obj.areas.add(a)
 
    criados += 1
 
print(f"Concluído {criados} TFCs criados.")