"""
Gera imagens tutoriais passo a passo para o Identificador de Drosofílideos.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
from pathlib import Path

OUT = Path(__file__).parent / "tutorial_imagens"
OUT.mkdir(exist_ok=True)

AZUL_ESCURO  = "#1a3d6e"
AZUL_MEDIO   = "#2d6aad"
VERDE_ESCURO = "#1b6f3c"
VERDE_MEDIO  = "#28a056"
CINZA_BG     = "#f0f2f6"
CINZA_CARD   = "#ffffff"
LARANJA      = "#e07b00"
CINZA_TEXTO  = "#333333"

def salvar(fig, nome):
    fig.savefig(OUT / nome, dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  ✓ {nome}")


# ─────────────────────────────────────────────────────────────────────────────
# PASSO 0 — Visão geral do fluxo
# ─────────────────────────────────────────────────────────────────────────────
def passo0_visao_geral():
    fig, ax = plt.subplots(figsize=(14, 5))
    fig.patch.set_facecolor(CINZA_BG)
    ax.set_facecolor(CINZA_BG)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5)
    ax.axis("off")

    # Título
    ax.text(7, 4.6, "Identificador de Espécies de Drosofílideos — Fluxo Geral",
            ha="center", va="center", fontsize=14, fontweight="bold",
            color=AZUL_ESCURO)

    etapas = [
        ("1\nAcessar\na ferramenta", AZUL_MEDIO),
        ("2\nSelecionar\ncaracterísticas", AZUL_MEDIO),
        ("3\nConsultar\nreferência ⓘ", LARANJA),
        ("4\nClicar em\n'Identificar'", AZUL_MEDIO),
        ("5\nVer\nresultados", VERDE_MEDIO),
    ]

    xs = [1.2, 3.8, 6.4, 9.0, 11.6]
    for (label, cor), x in zip(etapas, xs):
        box = FancyBboxPatch((x - 1.0, 1.2), 2.0, 2.0,
                             boxstyle="round,pad=0.15",
                             linewidth=2, edgecolor=cor,
                             facecolor=cor, alpha=0.88, zorder=3)
        ax.add_patch(box)
        ax.text(x, 2.2, label, ha="center", va="center",
                fontsize=11, fontweight="bold", color="white", zorder=4,
                linespacing=1.4)

    # Setas entre etapas
    for i in range(len(xs) - 1):
        ax.annotate("", xy=(xs[i+1] - 1.05, 2.2),
                    xytext=(xs[i] + 1.05, 2.2),
                    arrowprops=dict(arrowstyle="-|>", color=CINZA_TEXTO,
                                   lw=2, mutation_scale=18),
                    zorder=2)

    ax.text(7, 0.4, "Ferramenta baseada em similaridade morfológica — base de dados taxonômica de Drosofílideos",
            ha="center", va="center", fontsize=9, color=CINZA_TEXTO, style="italic")

    salvar(fig, "passo0_visao_geral.png")


# ─────────────────────────────────────────────────────────────────────────────
# PASSO 1 — Acessar a ferramenta
# ─────────────────────────────────────────────────────────────────────────────
def passo1_acesso():
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor(CINZA_BG)
    ax.set_facecolor(CINZA_BG)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")

    # Badge passo
    badge = FancyBboxPatch((0.3, 5.2), 1.4, 0.6,
                           boxstyle="round,pad=0.1",
                           facecolor=AZUL_MEDIO, edgecolor="none", zorder=3)
    ax.add_patch(badge)
    ax.text(1.0, 5.5, "PASSO 1", ha="center", va="center",
            fontsize=10, fontweight="bold", color="white", zorder=4)

    ax.text(6, 5.5, "Acessar a Ferramenta",
            ha="center", va="center", fontsize=16, fontweight="bold",
            color=AZUL_ESCURO)

    # Simulação do cabeçalho do app
    header = FancyBboxPatch((0.8, 2.8), 10.4, 2.1,
                            boxstyle="round,pad=0.2",
                            facecolor=AZUL_MEDIO, edgecolor=AZUL_ESCURO,
                            linewidth=2, zorder=3)
    ax.add_patch(header)
    ax.text(6, 4.35, "Identificador de Espécies de Drosofílideos",
            ha="center", va="center", fontsize=14, fontweight="bold",
            color="white", zorder=4)
    ax.text(6, 3.75, "Sistema digital de identificação taxonômica baseado em características morfológicas",
            ha="center", va="center", fontsize=9.5, color="white", alpha=0.88, zorder=4)
    ax.text(6, 3.2, "versão 0.5.13-beta",
            ha="center", va="center", fontsize=8, color="white", alpha=0.55, zorder=4)

    # Descrição
    desc = (
        "• Abra o navegador e acesse: localhost:8501\n"
        "• A ferramenta carrega automaticamente a base de dados de espécies\n"
        "• O cabeçalho azul indica que o sistema está pronto para uso"
    )
    ax.text(6, 1.5, desc, ha="center", va="center", fontsize=11,
            color=CINZA_TEXTO, linespacing=1.8,
            bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                      edgecolor="#cccccc", linewidth=1.2))

    salvar(fig, "passo1_acesso.png")


# ─────────────────────────────────────────────────────────────────────────────
# PASSO 2 — Selecionar características morfológicas
# ─────────────────────────────────────────────────────────────────────────────
def passo2_selecionar():
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor(CINZA_BG)
    ax.set_facecolor(CINZA_BG)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.axis("off")

    # Badge
    badge = FancyBboxPatch((0.3, 6.3), 1.4, 0.55,
                           boxstyle="round,pad=0.1",
                           facecolor=AZUL_MEDIO, edgecolor="none", zorder=3)
    ax.add_patch(badge)
    ax.text(1.0, 6.57, "PASSO 2", ha="center", va="center",
            fontsize=10, fontweight="bold", color="white", zorder=4)

    ax.text(7, 6.57, "Selecionar as Características do Espécime",
            ha="center", va="center", fontsize=15, fontweight="bold",
            color=AZUL_ESCURO)

    # Seção "Características observadas"
    secao = FancyBboxPatch((0.5, 4.9), 13, 1.2,
                           boxstyle="round,pad=0.15",
                           facecolor="#e8edf5", edgecolor="#c0cce0",
                           linewidth=1.5, zorder=2)
    ax.add_patch(secao)
    ax.text(1.1, 5.75, "Características observadas",
            ha="left", va="center", fontsize=11, fontweight="bold",
            color=AZUL_ESCURO, zorder=3)
    ax.text(1.1, 5.3, "Selecione as características do espécime. Clique em ⓘ ao lado do nome para ver a referência fotográfica.",
            ha="left", va="center", fontsize=9, color=CINZA_TEXTO, zorder=3, alpha=0.8)

    # Cards de características (grid 3 colunas)
    campos = [
        ("coloração",         "Amarela ▼",       True),
        ("c.p. escutelares",  "Presentes ▼",     True),
        ("c.escutelares",     "Convergente ▼",   True),
        ("c.cuneiformis",     "Ausentes ▼",      True),
        ("pentes sexuais",    "Presentes ▼",     True),
        ("i. costal",         "3.8",             False),
        ("mesonoto cor",      "Amarelo ▼",       True),
        ("veias transversais","Enfumaçadas ▼",   True),
        ("faixas tergitos",   "Desconhecido ▼",  False),
    ]

    cols_x = [1.3, 5.5, 9.7]
    rows_y = [4.2, 3.1, 2.0]

    for idx, (nome, valor, com_info) in enumerate(campos):
        col = idx % 3
        row = idx // 3
        x = cols_x[col]
        y = rows_y[row]

        # Card
        card = FancyBboxPatch((x - 0.9, y - 0.55), 3.8, 1.0,
                              boxstyle="round,pad=0.1",
                              facecolor="white", edgecolor="#c8d0dc",
                              linewidth=1.2, zorder=3)
        ax.add_patch(card)

        # Nome + ⓘ
        if com_info:
            ax.text(x + 1.0, y + 0.28, nome,
                    ha="left", va="center", fontsize=9,
                    fontweight="bold", color=CINZA_TEXTO, zorder=4)
            ax.text(x + 2.7, y + 0.28, "ⓘ",
                    ha="center", va="center", fontsize=9.5,
                    color=AZUL_MEDIO, zorder=4, alpha=0.7)
        else:
            ax.text(x + 1.0, y + 0.28, nome,
                    ha="left", va="center", fontsize=9,
                    fontweight="bold", color=CINZA_TEXTO, zorder=4)

        # Selectbox / input
        sel_color = "#e8f0fe" if valor != "Desconhecido ▼" else "#f5f5f5"
        sel = FancyBboxPatch((x - 0.8, y - 0.48), 3.6, 0.55,
                             boxstyle="round,pad=0.06",
                             facecolor=sel_color, edgecolor="#9aaccf",
                             linewidth=1, zorder=4)
        ax.add_patch(sel)
        ax.text(x + 1.0, y - 0.2, valor,
                ha="left", va="center", fontsize=8.5,
                color=AZUL_ESCURO if valor != "Desconhecido ▼" else "#999",
                zorder=5)

    # Legenda
    ax.text(7, 0.9,
            "Cada campo representa uma característica morfológica do espécime observado ao microscópio.\n"
            "Campos com ⓘ possuem foto de referência. Deixe 'Desconhecido' quando não for possível observar.",
            ha="center", va="center", fontsize=10, color=CINZA_TEXTO,
            linespacing=1.7,
            bbox=dict(boxstyle="round,pad=0.45", facecolor="white",
                      edgecolor="#cccccc", linewidth=1.1))

    salvar(fig, "passo2_selecionar.png")


# ─────────────────────────────────────────────────────────────────────────────
# PASSO 3 — Referência fotográfica (botão ⓘ)
# ─────────────────────────────────────────────────────────────────────────────
def passo3_referencia():
    fig, ax = plt.subplots(figsize=(13, 6.5))
    fig.patch.set_facecolor(CINZA_BG)
    ax.set_facecolor(CINZA_BG)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6.5)
    ax.axis("off")

    # Badge
    badge = FancyBboxPatch((0.3, 5.9), 1.4, 0.5,
                           boxstyle="round,pad=0.1",
                           facecolor=LARANJA, edgecolor="none", zorder=3)
    ax.add_patch(badge)
    ax.text(1.0, 6.15, "PASSO 3", ha="center", va="center",
            fontsize=10, fontweight="bold", color="white", zorder=4)

    ax.text(6.5, 6.15, "Consultar a Referência Fotográfica (opcional)",
            ha="center", va="center", fontsize=15, fontweight="bold",
            color=AZUL_ESCURO)

    # Esquerda — campo com botão ⓘ
    ax.text(1.5, 5.3, "Como acionar:", ha="left", fontsize=11,
            fontweight="bold", color=AZUL_ESCURO)

    # Campo simulado
    campo = FancyBboxPatch((0.4, 3.5), 4.2, 1.5,
                           boxstyle="round,pad=0.15",
                           facecolor="white", edgecolor="#c8d0dc",
                           linewidth=1.5, zorder=3)
    ax.add_patch(campo)
    ax.text(1.1, 4.7, "coloração",
            ha="left", va="center", fontsize=11, fontweight="bold",
            color=CINZA_TEXTO, zorder=4)

    # Botão ⓘ destacado
    info_btn = FancyBboxPatch((4.0, 4.45), 0.45, 0.45,
                              boxstyle="round,pad=0.05",
                              facecolor="#fff3cd", edgecolor=LARANJA,
                              linewidth=2, zorder=4)
    ax.add_patch(info_btn)
    ax.text(4.22, 4.68, "ⓘ", ha="center", va="center",
            fontsize=13, color=LARANJA, fontweight="bold", zorder=5)

    sel2 = FancyBboxPatch((0.6, 3.65), 3.8, 0.55,
                          boxstyle="round,pad=0.06",
                          facecolor="#e8f0fe", edgecolor="#9aaccf",
                          linewidth=1, zorder=4)
    ax.add_patch(sel2)
    ax.text(1.0, 3.93, "Amarela ▼", ha="left", va="center",
            fontsize=9.5, color=AZUL_ESCURO, zorder=5)

    # Seta
    ax.annotate("", xy=(5.1, 4.5), xytext=(4.5, 4.5),
                arrowprops=dict(arrowstyle="-|>", color=LARANJA,
                                lw=2.5, mutation_scale=20))

    # Modal simulado
    modal = FancyBboxPatch((5.2, 0.4), 7.4, 5.6,
                           boxstyle="round,pad=0.2",
                           facecolor="white", edgecolor="#888",
                           linewidth=2, zorder=3)
    ax.add_patch(modal)

    ax.text(8.9, 5.65, "Referência Fotográfica",
            ha="center", va="center", fontsize=12, fontweight="bold",
            color=AZUL_ESCURO, zorder=4)

    # Abas simuladas
    abas = ["Amarela", "Escura", "Acastanhada"]
    tab_colors = [AZUL_MEDIO, "#ccc", "#ccc"]
    for i, (aba, tc) in enumerate(zip(abas, tab_colors)):
        tab = FancyBboxPatch((5.4 + i*2.3, 5.0), 2.1, 0.45,
                             boxstyle="round,pad=0.05",
                             facecolor=tc, edgecolor="none", zorder=4)
        ax.add_patch(tab)
        ax.text(6.45 + i*2.3, 5.22, aba, ha="center", va="center",
                fontsize=9, color="white" if tc != "#ccc" else "#555",
                fontweight="bold" if i==0 else "normal", zorder=5)

    # Área da imagem
    img_area = FancyBboxPatch((6.0, 1.0), 5.8, 3.7,
                              boxstyle="round,pad=0.1",
                              facecolor="#f0f4ff", edgecolor="#c0cce0",
                              linewidth=1.5, zorder=4)
    ax.add_patch(img_area)
    ax.text(8.9, 3.5, "Coloração amarela",
            ha="center", va="center", fontsize=11, fontweight="bold",
            color=AZUL_ESCURO, zorder=5)
    ax.text(8.9, 2.7, "🔬", ha="center", va="center",
            fontsize=32, zorder=5)
    ax.text(8.9, 1.9, "[foto microscópica da característica]",
            ha="center", va="center", fontsize=9,
            color="#888", style="italic", zorder=5)

    # Slider zoom
    ax.text(8.9, 0.75, "Zoom: ——●————  75%",
            ha="center", va="center", fontsize=9,
            color=CINZA_TEXTO, zorder=5)

    ax.text(2.5, 2.8,
            "Clique no ⓘ ao lado\nda característica\npara abrir o modal\ncom fotos de referência",
            ha="center", va="center", fontsize=10,
            color=CINZA_TEXTO, linespacing=1.7,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff8e1",
                      edgecolor=LARANJA, linewidth=1.2))

    salvar(fig, "passo3_referencia.png")


# ─────────────────────────────────────────────────────────────────────────────
# PASSO 4 — Clicar em "Identificar Espécie"
# ─────────────────────────────────────────────────────────────────────────────
def passo4_identificar():
    fig, ax = plt.subplots(figsize=(12, 5.5))
    fig.patch.set_facecolor(CINZA_BG)
    ax.set_facecolor(CINZA_BG)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5.5)
    ax.axis("off")

    badge = FancyBboxPatch((0.3, 4.9), 1.4, 0.5,
                           boxstyle="round,pad=0.1",
                           facecolor=AZUL_MEDIO, edgecolor="none", zorder=3)
    ax.add_patch(badge)
    ax.text(1.0, 5.15, "PASSO 4", ha="center", va="center",
            fontsize=10, fontweight="bold", color="white", zorder=4)

    ax.text(6, 5.15, "Clicar em 'Identificar Espécie'",
            ha="center", va="center", fontsize=15, fontweight="bold",
            color=AZUL_ESCURO)

    # Botão
    btn = FancyBboxPatch((3.8, 3.5), 4.4, 0.9,
                         boxstyle="round,pad=0.15",
                         facecolor=AZUL_MEDIO, edgecolor=AZUL_ESCURO,
                         linewidth=2.5, zorder=3)
    ax.add_patch(btn)
    ax.text(6, 3.95, "Identificar Espécie",
            ha="center", va="center", fontsize=14,
            fontweight="bold", color="white", zorder=4)

    # Seta para baixo
    ax.annotate("", xy=(6, 2.6), xytext=(6, 3.45),
                arrowprops=dict(arrowstyle="-|>", color=AZUL_ESCURO,
                                lw=2.5, mutation_scale=20))

    # Caixas do algoritmo
    alg = FancyBboxPatch((1.0, 1.0), 10.0, 1.4,
                         boxstyle="round,pad=0.15",
                         facecolor="#e8edf5", edgecolor="#a0b4d0",
                         linewidth=1.5, zorder=3)
    ax.add_patch(alg)

    etapas_alg = [
        "Lê características\ninformadas",
        "Ignora campos\n'Desconhecido'",
        "Compara com\ncada espécie",
        "Calcula score:\nmatches / total",
        "Ordena por\nsimilaridade ↓",
    ]
    xs_alg = [1.9, 3.75, 5.7, 7.65, 9.6]
    for i, (etapa, x) in enumerate(zip(etapas_alg, xs_alg)):
        ax.text(x, 1.7, etapa, ha="center", va="center",
                fontsize=8.5, color=AZUL_ESCURO, fontweight="bold",
                linespacing=1.4, zorder=4)
        if i < len(etapas_alg) - 1:
            ax.annotate("", xy=(x + 0.95, 1.7), xytext=(x + 0.4, 1.7),
                        arrowprops=dict(arrowstyle="-|>", color="#555",
                                        lw=1.2, mutation_scale=12), zorder=5)

    ax.text(6, 0.4,
            "O algoritmo de similaridade morfológica compara as características selecionadas\n"
            "com todas as espécies na base de dados e retorna um ranking por similaridade.",
            ha="center", va="center", fontsize=10, color=CINZA_TEXTO,
            linespacing=1.7,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                      edgecolor="#cccccc", linewidth=1.1))

    salvar(fig, "passo4_identificar.png")


# ─────────────────────────────────────────────────────────────────────────────
# PASSO 5 — Resultados
# ─────────────────────────────────────────────────────────────────────────────
def passo5_resultados():
    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor(CINZA_BG)
    ax.set_facecolor(CINZA_BG)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis("off")

    badge = FancyBboxPatch((0.3, 7.4), 1.4, 0.5,
                           boxstyle="round,pad=0.1",
                           facecolor=VERDE_MEDIO, edgecolor="none", zorder=3)
    ax.add_patch(badge)
    ax.text(1.0, 7.65, "PASSO 5", ha="center", va="center",
            fontsize=10, fontweight="bold", color="white", zorder=4)

    ax.text(7, 7.65, "Interpretar os Resultados",
            ha="center", va="center", fontsize=15, fontweight="bold",
            color=AZUL_ESCURO)

    # A — Banner espécie mais provável
    ax.text(0.5, 7.0, "A", fontsize=11, fontweight="bold",
            color=VERDE_ESCURO, va="center")
    banner = FancyBboxPatch((0.5, 5.6), 8.0, 1.3,
                            boxstyle="round,pad=0.15",
                            facecolor=VERDE_MEDIO, edgecolor=VERDE_ESCURO,
                            linewidth=2, zorder=3)
    ax.add_patch(banner)
    ax.text(1.1, 6.65, "ESPÉCIE MAIS PROVÁVEL",
            ha="left", va="center", fontsize=8.5,
            color="white", alpha=0.85, fontweight="bold", zorder=4)
    ax.text(1.1, 6.2, "Drosophila melanogaster",
            ha="left", va="center", fontsize=14,
            color="white", fontweight="bold", style="italic", zorder=4)
    ax.text(1.1, 5.8, "Similaridade morfológica: 87.5%",
            ha="left", va="center", fontsize=10,
            color="white", alpha=0.9, zorder=4)

    # B — Prancha fotográfica
    ax.text(9.0, 7.0, "B", fontsize=11, fontweight="bold",
            color=AZUL_MEDIO, va="center")
    prancha = FancyBboxPatch((9.0, 5.4), 4.5, 1.5,
                             boxstyle="round,pad=0.15",
                             facecolor="#f0f4ff", edgecolor=AZUL_MEDIO,
                             linewidth=1.5, zorder=3)
    ax.add_patch(prancha)
    ax.text(11.25, 6.5, "Prancha fotográfica",
            ha="center", va="center", fontsize=10,
            fontweight="bold", color=AZUL_ESCURO, zorder=4)
    ax.text(11.25, 6.0, "D. melanogaster",
            ha="center", va="center", fontsize=10,
            color=AZUL_MEDIO, style="italic", zorder=4)
    ax.text(11.25, 5.65, "[foto da espécie identificada]",
            ha="center", va="center", fontsize=8.5,
            color="#888", style="italic", zorder=4)

    # C — Top 5
    ax.text(0.5, 5.2, "C", fontsize=11, fontweight="bold",
            color=AZUL_MEDIO, va="center")
    ax.text(0.5, 4.9, "Top 5 espécies mais similares",
            ha="left", va="center", fontsize=11,
            fontweight="bold", color=AZUL_ESCURO)

    especies = [
        ("D. melanogaster",  87.5, VERDE_MEDIO),
        ("D. ananassae",     62.5, "#4a9fd4"),
        ("D. hydei",         50.0, "#4a9fd4"),
        ("D. mercatorum",    37.5, "#4a9fd4"),
        ("D. immigrans",     25.0, "#4a9fd4"),
    ]
    for i, (esp, sim, cor) in enumerate(especies):
        y = 4.35 - i * 0.65
        row_bg = FancyBboxPatch((0.5, y - 0.25), 7.5, 0.48,
                                boxstyle="round,pad=0.04",
                                facecolor="white" if i % 2 == 0 else "#f5f8ff",
                                edgecolor="#dde4f0", linewidth=1, zorder=3)
        ax.add_patch(row_bg)
        ax.text(1.1, y, f"{i+1}. {esp}",
                ha="left", va="center", fontsize=9.5,
                color=CINZA_TEXTO, style="italic", zorder=4)
        bar = FancyBboxPatch((5.2, y - 0.17), sim / 100 * 2.5, 0.34,
                             boxstyle="round,pad=0.03",
                             facecolor=cor, edgecolor="none",
                             alpha=0.85, zorder=4)
        ax.add_patch(bar)
        ax.text(7.85, y, f"{sim}%",
                ha="right", va="center", fontsize=9,
                fontweight="bold", color=cor, zorder=5)

    # D — Gráfico de barras (simplificado)
    ax.text(9.0, 5.2, "D", fontsize=11, fontweight="bold",
            color=AZUL_MEDIO, va="center")
    ax.text(9.0, 4.9, "Gráfico de similaridade",
            ha="left", va="center", fontsize=11,
            fontweight="bold", color=AZUL_ESCURO)

    chart_ax = fig.add_axes([0.66, 0.07, 0.31, 0.5])
    chart_ax.set_facecolor("white")
    esp_nomes = ["D. melan.", "D. ananas.", "D. hydei", "D. mercat.", "D. immig."]
    sims       = [0.875, 0.625, 0.500, 0.375, 0.250]
    colors     = [VERDE_MEDIO] + [AZUL_MEDIO]*4
    bars = chart_ax.barh(esp_nomes[::-1], sims[::-1], color=colors[::-1], height=0.5)
    chart_ax.set_xlim(0, 1.05)
    chart_ax.set_xlabel("Similaridade", fontsize=8)
    chart_ax.tick_params(labelsize=7.5)
    chart_ax.spines[["top","right"]].set_visible(False)
    for bar_p, sim_val in zip(bars, sims[::-1]):
        chart_ax.text(sim_val + 0.01, bar_p.get_y() + bar_p.get_height()/2,
                      f"{sim_val*100:.0f}%", va="center", fontsize=7.5,
                      color=CINZA_TEXTO)

    # E — Expander ranking completo
    exp = FancyBboxPatch((0.5, 0.2), 8.0, 0.8,
                         boxstyle="round,pad=0.1",
                         facecolor="#f0f0f0", edgecolor="#bbbbbb",
                         linewidth=1.2, zorder=3)
    ax.add_patch(exp)
    ax.text(1.0, 0.6, "▶  Ver ranking completo  (expander — mostra todas as espécies da base de dados)",
            ha="left", va="center", fontsize=9.5,
            color="#555", zorder=4)

    salvar(fig, "passo5_resultados.png")


# ─────────────────────────────────────────────────────────────────────────────
# PASSO EXTRA — Como funciona o algoritmo
# ─────────────────────────────────────────────────────────────────────────────
def extra_algoritmo():
    fig, ax = plt.subplots(figsize=(14, 6.5))
    fig.patch.set_facecolor(CINZA_BG)
    ax.set_facecolor(CINZA_BG)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.5)
    ax.axis("off")

    badge = FancyBboxPatch((0.3, 5.9), 1.8, 0.5,
                           boxstyle="round,pad=0.1",
                           facecolor="#6a3d8f", edgecolor="none", zorder=3)
    ax.add_patch(badge)
    ax.text(1.2, 6.15, "EXTRA", ha="center", va="center",
            fontsize=10, fontweight="bold", color="white", zorder=4)

    ax.text(7, 6.15, "Como Funciona o Algoritmo de Similaridade",
            ha="center", va="center", fontsize=15, fontweight="bold",
            color=AZUL_ESCURO)

    # Tabela exemplo
    ax.text(0.5, 5.45, "Exemplo de cálculo:", ha="left", fontsize=11,
            fontweight="bold", color=AZUL_ESCURO)

    headers = ["Característica", "Observado", "D. melanogaster (base)", "Match?"]
    col_xs  = [0.7, 4.0, 7.2, 11.2]
    header_bg = FancyBboxPatch((0.5, 4.65), 13.0, 0.6,
                               boxstyle="square,pad=0",
                               facecolor=AZUL_ESCURO, edgecolor="none", zorder=3)
    ax.add_patch(header_bg)
    for h, cx in zip(headers, col_xs):
        ax.text(cx, 4.95, h, ha="left", va="center",
                fontsize=9.5, fontweight="bold", color="white", zorder=4)

    linhas = [
        ("coloração",        "Amarela",     "Amarela",     True),
        ("c.p. escutelares", "Presentes",   "Presentes",   True),
        ("c.escutelares",    "Convergente", "Divergente",  False),
        ("pentes sexuais",   "Presentes",   "Presentes",   True),
        ("i. costal",        "Desconhecido","—",           None),
        ("c.cuneiformis",    "Ausentes",    "Ausentes",    True),
    ]
    row_colors = ["#f8faff", "white"]
    for i, (carac, obs, base, match) in enumerate(linhas):
        y = 4.2 - i * 0.58
        rb = FancyBboxPatch((0.5, y - 0.25), 13.0, 0.5,
                            boxstyle="square,pad=0",
                            facecolor=row_colors[i % 2], edgecolor="#dde4f0",
                            linewidth=0.8, zorder=3)
        ax.add_patch(rb)
        vals = [carac, obs, base]
        for v, cx in zip(vals, col_xs[:3]):
            ax.text(cx, y, v, ha="left", va="center",
                    fontsize=9, color=CINZA_TEXTO, zorder=4)
        if match is True:
            ax.text(col_xs[3], y, "✔ Sim", ha="left", va="center",
                    fontsize=10, color=VERDE_ESCURO, fontweight="bold", zorder=4)
        elif match is False:
            ax.text(col_xs[3], y, "✘ Não", ha="left", va="center",
                    fontsize=10, color="#c0392b", fontweight="bold", zorder=4)
        else:
            ax.text(col_xs[3], y, "— Ignorado", ha="left", va="center",
                    fontsize=9, color="#999", zorder=4)

    # Fórmula
    formula_bg = FancyBboxPatch((0.5, 0.15), 13.0, 0.85,
                                boxstyle="round,pad=0.1",
                                facecolor="#1a3d6e", edgecolor="none",
                                alpha=0.9, zorder=3)
    ax.add_patch(formula_bg)
    ax.text(7, 0.72,
            "Similaridade  =  correspondências / características informadas  "
            "=  4 / 5  =  80%",
            ha="center", va="center", fontsize=12,
            fontweight="bold", color="white", zorder=4)
    ax.text(7, 0.33,
            "Campos 'Desconhecido' são ignorados. Quanto mais campos preenchidos, mais precisa a identificação.",
            ha="center", va="center", fontsize=9,
            color="white", alpha=0.75, zorder=4)

    salvar(fig, "extra_algoritmo.png")


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Gerando imagens do tutorial...")
    passo0_visao_geral()
    passo1_acesso()
    passo2_selecionar()
    passo3_referencia()
    passo4_identificar()
    passo5_resultados()
    extra_algoritmo()
    print(f"\nPronto! Imagens salvas em: {OUT}")
