"""Generate the animated SVGs used in README.md.

Run from the repo root:  python3 assets/generate.py
Edit TERMINAL_SCRIPT below to change what the terminal "types".
"""
import random
from html import escape
from pathlib import Path

OUT = Path(__file__).parent

# Tokyo Night palette (matches the stats cards in the README)
BG, BG2, BORDER = "#16161e", "#1f2335", "#2f334d"
FG, MUTED, COMMENT = "#c0caf5", "#a9b1d6", "#565f89"
BLUE, PURPLE, CYAN, GREEN, RED, YELLOW = "#7aa2f7", "#bb9af7", "#7dcfff", "#9ece6a", "#f7768e", "#e0af68"
SANS = "'Segoe UI', 'Helvetica Neue', Ubuntu, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'DejaVu Sans Mono', 'Liberation Mono', monospace"


def hero():
    rng = random.Random(983)
    stars = []
    for _ in range(46):
        x, y = rng.uniform(10, 990), rng.uniform(10, 270)
        r = rng.choice([0.7, 0.9, 1.1, 1.4, 1.8])
        dur, delay = rng.uniform(2.2, 5.0), rng.uniform(0, 4)
        stars.append(
            f'<circle class="star" cx="{x:.0f}" cy="{y:.0f}" r="{r}" '
            f'style="animation-duration:{dur:.1f}s;animation-delay:{delay:.1f}s"/>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="280" viewBox="0 0 1000 280" role="img" aria-label="Lê Thanh Minh — AI Engineer · Backend Developer · Competitive Programmer">
  <style>
    .star {{ fill: {FG}; animation: twinkle 3s ease-in-out infinite both; }}
    .aurora-a {{ animation: drift-a 14s ease-in-out infinite alternate; }}
    .aurora-b {{ animation: drift-b 18s ease-in-out infinite alternate; }}
    .name {{ font: 800 76px {SANS}; letter-spacing: 1px; stroke-width: 1.4; stroke-dasharray: 1000;
             animation: draw 2.6s ease-out both, fill-in 1.2s ease 1.5s both; }}
    .rule {{ transform-box: fill-box; transform-origin: center; animation: grow 1.2s cubic-bezier(.2,.8,.2,1) 2s both; }}
    .sub {{ font: 500 21px {SANS}; letter-spacing: 1.5px; fill: {MUTED}; animation: rise 1s ease 2.4s both; }}
    .dot {{ fill: {PURPLE}; }}
    @keyframes twinkle {{ 0%, 100% {{ opacity: .15 }} 50% {{ opacity: .9 }} }}
    @keyframes drift-a {{ from {{ transform: translate(-60px, 0) }} to {{ transform: translate(120px, 20px) }} }}
    @keyframes drift-b {{ from {{ transform: translate(80px, 10px) }} to {{ transform: translate(-110px, -15px) }} }}
    @keyframes draw {{ from {{ stroke-dashoffset: 1000 }} to {{ stroke-dashoffset: 0 }} }}
    @keyframes fill-in {{ from {{ fill-opacity: 0 }} to {{ fill-opacity: 1 }} }}
    @keyframes grow {{ from {{ transform: scaleX(0); opacity: 0 }} to {{ transform: scaleX(1); opacity: 1 }} }}
    @keyframes rise {{ from {{ opacity: 0; transform: translateY(12px) }} to {{ opacity: 1; transform: translateY(0) }} }}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <defs>
    <clipPath id="card"><rect width="1000" height="280" rx="18"/></clipPath>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{BG}"/><stop offset="1" stop-color="{BG2}"/>
    </linearGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="520" y2="0" gradientUnits="userSpaceOnUse" spreadMethod="repeat">
      <stop offset="0" stop-color="{BLUE}"/><stop offset=".35" stop-color="{PURPLE}"/>
      <stop offset=".7" stop-color="{CYAN}"/><stop offset="1" stop-color="{BLUE}"/>
      <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="520 0" dur="5s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{BLUE}" stop-opacity="0"/><stop offset=".5" stop-color="{PURPLE}"/>
      <stop offset="1" stop-color="{BLUE}" stop-opacity="0"/>
    </linearGradient>
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="45"/></filter>
    <filter id="glow" x="-10%" y="-40%" width="120%" height="180%">
      <feGaussianBlur stdDeviation="7" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <g clip-path="url(#card)">
    <rect width="1000" height="280" fill="url(#bg)"/>
    <ellipse class="aurora-a" cx="300" cy="90" rx="260" ry="90" fill="{BLUE}" opacity=".22" filter="url(#blur)"/>
    <ellipse class="aurora-b" cx="720" cy="200" rx="280" ry="80" fill="{PURPLE}" opacity=".18" filter="url(#blur)"/>
    {"".join(stars)}
  </g>
  <rect x=".5" y=".5" width="999" height="279" rx="18" fill="none" stroke="{BORDER}"/>
  <text class="name" x="500" y="140" text-anchor="middle" fill="url(#shine)" stroke="url(#shine)" filter="url(#glow)">Lê Thanh Minh</text>
  <rect class="rule" x="370" y="162" width="260" height="2" rx="1" fill="url(#rule)"/>
  <text class="sub" x="500" y="204" text-anchor="middle">AI Engineer <tspan class="dot">·</tspan> Backend Developer <tspan class="dot">·</tspan> Competitive Programmer</text>
</svg>
"""


# (kind, text): "cmd" lines are typed character by character, "out" lines appear at once.
TERMINAL_SCRIPT = [
    ("cmd", "whoami"),
    ("out", [(FG, "Lê Thanh Minh"), (COMMENT, " — "), (MUTED, "AI Engineer & Backend Developer, Ho Chi Minh City")]),
    ("cmd", "cat profile.yml"),
    ("kv", ("education ", "BSc IT @ University of Greenwich · GPA 3.95")),
    ("kv", ("experience", "AI Engineer @ Vingroup · AI Trainer @ Datacurve")),
    ("kv", ("focus     ", "LLM apps (RAG, multi-agent) · Edge AI · Django & FastAPI")),
    ("kv", ("codeforces", "Sagita_Phoenix · Specialist · Round #983 problem setter")),
    ("kv", ("community ", "VNOI · CODEMELY · Dev ơi mình đi đâu thế?")),
    ("kv", ("languages ", "Vietnamese (native) · English (IELTS 7.0)")),
    ("cmd", "echo $MOTTO"),
    ("out", [(YELLOW, '"Life is a journey, not a destination."')]),
]


def terminal():
    type_speed, after_cmd, after_out, hold = 0.075, 0.45, 0.22, 6.0
    lh, x0, y0 = 28, 28, 82
    height = y0 + lh * len(TERMINAL_SCRIPT) + 44

    # First pass: when does each line (and each typed character) appear?
    t, timeline = 0.8, []
    for kind, payload in TERMINAL_SCRIPT:
        if kind == "cmd":
            chars = [t + i * type_speed for i in range(len(payload))]
            timeline.append((t, chars))
            t += len(payload) * type_speed + after_cmd
        else:
            timeline.append((t, None))
            t += after_out
    final_prompt_at = t + 0.2
    cycle = final_prompt_at + hold

    def show(at, attr="visibility"):
        k = at / cycle
        return (f'<animate attributeName="{attr}" values="hidden;visible;hidden" keyTimes="0;{k:.4f};0.985" '
                f'dur="{cycle:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')

    prompt = (f'<tspan fill="{GREEN}">minh</tspan><tspan fill="{COMMENT}"> in </tspan>'
              f'<tspan fill="{BLUE}">~</tspan><tspan fill="{PURPLE}"> ❯ </tspan>')
    lines = []
    for i, ((kind, payload), (at, chars)) in enumerate(zip(TERMINAL_SCRIPT, timeline)):
        y = y0 + i * lh
        if kind == "cmd":
            typed = "".join(f'<tspan fill="{FG}">{escape(c)}{show(ct)}</tspan>' for c, ct in zip(payload, chars))
            lines.append(f'<text x="{x0}" y="{y}">{prompt}{typed}{show(at)}</text>')
        elif kind == "kv":
            key, val = payload
            body = (f'<tspan fill="{CYAN}" xml:space="preserve">  {escape(key)}</tspan><tspan fill="{COMMENT}"> : </tspan>'
                    f'<tspan fill="{MUTED}">{escape(val)}</tspan>')
            lines.append(f'<text x="{x0}" y="{y}" xml:space="preserve">{body}{show(at)}</text>')
        else:
            body = "".join(f'<tspan fill="{c}">{escape(s)}</tspan>' for c, s in payload)
            lines.append(f'<text x="{x0}" y="{y}" xml:space="preserve">  {body}{show(at)}</text>')
    y_final = y0 + len(TERMINAL_SCRIPT) * lh
    cursor = (f'<tspan fill="{FG}">█<animate attributeName="fill-opacity" values="1;0" dur="1.1s" '
              f'calcMode="discrete" repeatCount="indefinite"/></tspan>')
    lines.append(f'<text x="{x0}" y="{y_final}">{prompt}{cursor}{show(final_prompt_at)}</text>')

    body = "\n    ".join(lines)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{height}" viewBox="0 0 900 {height}" role="img" aria-label="Terminal: whoami and cat profile.yml for Lê Thanh Minh">
  <defs>
    <linearGradient id="edge" x1="0" y1="0" x2="900" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{BLUE}"/><stop offset=".5" stop-color="{PURPLE}"/><stop offset="1" stop-color="{CYAN}"/>
      <animateTransform attributeName="gradientTransform" type="rotate" values="0 450 {height / 2};360 450 {height / 2}" dur="8s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="898" height="{height - 2}" rx="14" fill="{BG}" stroke="url(#edge)" stroke-width="1.5" stroke-opacity=".75"/>
  <path d="M1 15 a14 14 0 0 1 14 -14 H885 a14 14 0 0 1 14 14 V40 H1 Z" fill="{BG2}"/>
  <line x1="1" y1="40" x2="899" y2="40" stroke="{BORDER}"/>
  <circle cx="24" cy="21" r="6" fill="{RED}"/><circle cx="44" cy="21" r="6" fill="{YELLOW}"/><circle cx="64" cy="21" r="6" fill="{GREEN}"/>
  <text x="450" y="26" text-anchor="middle" fill="{COMMENT}" font-family="{SANS}" font-size="13">minh@sagita — zsh</text>
  <g font-family="{MONO}" font-size="16">
    {body}
  </g>
</svg>
"""


def divider():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="14" viewBox="0 0 1000 14" role="img" aria-label="">
  <style>
    .comet {{ animation: fly 4.5s cubic-bezier(.45,0,.55,1) infinite; }}
    @keyframes fly {{ from {{ transform: translateX(-240px) }} to {{ transform: translateX(1000px) }} }}
    @media (prefers-reduced-motion: reduce) {{ .comet {{ animation: none; opacity: 0 }} }}
  </style>
  <defs>
    <linearGradient id="base" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{BORDER}" stop-opacity="0"/><stop offset=".5" stop-color="{BORDER}"/>
      <stop offset="1" stop-color="{BORDER}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="tail" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{PURPLE}" stop-opacity="0"/><stop offset=".85" stop-color="{BLUE}"/>
      <stop offset="1" stop-color="{CYAN}"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-300%" width="140%" height="700%"><feGaussianBlur stdDeviation="2.5"/></filter>
  </defs>
  <rect y="6.5" width="1000" height="1" fill="url(#base)"/>
  <g class="comet">
    <rect y="5" width="220" height="4" rx="2" fill="url(#tail)" filter="url(#glow)"/>
    <rect y="6" width="220" height="2" rx="1" fill="url(#tail)"/>
  </g>
</svg>
"""


if __name__ == "__main__":
    for name, build in {"hero.svg": hero, "terminal.svg": terminal, "divider.svg": divider}.items():
        (OUT / name).write_text(build(), encoding="utf-8")
        print("wrote", OUT / name)
