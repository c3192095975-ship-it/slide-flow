#!/usr/bin/env python3
"""Discover installed presentation/PPT skills and emit a capability catalog."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

MAX_READ = 128 * 1024
SKIP_DIRS = {".git", ".hg", ".svn", ".venv", "__pycache__", "node_modules", "dist", "build", ".mypy_cache", ".pytest_cache"}

CAPABILITY_KEYWORDS: dict[str, list[str]] = {
    "story_outline": ["story", "outline", "narrative", "deck plan", "storyboard", "大纲", "故事线", "叙事", "页面计划"],
    "content_evidence": ["research", "evidence", "citation", "data", "fact", "来源", "证据", "数据", "引用"],
    "visual_direction": ["visual", "design system", "brand", "palette", "typography", "color", "视觉", "配色", "字体", "品牌"],
    "visual_asset": ["framework figure", "academic figure", "scientific figure", "figure", "schematic", "mechanism", "vector", "tikz", "svg", "method overview", "toc", "框架图", "机制图", "示意图", "矢量图", "科研绘图"],
    "template_match": ["template", "master", "brand template", "theme", "母版", "模板", "主题"],
    "image_generation": ["image generation", "gpt-image", "imagegen", "image deck", "图片型", "出图", "生成图片"],
    "slide_authoring": ["slide", "deck", "presentation", "powerpoint", "pptx generation", "幻灯片", "演示文稿", "ppt制作"],
    "pptx_editing": ["edit pptx", "pptx manipulation", "patch deck", "merge slides", "编辑ppt", "修改pptx", "合并幻灯片"],
    "html_deck": ["html slides", "html presentation", "reveal.js", "slidev", "web deck", "网页ppt", "html演示"],
    "render_qa": ["render", "screenshot", "overflow", "visual qa", "layout qa", "渲染", "截图", "溢出", "视觉检查"],
    "accessibility": ["accessibility", "wcag", "alt text", "a11y", "无障碍", "对比度", "替代文本"],
    "delivery": ["export", "pdf", "pptx", "package", "deliver", "导出", "打包", "交付"],
    "orchestration": ["orchestrator", "workflow", "end-to-end", "全流程", "总编排"],
}

PPT_CORE_TERMS = [
    "slide", "slides", "deck", "presentation", "powerpoint", "pptx", "google slides",
    "keynote", "html presentation", "html slides", "web deck", "image deck",
    "幻灯片", "演示文稿", "汇报材料", "答辩", "ppt制作", "网页ppt",
]
PPT_AUX_NAMES = {"documents", "pdf", "template-creator", "visualize", "academic-figure-skill", "scientific-visualization", "nature-figure", "figure-library"}
PPT_EXCLUDED_NAMES = {"research-flow"}


@dataclass
class Root:
    path: str
    priority: int
    label: str


@dataclass
class Skill:
    name: str
    description: str
    path: str
    root: str
    root_label: str
    root_priority: int
    format: str = "standard"
    implicit_invocation: bool = True
    has_scripts: bool = False
    script_count: int = 0
    has_references: bool = False
    reference_count: int = 0
    capabilities: list[dict] = field(default_factory=list)
    ppt_relevance: str = "not_ppt"
    required_env_vars: list[str] = field(default_factory=list)
    missing_env_vars: list[str] = field(default_factory=list)
    availability: str = "ready"
    availability_reason: str = "no declared external dependency detected"
    metadata_hash: str = ""
    modified_at: str = ""


def parse_yaml_subset(text: str) -> dict[str, Any]:
    result: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(-1, result)]
    key_re = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")
    lines = text.splitlines(); i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1; continue
        indent = len(line) - len(line.lstrip(" "))
        m = key_re.match(line.strip())
        if not m:
            i += 1; continue
        key, value = m.group(1), m.group(2).strip()
        while stack and indent <= stack[-1][0]: stack.pop()
        parent = stack[-1][1]
        if value in {">", ">-", "|", "|-"}:
            collected=[]
            i += 1
            while i < len(lines):
                child=lines[i]
                if child.strip() and not child[:1].isspace(): break
                if child.strip(): collected.append(child.strip())
                i += 1
            parent[key]=" ".join(collected) if value.startswith(">") else "\n".join(collected)
            continue
        if value == "":
            child={}; parent[key]=child; stack.append((indent,child))
        else:
            v=value
            if len(v)>=2 and v[0]==v[-1] and v[0] in {"'", '"'}: v=v[1:-1]
            parent[key]=v
        i += 1
    return result


def read_limited(path: Path) -> str:
    with path.open("rb") as f:
        return f.read(MAX_READ).decode("utf-8", errors="replace")


def parse_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---"):
        return {}
    parts = text.splitlines()
    end = next((i for i in range(1, len(parts)) if parts[i].strip() == "---"), None)
    return parse_yaml_subset("\n".join(parts[1:end])) if end else {}


def env_vars(text: str) -> list[str]:
    names=set(re.findall(r"\$\{([A-Z][A-Z0-9_]{2,})\}|\$([A-Z][A-Z0-9_]{2,})", text))
    flat={a or b for a,b in names}
    flat-={"HOME","PATH","PWD","USER","SHELL","TMPDIR","CODEX_HOME","SKILL_DIR","PYTHONPATH"}
    return sorted(flat)


def ppt_relevance(name: str, description: str) -> str:
    if name in PPT_EXCLUDED_NAMES:
        return "not_ppt"
    if name in PPT_AUX_NAMES:
        return "ppt_auxiliary"
    primary = (name + "\n" + description).lower()
    if any(term.lower() in primary for term in PPT_CORE_TERMS):
        return "ppt_core"
    return "not_ppt"


def detect_capabilities(name: str, description: str, extra: str) -> list[dict]:
    if name in {"slide-flow", "research-flow"}:
        return [{"name": "orchestration", "score": 100, "matches": ["skill name"]}]
    primary=(name+"\n"+description).lower(); secondary=extra.lower()
    found=[]
    for role, keys in CAPABILITY_KEYWORDS.items():
        matches=[]; score=0
        for key in keys:
            k=key.lower()
            if k in primary: score+=3; matches.append(key)
            elif k in secondary: score+=1; matches.append(key)
        if score: found.append({"name":role,"score":score,"matches":matches[:8]})
    found.sort(key=lambda x:(-x["score"],x["name"]))
    return found[:10]


def find_skill_dirs(root: Path) -> Iterable[tuple[Path,str]]:
    if not root.exists(): return
    for dirpath, dirnames, _ in os.walk(root, followlinks=False):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        d=Path(dirpath)
        if (d/"SKILL.md").is_file():
            yield d,"standard"; dirnames[:]=[]
        elif (d/"manifest.yaml").is_file():
            yield d,"manifest_fallback"; dirnames[:]=[]
        elif (d/"agents"/"openai.yaml").is_file():
            yield d,"metadata_fallback"; dirnames[:]=[]


def count_files(d: Path, suffix: str|None=None) -> int:
    if not d.is_dir(): return 0
    return sum(1 for p in d.rglob("*") if p.is_file() and (not suffix or p.suffix.lower()==suffix))


def record(d: Path, root: Root, kind: str) -> Skill:
    text = read_limited(d/"SKILL.md") if (d/"SKILL.md").is_file() else ""
    fm = parse_frontmatter(text) if text else {}
    manifest={}
    if (d/"manifest.yaml").is_file():
        manifest=parse_yaml_subset(read_limited(d/"manifest.yaml"))
    ui_path=d/"agents"/"openai.yaml"; ui={}
    if ui_path.is_file():
        ui=parse_yaml_subset(read_limited(ui_path))
    name=str(fm.get("name") or manifest.get("name") or d.name)
    desc=str(fm.get("description") or manifest.get("description") or "")
    if not desc:
        readme=d/"README.md"
        if readme.is_file(): desc=" ".join(read_limited(readme).split())[:400]
    extra=" ".join([p.name for p in (d/"scripts").rglob("*") if p.is_file()][:40] + [p.name for p in (d/"references").rglob("*") if p.is_file()][:40]) if (d/"scripts").exists() or (d/"references").exists() else ""
    ui_iface=ui.get("interface",{}) if isinstance(ui.get("interface"),dict) else {}
    policy=ui.get("policy",{}) if isinstance(ui.get("policy"),dict) else {}
    implicit=policy.get("allow_implicit_invocation", True) is not False
    req_env=env_vars(text+"\n"+(read_limited(ui_path) if ui_path.is_file() else ""))
    missing=[v for v in req_env if v not in os.environ]
    if missing:
        availability="unavailable"; reason="missing environment variables: "+", ".join(missing)
    elif kind!="standard":
        availability="unverified"; reason="nonstandard format; execution compatibility not verified"
    else:
        availability="ready"; reason="no declared external dependency detected"
    data=(text or desc or name).encode()
    relevance=ppt_relevance(name,desc)
    caps=detect_capabilities(name,desc,extra)
    if relevance=="ppt_auxiliary":
        caps=[c for c in caps if c["name"] in {"delivery","render_qa","accessibility","template_match","image_generation","visual_asset"}]
    return Skill(
        name=name, description=desc, path=str(d.resolve()), root=root.path, root_label=root.label,
        root_priority=root.priority, format=kind, implicit_invocation=implicit,
        has_scripts=count_files(d/"scripts")>0, script_count=count_files(d/"scripts"),
        has_references=count_files(d/"references",".md")>0, reference_count=count_files(d/"references",".md"),
        capabilities=caps, ppt_relevance=relevance, required_env_vars=req_env,
        missing_env_vars=missing, availability=availability, availability_reason=reason,
        metadata_hash=hashlib.sha256(data).hexdigest()[:16],
        modified_at=datetime.fromtimestamp((d/"SKILL.md").stat().st_mtime,timezone.utc).isoformat() if (d/"SKILL.md").is_file() else "",
    )


def roots(cwd: Path, extra: list[Path], no_defaults: bool, include_plugins: bool) -> list[Root]:
    rs=[]
    for i,p in enumerate(extra): rs.append(Root(str(p.expanduser().resolve()),100-i,"explicit"))
    if no_defaults: return dedupe(rs)
    env=os.environ.get("SLIDE_FLOW_SKILL_ROOTS","")
    for i,x in enumerate(v for v in env.split(os.pathsep) if v.strip()): rs.append(Root(str(Path(x).expanduser().resolve()),95-i,"environment"))
    home=Path.home(); codex=Path(os.environ.get("CODEX_HOME",home/".codex")); cur=cwd.resolve()
    depth=0
    for parent in [cur,*cur.parents]:
        if parent==parent.parent: break
        for rel in (Path(".codex/skills"),Path(".agents/skills"),Path(".claude/skills")):
            p=parent/rel
            if p.is_dir(): rs.append(Root(str(p.resolve()),85-depth*2,"project"))
        depth+=1
    for p,pri,label in [(codex/"skills",80,"codex_home"),(home/".codex/skills",75,"user_codex"),(home/".agents/skills",70,"user_agents"),(home/".claude/skills",65,"user_claude")]:
        rs.append(Root(str(p.resolve()),pri,label))
    if include_plugins:
        for p,pri in [(codex/"plugins/cache",40),(home/".codex/plugins/cache",39)]: rs.append(Root(str(p.resolve()),pri,"plugin_cache"))
    return dedupe(rs)


def dedupe(rs: list[Root]) -> list[Root]:
    best={}
    for r in rs:
        old=best.get(r.path)
        if old is None or r.priority>old.priority: best[r.path]=r
    return sorted(best.values(),key=lambda r:(-r.priority,r.path))


def unique(skills: list[Skill]) -> tuple[list[Skill],dict]:
    groups={}
    for s in skills: groups.setdefault(s.name,[]).append(s)
    chosen=[]; dup={}
    for name,arr in groups.items():
        arr.sort(key=lambda s:(-s.root_priority,len(s.path),s.path)); chosen.append(arr[0])
        if len(arr)>1: dup[name]=[{"path":s.path,"root_label":s.root_label,"priority":s.root_priority} for s in arr[1:]]
    return sorted(chosen,key=lambda s:s.name.lower()),dup


def main(argv=None):
    ap=argparse.ArgumentParser(description="Discover installed slide/PPT skills.")
    ap.add_argument("--root",action="append",default=[])
    ap.add_argument("--no-default-roots",action="store_true")
    ap.add_argument("--include-plugins",action="store_true")
    ap.add_argument("--output")
    args=ap.parse_args(argv)
    rs=roots(Path.cwd(),[Path(x) for x in args.root],args.no_default_roots,args.include_plugins)
    all_skills=[]; errors=[]
    for r in rs:
        if not Path(r.path).exists(): continue
        try:
            for d,kind in find_skill_dirs(Path(r.path)):
                try: all_skills.append(record(d,r,kind))
                except Exception as e: errors.append({"path":str(d),"error":f"{type(e).__name__}: {e}"})
        except Exception as e: errors.append({"path":r.path,"error":f"{type(e).__name__}: {e}"})
    relevant=[s for s in all_skills if s.ppt_relevance in {"ppt_core","ppt_auxiliary"}]
    chosen,dup=unique(relevant)
    core_count=sum(1 for s in chosen if s.ppt_relevance=="ppt_core")
    aux_count=sum(1 for s in chosen if s.ppt_relevance=="ppt_auxiliary")
    payload={
        "schema_version":2,"generated_at":datetime.now(timezone.utc).isoformat(),"cwd":str(Path.cwd()),
        "roots":[asdict(r) for r in rs],
        "summary":{"skill_files_found":len(all_skills),"relevant_skill_files":len(relevant),"unique_skills":len(chosen),"ppt_core":core_count,"ppt_auxiliary":aux_count,"duplicate_names":len(dup),"errors":len(errors)},
        "skills":[asdict(s) for s in chosen],"duplicate_names":dup,"errors":errors,
    }
    out=json.dumps(payload,ensure_ascii=False,indent=2)
    print(out)
    if args.output:
        p=Path(args.output).expanduser(); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(out+"\n",encoding="utf-8")
    return 0

if __name__=="__main__":
    sys.exit(main())
