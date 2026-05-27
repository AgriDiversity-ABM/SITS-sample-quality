import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle, Arc

# ==================== QUALIDADE EDITORIAL ====================

ARTWORK_DPI = 600

plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42

def save_png_svg_pdf_eps(fig, png_path):
    fig.patch.set_facecolor("white")

    base_path, _ = os.path.splitext(png_path)

    fig.savefig(
        png_path,
        bbox_inches="tight",
        dpi=ARTWORK_DPI,
        facecolor="white",
        edgecolor="none",
        format="png",
        metadata={"Software": "Matplotlib", "dpi": str(ARTWORK_DPI)},
        pil_kwargs={"dpi": (ARTWORK_DPI, ARTWORK_DPI), "compress_level": 1}
    )

    fig.savefig(base_path + ".svg", bbox_inches="tight", dpi=ARTWORK_DPI,
                facecolor="white", edgecolor="none", format="svg")

    fig.savefig(base_path + ".pdf", bbox_inches="tight", dpi=ARTWORK_DPI,
                facecolor="white", edgecolor="none", format="pdf")

    fig.savefig(base_path + ".eps", bbox_inches="tight", dpi=ARTWORK_DPI,
                facecolor="white", edgecolor="none", format="eps")


# ==================== ÍCONE SIMPLES DE BASE DE DADOS ====================

def generate_database_icon(output_path="step_1_database_icon.png"):
    fig, ax = plt.subplots(figsize=(2.2, 1.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    x = 5.0
    y_top = 6.1
    y_bottom = 1.9
    width = 6.6
    ell_h = 1.35
    lw = 2.2

    # Corpo
    ax.plot([x - width / 2, x - width / 2], [y_bottom, y_top], color="black", linewidth=lw)
    ax.plot([x + width / 2, x + width / 2], [y_bottom, y_top], color="black", linewidth=lw)

    # Tampa superior
    ax.add_patch(Ellipse(
        (x, y_top),
        width,
        ell_h,
        facecolor="white",
        edgecolor="black",
        linewidth=lw
    ))

    # Arcos internos simples para sugerir camadas do banco
    for y in [4.7, 3.3]:
        ax.add_patch(Arc(
            (x, y),
            width,
            ell_h,
            theta1=180,
            theta2=360,
            color="black",
            linewidth=lw
        ))

    # Base inferior
    ax.add_patch(Arc(
        (x, y_bottom),
        width,
        ell_h,
        theta1=180,
        theta2=360,
        color="black",
        linewidth=lw
    ))

    save_png_svg_pdf_eps(fig, output_path)
    plt.close(fig)


if __name__ == "__main__":
    generate_database_icon("step_1_database_icon.png")